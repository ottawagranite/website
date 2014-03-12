from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.query_utils import Q
from django.utils.translation import ugettext_lazy as _

from curling.choices import PLAYER_GENDER_CHOICES, LEAGUE_FORMAT_CHOICES, \
    POSITION_CHOICES
from curling.league_format import league_formats
from django.conf import settings


# Teams
class Player(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('user'), blank=True, null=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    gender = models.CharField(_('gender'), max_length=1, choices=PLAYER_GENDER_CHOICES)
    jersey = models.CharField(_('jersey'), max_length=100, blank=True)

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
        if settings.CURLING_REQUIRE_GENDER and not self.gender:
            raise ValidationError('A value for gender is required.')


class Team(models.Model):
    name = models.CharField(_('name'), max_length=100, blank=True)

    def __unicode__(self):
        return self.name or 'Team %s' % self.pk

    def games(self):
        return Game.objects.filter(Q(team_a=self) | Q(team_b=self))


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team, verbose_name=_('team'))
    position = models.CharField(_('position'), max_length=50, choices=POSITION_CHOICES)
    player = models.ForeignKey(Player, verbose_name=_('player'))

    def __unicode__(self):
        return u'%s %s %s' % (self.team, self.position, self.player)


# Clubs
class Club(models.Model):
    name = models.CharField(_('name'), max_length=200)

    def __unicode__(self):
        return self.name


class Sheet(models.Model):
    club = models.ForeignKey(Club, verbose_name=_('club'))
    name = models.CharField(_('name'), max_length=10)

    def __unicode__(self):
        return u'%s: %s' % (self.club, self.name)

    def generate_rocks(self, colours=[], numbers=[1, 2, 3, 4, 5, 6, 7, 8]):
        for c in colours:
            for n in numbers:
                Rock.objects.get_or_create(sheet=self, colour=c, number=n)

# Rocks


class Colour(models.Model):
    name = models.CharField(_('name'), max_length=100)
    hex = models.CharField(_('hex code'), max_length=6,
                           validators=[RegexValidator('^[0-9a-fA-F]{6}$', 'Not a valid hex code', 'Invalid Code')])

    def __unicode__(self):
        return u'%s: %s' % (self.name, self.hex)


class Rock(models.Model):
    sheet = models.ForeignKey(Sheet, verbose_name=_('sheet'))
    colour = models.ForeignKey(Colour, verbose_name=_('colour'))
    number = models.CharField(_('number'), max_length=1)

    def __unicode__(self):
        return u'%s: %s %s' % (self.sheet, self.colour.name, self.number)


# League
class League(models.Model):
    name = models.CharField(_('name'), max_length=100)
    teams = models.ManyToManyField(Team, verbose_name=_('team'), related_name='league')
    format = models.CharField(_('format'), max_length=10, choices=LEAGUE_FORMAT_CHOICES)

    def validate(self):
        for validator in league_formats[self.format]['team_validators']:
            for team in self.teams.all():
                validator(team)

    def __unicode__(self):
        return u'%s: %s' % (self.position, self.player)


# Games
class Game(models.Model):
    sheet = models.ForeignKey(Sheet, verbose_name=_('sheet'), related_name='game')
    team_a = models.ForeignKey(Team, verbose_name=_('team a'), related_name='game_a_team')
    team_b = models.ForeignKey(Team, verbose_name=_('team b'), related_name='game_b_team')
    team_a_colour = models.ForeignKey(Colour, verbose_name=_('team a colour'), related_name='game_a_colour')
    team_b_colour = models.ForeignKey(Colour, verbose_name=_('team b colour'), related_name='game_b_colour')
    start_time = models.DateTimeField(_('start time'))
    finish_time = models.DateTimeField(_('finish time'), blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.sheet, self.start_time)


class End(models.Model):
    game = models.ForeignKey(Game, verbose_name=_('game'), related_name='end')
    number = models.IntegerField(_('number'))
    start_time = models.DateTimeField(_('start time'), blank=True, null=True)
    finish_time = models.DateTimeField(_('finish time'), blank=True, null=True)
    scoring_team = models.ForeignKey(Team, verbose_name=_('scoring_team'), related_name='scoring_end')

    def __unicode__(self):
        return u'%s: %s' % (self.game, self.end)


class Throw(models.Model):
    end = models.ForeignKey(End, verbose_name=_('end'))
    number = models.IntegerField(_('number'),)
    rock = models.ForeignKey(Rock, verbose_name=_('rock'))
    player = models.ForeignKey(Player, verbose_name=_('player'))
    start_time = models.DateTimeField(_('start time'), blank=True, null=True)
    finish_time = models.DateTimeField(_('finish time'), blank=True, null=True)

    def __unicode__(self):
        return u'%s: %s' % (self.end, self.number)
