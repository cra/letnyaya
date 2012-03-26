# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Workshop.subleader'
        db.add_column('workshops_workshop', 'subleader', self.gf('django.db.models.fields.EmailField')(default=u'gri-tarasevich@yandex.ua', max_length=75), keep_default=False)

        # Adding field 'Workshop.visible'
        db.add_column('workshops_workshop', 'visible', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Workshop.subleader'
        db.delete_column('workshops_workshop', 'subleader')

        # Deleting field 'Workshop.visible'
        db.delete_column('workshops_workshop', 'visible')


    models = {
        'workshops.workshop': {
            'Meta': {'object_name': 'Workshop'},
            'about': ('django.db.models.fields.TextField', [], {}),
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
