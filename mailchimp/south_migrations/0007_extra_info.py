# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'Campaign.extra_info'
        db.add_column('mailchimp_campaign', 'extra_info', self.gf('django.db.models.fields.TextField')(null=True))

        # Adding field 'Queue.extra_info'
        db.add_column('mailchimp_queue', 'extra_info', self.gf('django.db.models.fields.TextField')(null=True))
    
    
    def backwards(self, orm):
        
        # Deleting field 'Campaign.extra_info'
        db.delete_column('mailchimp_campaign', 'extra_info')

        # Deleting field 'Queue.extra_info'
        db.delete_column('mailchimp_queue', 'extra_info')
    
    
    models = {
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mailchimp.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'campaign_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'extra_info': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'mailchimp.queue': {
            'Meta': {'object_name': 'Queue'},
            'authenticate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_footer': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_tweet': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'campaign_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'extra_info': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'folder_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'generate_text': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'google_analytics': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'segment_options': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'segment_options_all': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'segment_options_conditions': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'to_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'tracking_html_clicks': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tracking_opens': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'tracking_text_clicks': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'type_opts': ('django.db.models.fields.TextField', [], {})
        },
        'mailchimp.reciever': {
            'Meta': {'object_name': 'Reciever'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recievers'", 'to': "orm['mailchimp.Campaign']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['mailchimp']
