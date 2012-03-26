# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Workshop.short_name'
        db.add_column('workshops_workshop', 'short_name', self.gf('django.db.models.fields.CharField')(default=u'\xd0\xba\xd0\xbe\xd1\x80\xd0\xbe\xd1\x82\xd0\xba\xd0\xbe\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x85\xd0\xb5\xd1\x85\xd0\xb5', max_length=200), keep_default=False)

        # Adding field 'Application.edit_link'
        db.add_column('workshops_application', 'edit_link', self.gf('django.db.models.fields.CharField')(default=u'0662eadc7bb2784e4caa5843c9716eab63ca4c516748c9040c2469f11c70b81061aadb4e5b3a20823ea32290273b03c91e94dc7f1ce621cfdb3f63a09a6112d0884e637ea055ffc2fd4bb8adb1c942421e0a00d551572cb5109e9d80c5d16676721bba7d', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Workshop.short_name'
        db.delete_column('workshops_workshop', 'short_name')

        # Deleting field 'Application.edit_link'
        db.delete_column('workshops_application', 'edit_link')


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
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'questions': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'view_link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'workplace': ('django.db.models.fields.TextField', [], {'max_length': '300'})
        },
        'workshops.application': {
            'Meta': {'object_name': 'Application'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['applications.Applicant']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {}),
            'edit_link': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.NullBooleanField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'is_interviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshops.Workshop']"})
        },
        'workshops.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'about_leader': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'blank': 'True'}),
            'applicants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['applications.Applicant']", 'through': "orm['workshops.Application']", 'symmetrical': 'False'}),
            'badge': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'contacts': ('django.db.models.fields.TextField', [], {'max_length': '300', 'blank': 'True'}),
            'fb_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'}),
            'subleader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'vk_group': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['workshops']
