# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Campaign'
        db.create_table('mailchimp_campaign', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('sent_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('campaign_id', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('mailchimp', ['Campaign'])

        # Adding model 'Reciever'
        db.create_table('mailchimp_reciever', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('campaign', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recievers', to=orm['mailchimp.Campaign'])),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('mailchimp', ['Reciever'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Campaign'
        db.delete_table('mailchimp_campaign')

        # Deleting model 'Reciever'
        db.delete_table('mailchimp_reciever')
    
    
    models = {
        'mailchimp.campaign': {
            'Meta': {'object_name': 'Campaign'},
            'campaign_id': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sent_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'mailchimp.reciever': {
            'Meta': {'object_name': 'Reciever'},
            'campaign': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recievers'", 'to': "orm['mailchimp.Campaign']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['mailchimp']
