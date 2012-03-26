# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Workshop.about_leader'
        db.add_column('workshops_workshop', 'about_leader', self.gf('django.db.models.fields.TextField')(default=u'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd1\x83\xd0\xba\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xb0, \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xbc\xd0\xbe\xd0\xb6\xd0\xbd\xd0\xbe, \xd1\x81 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd0\xb8\xd0\xbd\xd0\xba\xd0\xb0\xd0\xbc\xd0\xb8 \xd0\xb8 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x87\xd0\xb8\xd0\xbc\xd0\xb8 \xd1\x80\xd0\xb0\xd0\xb4\xd0\xbe\xd1\x81\xd1\x82\xd1\x8f\xd0\xbc\xd0\xb8 \xd0\xb6\xd0\xb8\xd0\xb7\xd0\xbd\xd0\xb8', max_length=1000), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Workshop.about_leader'
        db.delete_column('workshops_workshop', 'about_leader')


    models = {
        'applications.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'been_before': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'courses': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'dosug': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'how_long': ('django.db.models.fields.TextField', [], {'max_length': '800'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'onboard': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'questions': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'workplace': ('django.db.models.fields.TextField', [], {'max_length': '300'})
        },
        'workshops.application': {
            'Meta': {'object_name': 'Application'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['applications.Applicant']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'is_interviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshops.Workshop']"})
        },
        'workshops.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'about_leader': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'applicants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['applications.Applicant']", 'through': "orm['workshops.Application']", 'symmetrical': 'False'}),
            'badge': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'contacts': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'fb_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'}),
            'subleader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vk_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['workshops']
