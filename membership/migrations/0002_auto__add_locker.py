#@PydevCodeAnalysisIgnore

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Locker'
        db.create_table(u'membership_locker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('current_member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['membership.Member'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'membership', ['Locker'])

    def backwards(self, orm):
        # Deleting model 'Locker'
        db.delete_table(u'membership_locker')

    models = {
        u'membership.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Canada'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'address'", 'to': u"orm['membership.Member']"}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'membership.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'address': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email'", 'to': u"orm['membership.Member']"}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'membership.emergencycontact': {
            'Meta': {'object_name': 'EmergencyContact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emergency_contact'", 'to': u"orm['membership.Member']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'relationship': ('django.db.models.fields.TextField', [], {})
        },
        u'membership.emergencycontactphonenumber': {
            'Meta': {'object_name': 'EmergencyContactPhoneNumber'},
            'emergency_contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_number'", 'to': u"orm['membership.EmergencyContact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'membership.locker': {
            'Meta': {'object_name': 'Locker'},
            'current_member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['membership.Member']"}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'membership.member': {
            'Meta': {'object_name': 'Member'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salutation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'membership.membership': {
            'Meta': {'object_name': 'Membership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['membership.Member']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['membership.Season']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['membership.MembershipType']"})
        },
        u'membership.membershiptype': {
            'Meta': {'object_name': 'MembershipType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'membership.phonenumber': {
            'Meta': {'object_name': 'PhoneNumber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phone_number'", 'to': u"orm['membership.Member']"}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'membership.season': {
            'Meta': {'object_name': 'Season'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['membership']
