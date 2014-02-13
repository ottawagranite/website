#@PydevCodeAnalysisIgnore

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OttawaGraniteMember'
        db.create_table(u'ottawagranite_ottawagranitemember', (
            (u'member_ptr', self.gf('django.db.models.fields.related.OneToOneField')
             (to=orm['membership.Member'], unique=True, primary_key=True)),
            ('membership_number', self.gf('django.db.models.fields.IntegerField')()),
            ('latest_membership', self.gf('django.db.models.fields.IntegerField')()),
            ('earliest_membership', self.gf('django.db.models.fields.IntegerField')()),
            ('started_curling', self.gf('django.db.models.fields.IntegerField')()),
            ('rookie_year', self.gf('django.db.models.fields.IntegerField')()),
            ('locker_number', self.gf('django.db.models.fields.IntegerField')()),
            ('parking_stickers', self.gf('django.db.models.fields.IntegerField')()),
            ('social', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('honorary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('instructor', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'ottawagranite', ['OttawaGraniteMember'])

        # Adding model 'OttawaGraniteLeague'
        db.create_table(u'ottawagranite_ottawagraniteleague', (
            (u'league_ptr', self.gf('django.db.models.fields.related.OneToOneField')
             (to=orm['curling.League'], unique=True, primary_key=True)),
            ('rating', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'ottawagranite', ['OttawaGraniteLeague'])

    def backwards(self, orm):
        # Deleting model 'OttawaGraniteMember'
        db.delete_table(u'ottawagranite_ottawagranitemember')

        # Deleting model 'OttawaGraniteLeague'
        db.delete_table(u'ottawagranite_ottawagraniteleague')

    models = {
        u'curling.league': {
            'Meta': {'object_name': 'League'},
            'format': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'league'", 'symmetrical': 'False', 'to': u"orm['curling.Team']"})
        },
        u'curling.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'membership.member': {
            'Meta': {'object_name': 'Member'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ottawagranite.ottawagraniteleague': {
            'Meta': {'object_name': 'OttawaGraniteLeague', '_ormbases': [u'curling.League']},
            u'league_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['curling.League']", 'unique': 'True', 'primary_key': 'True'}),
            'rating': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        u'ottawagranite.ottawagranitemember': {
            'Meta': {'object_name': 'OttawaGraniteMember', '_ormbases': [u'membership.Member']},
            'earliest_membership': ('django.db.models.fields.IntegerField', [], {}),
            'honorary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'instructor': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'latest_membership': ('django.db.models.fields.IntegerField', [], {}),
            'locker_number': ('django.db.models.fields.IntegerField', [], {}),
            u'member_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['membership.Member']", 'unique': 'True', 'primary_key': 'True'}),
            'membership_number': ('django.db.models.fields.IntegerField', [], {}),
            'parking_stickers': ('django.db.models.fields.IntegerField', [], {}),
            'rookie_year': ('django.db.models.fields.IntegerField', [], {}),
            'social': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'started_curling': ('django.db.models.fields.IntegerField', [], {}),
            'student': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['ottawagranite']
