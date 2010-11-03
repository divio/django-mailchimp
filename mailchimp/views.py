from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.core.urlresolvers import reverse
from mailchimp.utils import BaseView, Lazy
from mailchimp.models import Campaign, Queue
from mailchimp.settings import WEBHOOK_KEY
from mailchimp.signals import get_signal
import datetime
import re

class MailchimpView(BaseView):
    required_permissions = ['mailchimp.can_view']


class Overview(MailchimpView):    
    def handle_post(self):
        return self.not_allowed()
    
    def handle_get(self):
        data = {
            'paginator': self.paginate(Campaign.objects.all(), self.kwargs.page),
            'queue': Queue.objects.all()
        }
        return self.render_to_response(data)
        
    def get_page_link(self, page):
        return self.reverse('mailchimp_overview', page=page)


class ScheduleCampaignForObject(MailchimpView):
    def auth_check(self):
        basic = super(ScheduleCampaignForObject, self).auth_check()
        if not basic:
            return basic
        return self.request.user.has_perm('mailchimp.can_send')
    
    def handle_post(self):
        return self.not_allowed()
    
    def back(self):
        return self.redirect(self.request.META['HTTP_REFERER'])
    
    def handle_get(self):
        ct = ContentType.objects.get(pk=self.kwargs.content_type)
        obj = ct.model_class().objects.get(pk=self.kwargs.pk)
        if obj.mailchimp_schedule(self.connection):
            self.message_success("The Campaign has been scheduled for sending.")
        else:
            self.message_error("An error has occured while trying to send, please try again later.")
        return self.back()
        
        
class TestCampaignForObjectReal(ScheduleCampaignForObject):
    def handle_get(self):
        ct = ContentType.objects.get(pk=self.kwargs.content_type)
        obj = ct.model_class().objects.get(pk=self.kwargs.pk)
        self.connection.warnings.reset()
        if obj.mailchimp_test(self.connection, self.request):
            self.message_success("A Test Campaign has been sent to your email address (%s)." % self.request.user.email)
            for message, category, filename, lineno in self.connection.warnings.get():
                self.message_warning("%s: %s" % (category.__name__, message))
        else:
            self.message_error("And error has occured while trying to send the test mail to you, please try again later")
        return self.simplejson(True)
    
    
class TestCampaignForObject(ScheduleCampaignForObject):
    template = 'mailchimp/send_test.html'
    
    def handle_get(self):
        data = {
            'ajaxurl': reverse('mailchimp_real_test_for_object', kwargs=self.kwargs),
            'redirecturl': self.request.META['HTTP_REFERER']
        }
        return self.render_to_response(data)


class CampaignInformation(MailchimpView):
    def handle_post(self):
        return self.not_allowed()
    
    def handle_get(self):
        camp = Campaign.objects.get_or_404(campaign_id=self.kwargs.campaign_id)
        data = {'campaign': camp}
        extra_info = camp.get_extra_info()
        if camp.object and hasattr(camp.object, 'mailchimp_get_extra_info'):
            extra_info = camp.object.mailchimp_get_extra_info()
        data['extra_info'] = extra_info
        return self.render_to_response(data)
        

class WebHook(BaseView):
    def handle_get(self):
        return self.response("hello chimp")
    
    def handle_post(self):
        if self.kwargs.key != WEBHOOK_KEY:
            return self.not_found()
        data = self.POST
        signal = get_signal(data['type'])
        ts = data["fired_at"]
        fired_at = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")
        kwargs = {
            'list': self.connection.get_list_by_id(data["data[list_id]"]),
            'fired_at': fired_at,
            'type': data['type'],
        }
        if data['type'] == 'cleaned':
            kwargs.update({
                'reason': data['data[reason]'],
                'email': data['data[email]'],
            })
        elif data['type'] == 'upemail':
            kwargs.update({
                 'old_email': data['data[old_email]'],
                 'new_email': data['data[new_email]'],
            })
        else:
            merge_re = re.compile('data\[merges\]\[(?P<name>w+)\]')
            merges = {}
            for key, value in data.items():
                match = merge_re.match(key)
                if match:
                    name = match.group('name').lower()
                    if name in ('interests', 'fname', 'lname'):
                        continue
                    merges[name] = value
            kwargs.update({
                'email': data['data[email]'],
                'interests': data['data[merges][INTERESTS]'].split(','),
                'fname': data['data[merges][FNAME]'],
                'lname': data['data[merges][LNAME]'],
                'merges': merges,
            })
        signal.send(sender=self.connection, **kwargs)
        return self.response("ok")

        
class Dequeue(ScheduleCampaignForObject):
    def handle_get(self):
        q = Queue.objects.get_or_404(pk=self.kwargs.id)
        if q.send():
            self.message_success("The Campaign has successfully been dequeued.")
        else:
            self.message_error("An error has occured while trying to dequeue this campaign, please try again later.")
        return self.back()
        

class Cancel(ScheduleCampaignForObject):
    def handle_get(self):
        q = Queue.objects.get_or_404(pk=self.kwargs.id)
        q.delete()
        self.message_success("The Campaign has been canceled.")
        return self.back()
    
    
class BaseSubscribe(BaseView):
    form = BaseRegisterForm
    template = 'mailchimp/subscribe.html'
    
    def handle_get(self):
        return self.render_to_response({'form': self.form()})
        
    def handle_post(self):
        form = self.form(self.request.POST)
        if form.is_valid():
            return self.render_to_response({'success': True})
        return self.render_to_response({'form': form})

webhook = WebHook()
dequeue = Dequeue()
cancel = Cancel()
campaign_information = CampaignInformation()
overview = Overview()
schedule_campaign_for_object = ScheduleCampaignForObject()
test_campaign_for_object = TestCampaignForObject()
test_real = TestCampaignForObjectReal()