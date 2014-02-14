from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=512)
    rep = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Division(models.Model):
    name = models.CharField(max_length=512)
    league = models.ForeignKey(League)

    def __str__(self):
        return "%s of %s" % (self.name, self.league.name)

class Team(models.Model):
    name = models.CharField(max_length=512)
    division = models.ForeignKey(Division)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=512)
    team = models.ForeignKey(Team)

    def __str__(self):
        return "%s of Team %s in League %s" % (self.name,
                                               self.team.name,
                                               self.team.division.league.name)

class Member(models.Model):
    """This class represents a club member."""
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    positions = models.ForeignKey(Position, null=True, blank=True)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)
