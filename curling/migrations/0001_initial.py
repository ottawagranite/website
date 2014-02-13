#@PydevCodeAnalysisIgnore

# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'curling_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('jersey', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'curling', ['Player'])

        # Adding model 'Team'
        db.create_table(u'curling_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'curling', ['Team'])

        # Adding model 'TeamPlayer'
        db.create_table(u'curling_teamplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Team'])),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Player'])),
        ))
        db.send_create_signal(u'curling', ['TeamPlayer'])

        # Adding model 'Club'
        db.create_table(u'curling_club', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'curling', ['Club'])

        # Adding model 'Sheet'
        db.create_table(u'curling_sheet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('club', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Club'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'curling', ['Sheet'])

        # Adding model 'Colour'
        db.create_table(u'curling_colour', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('hex', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'curling', ['Colour'])

        # Adding model 'Rock'
        db.create_table(u'curling_rock', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sheet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Sheet'])),
            ('colour', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Colour'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'curling', ['Rock'])

        # Adding model 'League'
        db.create_table(u'curling_league', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('format', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'curling', ['League'])

        # Adding M2M table for field teams on 'League'
        m2m_table_name = db.shorten_name(u'curling_league_teams')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('league', models.ForeignKey(orm[u'curling.league'], null=False)),
            ('team', models.ForeignKey(orm[u'curling.team'], null=False))
        ))
        db.create_unique(m2m_table_name, ['league_id', 'team_id'])

        # Adding model 'Game'
        db.create_table(u'curling_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game', to=orm['curling.Sheet'])),
            ('team_a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_a_team', to=orm['curling.Team'])),
            ('team_b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='game_b_team', to=orm['curling.Team'])),
            ('team_a_colour', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='game_a_colour', to=orm['curling.Colour'])),
            ('team_b_colour', self.gf('django.db.models.fields.related.ForeignKey')
             (related_name='game_b_colour', to=orm['curling.Colour'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'curling', ['Game'])

        # Adding model 'End'
        db.create_table(u'curling_end', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='end', to=orm['curling.Game'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('scoring_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scoring_end', to=orm['curling.Team'])),
        ))
        db.send_create_signal(u'curling', ['End'])

        # Adding model 'Throw'
        db.create_table(u'curling_throw', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('end', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.End'])),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('rock', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Rock'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['curling.Player'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'curling', ['Throw'])

    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'curling_player')

        # Deleting model 'Team'
        db.delete_table(u'curling_team')

        # Deleting model 'TeamPlayer'
        db.delete_table(u'curling_teamplayer')

        # Deleting model 'Club'
        db.delete_table(u'curling_club')

        # Deleting model 'Sheet'
        db.delete_table(u'curling_sheet')

        # Deleting model 'Colour'
        db.delete_table(u'curling_colour')

        # Deleting model 'Rock'
        db.delete_table(u'curling_rock')

        # Deleting model 'League'
        db.delete_table(u'curling_league')

        # Removing M2M table for field teams on 'League'
        db.delete_table(db.shorten_name(u'curling_league_teams'))

        # Deleting model 'Game'
        db.delete_table(u'curling_game')

        # Deleting model 'End'
        db.delete_table(u'curling_end')

        # Deleting model 'Throw'
        db.delete_table(u'curling_throw')

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'curling.club': {
            'Meta': {'object_name': 'Club'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'curling.colour': {
            'Meta': {'object_name': 'Colour'},
            'hex': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'curling.end': {
            'Meta': {'object_name': 'End'},
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'end'", 'to': u"orm['curling.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'scoring_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scoring_end'", 'to': u"orm['curling.Team']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'curling.game': {
            'Meta': {'object_name': 'Game'},
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game'", 'to': u"orm['curling.Sheet']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'team_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_a_team'", 'to': u"orm['curling.Team']"}),
            'team_a_colour': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_a_colour'", 'to': u"orm['curling.Colour']"}),
            'team_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_b_team'", 'to': u"orm['curling.Team']"}),
            'team_b_colour': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_b_colour'", 'to': u"orm['curling.Colour']"})
        },
        u'curling.league': {
            'Meta': {'object_name': 'League'},
            'format': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'league'", 'symmetrical': 'False', 'to': u"orm['curling.Team']"})
        },
        u'curling.player': {
            'Meta': {'object_name': 'Player'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jersey': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'curling.rock': {
            'Meta': {'object_name': 'Rock'},
            'colour': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Colour']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'sheet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Sheet']"})
        },
        u'curling.sheet': {
            'Meta': {'object_name': 'Sheet'},
            'club': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Club']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'curling.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'curling.teamplayer': {
            'Meta': {'object_name': 'TeamPlayer'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Player']"}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Team']"})
        },
        u'curling.throw': {
            'Meta': {'object_name': 'Throw'},
            'end': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.End']"}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Player']"}),
            'rock': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['curling.Rock']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['curling']
