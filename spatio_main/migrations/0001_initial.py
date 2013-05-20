# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass

    def backwards(self, orm):
        pass

    models = {
        u'spatio_main.community': {
            'Meta': {'object_name': 'Community', 'db_table': "'communities'", 'managed': 'False'},
            'area': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3785'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spatio_main.State']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'spatio_main.district': {
            'Meta': {'object_name': 'District', 'db_table': "'districts'", 'managed': 'False'},
            'area': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3785'}),
            'community': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spatio_main.Community']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'spatio_main.state': {
            'Meta': {'object_name': 'State', 'db_table': "'states'", 'managed': 'False'},
            'area': ('django.contrib.gis.db.models.fields.GeometryField', [], {'srid': '3785', 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['spatio_main']