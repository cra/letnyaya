# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Applicant'
        db.create_table('applications_applicant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('telephone', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('age', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('education', self.gf('django.db.models.fields.TextField')(max_length=400)),
            ('questions', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('has_sleepbag', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_carrymat', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_backpack', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('has_tent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('applications', ['Applicant'])


    def backwards(self, orm):
        
        # Deleting model 'Applicant'
        db.delete_table('applications_applicant')


    models = {
        'applications.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'age': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'education': ('django.db.models.fields.TextField', [], {'max_length': '400'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'has_backpack': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_carrymat': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_sleepbag': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'has_tent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'questions': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        }
    }

    complete_apps = ['applications']
