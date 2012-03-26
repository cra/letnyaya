# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Applicant.has_sleepbag'
        db.delete_column('applications_applicant', 'has_sleepbag')

        # Deleting field 'Applicant.education'
        db.delete_column('applications_applicant', 'education')

        # Deleting field 'Applicant.has_carrymat'
        db.delete_column('applications_applicant', 'has_carrymat')

        # Deleting field 'Applicant.workshop'
        db.delete_column('applications_applicant', 'workshop_id')

        # Deleting field 'Applicant.has_backpack'
        db.delete_column('applications_applicant', 'has_backpack')

        # Deleting field 'Applicant.has_tent'
        db.delete_column('applications_applicant', 'has_tent')

        # Adding field 'Applicant.workplace'
        db.add_column('applications_applicant', 'workplace', self.gf('django.db.models.fields.TextField')(default=u'undefined', max_length=300), keep_default=False)

        # Adding field 'Applicant.job'
        db.add_column('applications_applicant', 'job', self.gf('django.db.models.fields.CharField')(default=u'undefined', max_length=300), keep_default=False)

        # Adding field 'Applicant.onboard'
        db.add_column('applications_applicant', 'onboard', self.gf('django.db.models.fields.CharField')(default=u'\xd0\xbf\xd0\xb8\xd1\x82\xd1\x8c \xd0\xba\xd1\x83\xd1\x80\xd0\xb8\xd1\x82\xd1\x8c \xd0\xb8 \xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f. undefined', max_length=500), keep_default=False)

        # Adding field 'Applicant.been_before'
        db.add_column('applications_applicant', 'been_before', self.gf('django.db.models.fields.CharField')(default=u'0', max_length=300), keep_default=False)

        # Adding field 'Applicant.how_long'
        db.add_column('applications_applicant', 'how_long', self.gf('django.db.models.fields.TextField')(default=u'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x87\xd0\xb0\xd1\x81\xd0\xb0. undefined', max_length=800), keep_default=False)

        # Adding field 'Applicant.courses'
        db.add_column('applications_applicant', 'courses', self.gf('django.db.models.fields.CharField')(default=u'\xd1\x83\xd0\xbb\xd0\xb8\xd1\x87\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xbc\xd0\xb0\xd0\xb3\xd0\xb8\xd1\x8f', max_length=500), keep_default=False)

        # Adding field 'Applicant.dosug'
        db.add_column('applications_applicant', 'dosug', self.gf('django.db.models.fields.CharField')(default=u'\xd1\x8d\xd0\xba\xd1\x81\xd0\xb1\xd0\xb8\xd1\x86\xd0\xb8\xd0\xbe\xd0\xbd\xd0\xb8\xd0\xb7\xd0\xbc', max_length=500), keep_default=False)

        # Adding field 'Applicant.money'
        db.add_column('applications_applicant', 'money', self.gf('django.db.models.fields.CharField')(default=u'\xd0\xbd\xd0\xb8\xd1\x89\xd0\xb5\xd0\xb1\xd1\x80\xd0\xbe\xd0\xb4\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe', max_length=150), keep_default=False)

        # Changing field 'Applicant.city'
        db.alter_column('applications_applicant', 'city', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Applicant.name'
        db.alter_column('applications_applicant', 'name', self.gf('django.db.models.fields.CharField')(max_length=150))


    def backwards(self, orm):
        
        # Adding field 'Applicant.has_sleepbag'
        db.add_column('applications_applicant', 'has_sleepbag', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Applicant.education'
        raise RuntimeError("Cannot reverse this migration. 'Applicant.education' and its values cannot be restored.")

        # Adding field 'Applicant.has_carrymat'
        db.add_column('applications_applicant', 'has_carrymat', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Applicant.workshop'
        raise RuntimeError("Cannot reverse this migration. 'Applicant.workshop' and its values cannot be restored.")

        # Adding field 'Applicant.has_backpack'
        db.add_column('applications_applicant', 'has_backpack', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Applicant.has_tent'
        db.add_column('applications_applicant', 'has_tent', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Applicant.workplace'
        db.delete_column('applications_applicant', 'workplace')

        # Deleting field 'Applicant.job'
        db.delete_column('applications_applicant', 'job')

        # Deleting field 'Applicant.onboard'
        db.delete_column('applications_applicant', 'onboard')

        # Deleting field 'Applicant.been_before'
        db.delete_column('applications_applicant', 'been_before')

        # Deleting field 'Applicant.how_long'
        db.delete_column('applications_applicant', 'how_long')

        # Deleting field 'Applicant.courses'
        db.delete_column('applications_applicant', 'courses')

        # Deleting field 'Applicant.dosug'
        db.delete_column('applications_applicant', 'dosug')

        # Deleting field 'Applicant.money'
        db.delete_column('applications_applicant', 'money')

        # Changing field 'Applicant.city'
        db.alter_column('applications_applicant', 'city', self.gf('django.db.models.fields.CharField')(max_length=60))

        # Changing field 'Applicant.name'
        db.alter_column('applications_applicant', 'name', self.gf('django.db.models.fields.CharField')(max_length=60))


    models = {
        'applications.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'been_before': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'courses': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'dosug': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'how_long': ('django.db.models.fields.TextField', [], {'max_length': '800'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'money': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'onboard': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'questions': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'workplace': ('django.db.models.fields.TextField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['applications']
