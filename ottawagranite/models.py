from django.db import models
from django.utils.translation import ugettext_lazy as _

from curling.models import League
from membership.models import Member


class OttawaGraniteMember(Member):
    """A class implementing the Member interface, with fields specific to the
    Granite Curling Club of West Ottawa."""
    membership_number = models.IntegerField(_('membership number'),
        unique=True,
        help_text=_("An artibrary number assigned to a member for unique identification."))
    latest_membership = models.IntegerField(_('latest_membership'),
        help_text=_("FIXME: I don't know what this is for."))
    earliest_membership = models.IntegerField(_('earliest membership'),
        help_text=_("FIXME: I don't know what this is for."))

    started_curling = models.IntegerField(_('started curling'),
        help_text=_("FIXME: I don't know what this is for."))
    rookie_year = models.IntegerField(_('rookie year'),
        help_text=_("The year you started curling."))

    locker_number = models.IntegerField(_('locker number'),
        help_text=_("Your locker number, if you have one."))
    parking_stickers = models.IntegerField(_('parking stickers'),
        help_text=_("The number of parking stickers you have been issued."))

    social = models.BooleanField(_('social'),
        default=False,
        help_text=_("This is a social membership, without any actual curling."))
    # FIXME: Should this be "honourary"?
    honorary = models.BooleanField(_('honorary'),
        default=False,
        help_text=_("An honorary member."))
    student = models.BooleanField(_('student'),
        default=False,
        help_text=_("A student membership."))

    instructor = models.CharField(_('instructor'),
        max_length=500,
        blank=True,
        help_text=_("Your initial instructor in curling, if any."))

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

class OttawaGraniteLeague(League):
    rating = models.CharField(_('rating'), max_length=20, blank=True)
