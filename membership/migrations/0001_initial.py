#@PydevCodeAnalysisIgnore

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table(u'membership_member', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salutation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')()),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'membership', ['Member'])

        # Adding model 'Address'
        db.create_table(u'membership_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('country', self.gf('django.db.models.fields.CharField')(default='Canada', max_length=200)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='address', to=orm['membership.Member'])),
        ))
        db.send_create_signal(u'membership', ['Address'])

        # Adding model 'EmailAddress'
        db.create_table(u'membership_emailaddress', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('address', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email', to=orm['membership.Member'])),
        ))
        db.send_create_signal(u'membership', ['EmailAddress'])

        # Adding model 'PhoneNumber'
        db.create_table(u'membership_phonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone_number', to=orm['membership.Member'])),
        ))
        db.send_create_signal(u'membership', ['PhoneNumber'])

        # Adding model 'EmergencyContact'
        db.create_table(u'membership_emergencycontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='emergency_contact', to=orm['membership.Member'])),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('relationship', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'membership', ['EmergencyContact'])

        # Adding model 'EmergencyContactPhoneNumber'
        db.create_table(u'membership_emergencycontactphonenumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('emergency_contact', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phone_number', to=orm['membership.EmergencyContact'])),
        ))
        db.send_create_signal(u'membership', ['EmergencyContactPhoneNumber'])

        # Adding model 'Season'
        db.create_table(u'membership_season', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'membership', ['Season'])

        # Adding model 'MembershipType'
        db.create_table(u'membership_membershiptype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'membership', ['MembershipType'])

        # Adding model 'Membership'
        db.create_table(u'membership_membership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['membership.Member'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['membership.MembershipType'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['membership.Season'])),
        ))
        db.send_create_signal(u'membership', ['Membership'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table(u'membership_member')

        # Deleting model 'Address'
        db.delete_table(u'membership_address')

        # Deleting model 'EmailAddress'
        db.delete_table(u'membership_emailaddress')

        # Deleting model 'PhoneNumber'
        db.delete_table(u'membership_phonenumber')

        # Deleting model 'EmergencyContact'
        db.delete_table(u'membership_emergencycontact')

        # Deleting model 'EmergencyContactPhoneNumber'
        db.delete_table(u'membership_emergencycontactphonenumber')

        # Deleting model 'Season'
        db.delete_table(u'membership_season')

        # Deleting model 'MembershipType'
        db.delete_table(u'membership_membershiptype')

        # Deleting model 'Membership'
        db.delete_table(u'membership_membership')


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