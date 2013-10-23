from django.db import models
from django.utils.translation import ugettext_lazy as _

from curling.models import League
from membership.models import Member


class OttawaGraniteMember(Member):
    membership_number = models.IntegerField(_('membership number'))
    latest_membership = models.IntegerField(_('latest_membership'))
    earliest_membership = models.IntegerField(_('earliest membership'))

    started_curling = models.IntegerField(_('started curling'))
    rookie_year = models.IntegerField(_('rookie year'))

    locker_number = models.IntegerField(_('locker number'))
    parking_stickers = models.IntegerField(_('parking stickers'))

    social = models.BooleanField(_('social'), default=False)
    honorary = models.BooleanField(_('honorary'), default=False)
    student = models.BooleanField(_('student'), default=False)

    instructor = models.CharField(_('instructor'), max_length=500)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')


class OttawaGraniteLeague(League):
    rating = models.CharField(_('rating'), max_length=20, blank=True)
