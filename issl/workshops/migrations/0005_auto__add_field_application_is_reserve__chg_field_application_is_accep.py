# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Application.is_reserve'
        db.add_column('workshops_application', 'is_reserve', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Changing field 'Application.is_accepted'
        db.alter_column('workshops_application', 'is_accepted', self.gf('django.db.models.fields.NullBooleanField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'Application.is_reserve'
        db.delete_column('workshops_application', 'is_reserve')

        # Changing field 'Application.is_accepted'
        db.alter_column('workshops_application', 'is_accepted', self.gf('django.db.models.fields.BooleanField')())


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
        },
        'workshops.application': {
            'Meta': {'object_name': 'Application'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['applications.Applicant']"}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_accepted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'is_interviewed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workshop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshops.Workshop']"})
        },
        'workshops.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'applicants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['applications.Applicant']", 'through': "orm['workshops.Application']", 'symmetrical': 'False'}),
            'badge': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'contacts': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200', 'null': 'True', 'db_index': 'True'}),
            'subleader': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['workshops']
