# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Applicant.photo'
        db.add_column('applications_applicant', 'photo', self.gf('django.db.models.fields.files.ImageField')(default=u'applicant-photos/2012-64-18_40_00/dude_what.jpg', max_length=100), keep_default=False)

        # Adding field 'Applicant.view_link'
        db.add_column('applications_applicant', 'view_link', self.gf('django.db.models.fields.CharField')(default=u'8fb11b6c32e861d983d7f000d32120cc6665736028c16777667d85865199d2f232ea6f5871ea40df6486e1d5910e5df74c8fe7895624b95701d4841d233e3efe584364f9bc17864cf4dbfef7cd2070805d2b1516b965e0e77f5ce346e6d6a3817a2efcae', max_length=200), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Applicant.photo'
        db.delete_column('applications_applicant', 'photo')

        # Deleting field 'Applicant.view_link'
        db.delete_column('applications_applicant', 'view_link')


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
        }
    }

    complete_apps = ['applications']
