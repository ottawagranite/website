from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PhoneNumber(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of phone number'), choices=settings.PHONE_NUMBER_TYPE_CHOICES)
    number = models.TextField(_('number'), help_text=_('The phone number'), max_length=100)

    class Meta:
        abstract = True
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')


class EmailAddress(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of email address'), choices=settings.EMAIL_ADDRESS_TYPE_CHOICES)
    address = models.EmailField(_('address'), help_text=_('The email address'))

    class Meta:
        abstract = True
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')


class Address(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of address'), choices=settings.ADDRESS_TYPE_CHOICES)
    street = models.CharField(_('street'))
    city = models.CharField(_('city'), help_text=_('City or Town'))
    province = models.CharField(_('province'), help_text=_('Province or State'))
    country = models.CharField(_('country'), default='Canada')
    postal_code = models.CharField(_('postal code'), help_text=_('Format: A1A 1A1'))

    class Meta:
        abstract = True
        verbose_name = _('address')
        verbose_name_plural = _('addresses')


class Member(models.Model):
    membership_number = models.IntegerField(_('membership number'))
    latest_membership = models.IntegerField(_('latest_membership'))
    earliest_membership = models.IntegerField(_('earliest membership'))

    salutation = models.CharField(_('salutation'), max_length=100, choices=settings.SALUTATION_CHOICES)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    gender = models.CharField(_('gender'), max_length=100, choices=settings.GENDER_CHOICES)

    date_of_birth = models.DateField(_('date of birth'))
    started_curling = models.IntegerField(_('started curling'))
    rookie_year = models.IntegerField(_('rookie year'))

    locker_number = models.IntegerField(_('locker number'))
    parking_stickers = models.IntegerField(_('parking stickers'))

    social = models.BooleanField(_('social'), default=False)
    honorary = models.BooleanField(_('honorary'), default=False)
    student = models.BooleanField(_('student'), default=False)

    comments = models.TextField(_('comments'), blank=True)

    class Meta:
        abstract = True
        verbose_name = _('member')
        verbose_name_plural = _('members')


class MemberAddress(Address):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='address')


class MemberEmailAddress(EmailAddress):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='email')


class MemberPhoneNumber(PhoneNumber):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='phone_number')

''' Unknown
INSTRUCTOR    Text    10
'''

''' Mailing List
MAIL LIST    Long Integer    4
'''

''' Leagues
DAYTIME    Long Integer    4
DayMixTues    Long Integer    4
DayMixThur    Long Integer    4
EVEFIX    Long Integer    4
EVEDRAW    Long Integer    4
MONOPEN    Long Integer    4
WEDOPEN    Long Integer    4
SATOPEN    Long Integer    4
SUNOPEN    Long Integer    4
MIXED    Long Integer    4
LTLROCK    Long Integer    4
JUNIOR    Long Integer    4
BANTAM    Long Integer    4
RookiesEve    Long Integer    4
RookiesDay    Long Integer    4
'''

''' For Leagues
Rating    Text    1
'''

''' Payments and fees
InitFeeCharged    Integer    2
InitPaymentDate - 1    Date / Time    8
InitPaymentAmount - 1    Integer    2
InitPaymentDate - 2    Date / Time    8
InitPaymentAmount - 2    Integer    2
InitPaymentDate - 3    Date / Time    8
InitPaymentAmount - 3    Integer    2
InitPaymentDate - 4    Date / Time    8
InitPaymentAmount - 4    Integer    2
LateFeesOwed    Currency    8
OverrideFee    Currency    8
OverrideFeeIndicator    Text    1
OverrideFeeDescription    Text    250
OverrideFeeDate    Date / Time    8
'''


class EmergencyContact(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='emergency_contact')
    name = models.TextField(_('name'))
    relationship = models.TextField(_('relationship'))

    class Meta:
        abstract = True
        verbose_name = _('emergency contact')
        verbose_name_plural = _('emergency contacts')


class EmergencyContactPhoneNumber(PhoneNumber):
    emergency_contact = models.ForeignKey(EmergencyContact, verbose_name=_('emergency_contact'), related_name='phone_number')
