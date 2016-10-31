# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 08:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curling', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='league',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='league', to='curling.Team', verbose_name='teams'),
        ),
        migrations.AddField(
            model_name='game',
            name='sheet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='curling.Sheet', verbose_name='sheet'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_a_team', to='curling.Team', verbose_name='team a'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_a_colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_a_colour', to='curling.Colour', verbose_name='team a colour'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_b_team', to='curling.Team', verbose_name='team b'),
        ),
        migrations.AddField(
            model_name='game',
            name='team_b_colour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_b_colour', to='curling.Colour', verbose_name='team b colour'),
        ),
        migrations.AddField(
            model_name='end',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end', to='curling.Game', verbose_name='game'),
        ),
        migrations.AddField(
            model_name='end',
            name='scoring_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scoring_end', to='curling.Team', verbose_name='scoring_team'),
        ),
    ]
