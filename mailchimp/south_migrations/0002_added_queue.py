# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Queue'
        db.create_table('mailchimp_queue', (
            ('type_opts', self.gf('django.db.models.fields.TextField')()),
            ('segment_options_all', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('campaign_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('authenticate', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('from_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('segment_options', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('list_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('auto_tweet', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('from_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('folder_id', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('generate_text', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('to_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('tracking_text_clicks', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('auto_footer', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('tracking_html_clicks', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('google_analytics', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('segment_options_conditions', self.gf('django.db.models.fields.TextField')()),
            ('template_id', self.gf('django.db.models.fields.IntegerField')()),
            ('tracking_opens', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('mailchimp', ['Queue'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Queue'
        db.delete_table('mailchimp_queue')
    
    
    models = {
        'mailchimp.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'campaign_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'mailchimp.queue': {
            'Meta': {'object_name': 'Queue'},
            'authenticate': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_footer': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'auto_tweet': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'campaign_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contents': ('django.db.models.fields.TextField', [], {}),
            'folder_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'from_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'from_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'generate_text': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'google_analytics': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'segment_options': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'segment_options_all': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'segment_options_conditions': ('django.db.models.fields.TextField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
