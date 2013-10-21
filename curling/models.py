from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.query_utils import Q

from curling.choices import PLAYER_GENDER_CHOICES, LEAGUE_FORMAT_CHOICES, \
    POSITION_CHOICES
from curling.league_format import league_formats
from curling.settings import REQUIRE_GENDER


# Teams
class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, required=False)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=1, choices=PLAYER_GENDER_CHOICES)
    jersey = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        if self.first_name and self.last_name:
            return u'%s %s' % (self.first_name, self.last_name)
        elif self.last_name:
            return self.last_name
        elif self.jersey:
            return self.jersey
        else:
            return 'Player %s' % self.pk

    def clean(self):
        if REQUIRE_GENDER and not self.gender:
            raise ValidationError('A value for gender is required.')


class Team(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return self.name or 'Team %s' % self.pk

    def games(self):
        return Game.objects.filter(Q(team_a=self) | Q(team_b=self))


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    player = models.ForeignKey(Player)

    def __unicode__(self):
        return u'%s %s %s' % (self.team, self.position, self.player)


# Clubs
class Club(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Sheet(models.Model):
    club = models.ForeignKey(Club)
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s: %s' % (self.club, self.name)


# Rocks
class Colour(models.Model):
    name = models.CharField(max_length=100)
    hex = models.CharField(max_length=6, validators=[RegexValidator('^[0-9a-fA-F]{6}$', 'Not a valid hex code', 'Invalid Code')])

    def __unicode__(self):
        return u'%s: %s' % (self.name, self.hex)


class Rock(models.Model):
    sheet = models.ForeignKey(Sheet)
    colour = models.ForeignKey(Colour)
    number = models.CharField(max_length=1)

    def __unicode__(self):
        return u'%s: %s %s' % (self.sheet, self.colour, self.number)


# League
class League(models.Model):
    name = models.CharField(max_length=100)
    teams = models.ManyToManyField(Team, related_name='league')
    format = models.CharField(max_length=10, choices=LEAGUE_FORMAT_CHOICES)

    def validate(self):
        for validator in league_formats[self.format]['team_validators']:
            for team in self.teams.all():
                validator(team)

    def __unicode__(self):
        return u'%s: %s' % (self.position, self.player)


# Games
class Game(models.Model):
    sheet = models.ForeignKey(Sheet, related_name='game')
    team_a = models.ForeignKey(Team)
    team_b = models.ForeignKey(Team)
    team_a_colour = models.ForeignKey(Colour)
    team_b_colour = models.ForeignKey(Colour)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.sheet, self.start_time)


class End(models.Model):
    game = models.ForeignKey(Game, related_name='end')
    number = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    scoring_team = models.ForeignKey(Team, related_name='scoring_end')

    def __unicode__(self):
        return u'%s: %s' % (self.game, self.end)


class Throw(models.Model):
    end = models.ForeignKey(End)
    number = models.IntegerField()
    rock = models.ForeignKey(Rock)
    player = models.ForeignKey(Player)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.end, self.number)
