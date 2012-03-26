# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Workshop.telephone'
        db.delete_column('workshops_workshop', 'telephone')

        # Adding field 'Workshop.slug'
        db.add_column('workshops_workshop', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=200, null=True, db_index=True), keep_default=False)

        # Adding field 'Workshop.about'
        db.add_column('workshops_workshop', 'about', self.gf('django.db.models.fields.TextField')(default=u'\xd0\x9e\xd0\xb1 \xd1\x8d\xd1\x82\xd0\xbe\xd0\xb9 \xd0\xbc\xd0\xb0\xd1\x81\xd1\x82\xd0\xb5\xd1\x80\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9'), keep_default=False)

        # Adding field 'Workshop.badge'
        db.add_column('workshops_workshop', 'badge', self.gf('django.db.models.fields.files.ImageField')(default=u'/tmp/badje.png', max_length=100), keep_default=False)

        # Adding field 'Workshop.contacts'
        db.add_column('workshops_workshop', 'contacts', self.gf('django.db.models.fields.TextField')(default=u'Contactzzz', max_length=300), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Workshop.telephone'
        db.add_column('workshops_workshop', 'telephone', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True), keep_default=False)

        # Deleting field 'Workshop.slug'
        db.delete_column('workshops_workshop', 'slug')

        # Deleting field 'Workshop.about'
        db.delete_column('workshops_workshop', 'about')

        # Deleting field 'Workshop.badge'
        db.delete_column('workshops_workshop', 'badge')

        # Deleting field 'Workshop.contacts'
        db.delete_column('workshops_workshop', 'contacts')


    models = {
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

    complete_apps = ['workshops']
