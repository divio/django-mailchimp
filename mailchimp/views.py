from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from mailchimp.utils import View, Lazy
from mailchimp.models import Campaign
from mailchimp.settings import WEBHOOK_KEY
from mailchimp.signals import get_signal
import datetime

class MailchimpView(View):
    def auth_check(self):
        return self.request.user.has_perm('mailchimp.can_view')


class Overview(MailchimpView):    
    def handle_post(self):
        return self.not_allowed()
    
    def handle_get(self):
        self.data['paginator'] = self.paginate(Campaign.objects.all(), self.kwargs.page)
        
    def get_page_link(self, page):
        return self.reverse('mailchimp_overview', page=page)


class SendCampaign(MailchimpView):
    
    def auth_check(self):
        basic = super(SendCampaign, self).auth_check()
        if not basic:
            return basic
        return self.request.user.has_perm('mailchimp.can_send')
        
    def get_form(self):
        return 
    
    def handle_get(self):
        # display a form?
        self.data['form'] = self.get_form()
        
    def handle_post(self):
        form = self.get_form(self.POST)
        if form.is_valid():
            if self.handle_campaign(form):
                self.message_success("The Campaign has been scheduled for sending.")
                return self.redirect('mailchimp_overview')
            else:
                self.message_error("An error has occured while trying to send, please try again later.")
        self.data['form'] = form
            
    def handle_campaign(self, data):
        return self.send(self.create(**data))
        
    def create(self, **kwargs):
        return self.connection.create_campaign(**kwargs)
    
    def send(self, camp):
        return camp.schedule(datetime.datetime.now())


class ScheduleCampaignForObject(SendCampaign):
    def handle_post(self):
        return self.not_allowed()
    
    def handle_get(self):
        ct = ContentType.objects.get(pk=self.kwargs.content_type)
        obj = ct.model_class().objects.get(pk=self.kwargs.pk)
        if obj.mailchimp_schedule(self.connection):
            self.message_success("The Campaign has been scheduled for sending.")
            return self.redirect_raw(self.request.META['HTTP_REFERER'])
        else:
            self.message_error("An error has occured while trying to send, please try again later.")
            return self.redirect_raw(self.request.META['HTTP_REFERER'])


class CampaignInformation(MailchimpView):
    def handle_post(self):
        return self.not_allowed()
    
    def handle_get(self):
        self.data['campaign'] = Campaign.objects.get_or_404(campaign_id=self.kwargs.campaign_id)
        

class WebHook(View):
    def handle_get(self):
        return self.not_found()
    
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
            'email': data['data[email]'],
            'type': data['type'],
        }
        if data['type'] == 'cleaned':
            kwargs.update({
                'reason': data['data[reason]'],
            })
        else:
            kwargs.update({
                'interests': data['data[merges][INTERESTS]'].split(','),
                'fname': data['data[merges][FNAME]'],
                'lname': data['data[merges][LNAME]'],
            })
        signal.send(sender=self.connection, **kwargs)

webhook = WebHook()
campaign_information = CampaignInformation()
send_campaign = SendCampaign()
overview = Overview()
schedule_campaign_for_object = ScheduleCampaignForObject()