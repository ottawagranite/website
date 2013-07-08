from django.conf import settings
from django.db import models


class PhoneNumber(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of phone number'), choices=settings.PHONE_NUMBER_TYPE_CHOICES)
    number = models.TextField(_('number'), help_text=_('The phone number'), max_length=100)

    class Meta:
        abstract = True
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')


class EmailAddress(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of email address'), choices=settings.EMAIL_ADDRESS_TYPE_CHOICES)
    address = models.EmailField(_('address'), help_text=_('The email address'),)

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
    membership_number = models.IntegerField()
    membership_year = models.IntegerField()
    number_of_parking_stickers = models.IntegerField()

    saluation = models.CharField(max_length=100, choices=settings.SALUTATION_CHOICES)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=settings.GENDER_CHOICES)

    date_of_birth = models.DateField()
    started_curling = models.IntegerField()
    rookie_year = models.IntegerField()

    locker_number = models.IntegerField()

    social = models.BooleanField(default=False)
    honourary = models.BooleanField(default=False)
    deceased = models.BooleanField(default=False)

    comments = models.TextField(blank=True)


class MemberAddress(Address):
    member = models.ForeignKey(Member, related_name='address')


class MemberEmailAddress(EmailAddress):
    member = models.ForeignKey(Member, related_name='email')


class MemberPhoneNumber(PhoneNumber):
    member = models.ForeignKey(Member, related_name='phone_number')

''' Unknown
Rating    Text    1
FIRSTYEARGCC    Text    4 DUP on membership_year?
BOARDMEM    Long Integer    4
INSTRUCTOR    Text    10
pres year    Text    12
OKBookEmail    Long Integer    4
OKBOOK    Long Integer    4
STUDENT    Long Integer    4
JUNIOR    Long Integer    4
BANTAM    Long Integer    4
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
RookiesEve    Long Integer    4
RookiesDay    Long Integer    4

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
    member = models.ForeignKey(Member)
    name = models.TextField()
    relationship = models.TextField()


class EmergencyContactPhoneNumber(PhoneNumber):
    emergency_contact = models.ForeignKey(EmergencyContact, related_name='phone_number')
