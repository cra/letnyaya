# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Applicant.workshop'
        db.add_column('applications_applicant', 'workshop', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['workshops.Workshop']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Applicant.workshop'
        db.delete_column('applications_applicant', 'workshop_id')


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
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshops.Workshop']"})
        },
        'workshops.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'badge': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'contacts': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['applications']
