# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Applicant.courses'
        db.alter_column('applications_applicant', 'courses', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'Applicant.dosug'
        db.alter_column('applications_applicant', 'dosug', self.gf('django.db.models.fields.TextField')(max_length=500))

        # Changing field 'Applicant.onboard'
        db.alter_column('applications_applicant', 'onboard', self.gf('django.db.models.fields.TextField')(max_length=500))


    def backwards(self, orm):
        
        # Changing field 'Applicant.courses'
        db.alter_column('applications_applicant', 'courses', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Applicant.dosug'
        db.alter_column('applications_applicant', 'dosug', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Applicant.onboard'
        db.alter_column('applications_applicant', 'onboard', self.gf('django.db.models.fields.CharField')(max_length=500))


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
        }
    }

    complete_apps = ['applications']
