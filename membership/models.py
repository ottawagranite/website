from django.db import models
from django.utils.translation import ugettext_lazy as _
from membership import choices
from django.contrib.auth.models import User

class AbstractPhoneNumber(models.Model):
    type = models.CharField(_('type'), max_length=50, help_text=_('The type of phone number'), choices=choices.PHONE_NUMBER_TYPE_CHOICES)
    number = models.CharField(_('number'), max_length=200, help_text=_('The phone number'))

    def __unicode__(self):
        return u'%s %s' % (self.type, self.number)

    class Meta:
        abstract = True
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')

class AbstractEmailAddress(models.Model):
    type = models.CharField(_('type'), max_length=200, help_text=_('The type of email address'), choices=choices.EMAIL_ADDRESS_TYPE_CHOICES)
    address = models.EmailField(_('address'), max_length=200, help_text=_('The email address'))

    def __unicode__(self):
        return u'%s %s' % (self.type, self.address)

    class Meta:
        abstract = True
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')

class AbstractAddress(models.Model):
    type = models.CharField(_('type'), max_length=50, help_text=_('The type of address'), choices=choices.ADDRESS_TYPE_CHOICES)
    street = models.CharField(_('street'), max_length=200)
    city = models.CharField(_('city'), max_length=200, help_text=_('City or Town'))
    province = models.CharField(_('province'), max_length=200, help_text=_('Province or State'))
    country = models.CharField(_('country'), max_length=200, default='Canada')
    postal_code = models.CharField(_('postal code'), max_length=7, help_text=_('Format: A1A 1A1'))

    def __unicode__(self):
        return u'%s %s %s' % (self.type, self.street, self.city)

    class Meta:
        abstract = True
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

########################################
class Member(models.Model):
    user = models.OneToOneField(User)

    salutation = models.CharField(_('salutation'), max_length=100, choices=choices.SALUTATION_CHOICES, blank=True)
    gender = models.CharField(_('gender'), max_length=100, choices=choices.GENDER_CHOICES, blank=True)

    date_of_birth = models.DateField(_('date of birth'), blank=True)
    comments = models.TextField(_('comments'), blank=True)

    def __unicode__(self):
        return u'%s, %s' % (self.user.last_name, self.user.first_name)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

class Address(AbstractAddress):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='address')

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')

class EmailAddress(AbstractEmailAddress):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='email')

    class Meta:
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')

class PhoneNumber(AbstractPhoneNumber):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='phone_number')

    class Meta:
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')

class EmergencyContact(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='emergency_contact')
    name = models.TextField(_('name'))
    relationship = models.TextField(_('relationship'))

    class Meta:
        verbose_name = _('emergency contact')
        verbose_name_plural = _('emergency contacts')

class EmergencyContactPhoneNumber(AbstractPhoneNumber):
    emergency_contact = models.ForeignKey(EmergencyContact, verbose_name=_('emergency_contact'), related_name='phone_number')

    class Meta:
        verbose_name = _('emergency phone number')
        verbose_name_plural = _('emergency phone numbers')

########################################
class Season(models.Model):
    name = models.CharField(_('name'), max_length=100)
    start = models.DateField(_('start'))
    end = models.DateField(_('end'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('season')
        verbose_name_plural = _('seasons')

class MembershipType(models.Model):
    name = models.CharField(_('name'), max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('membership type')
        verbose_name_plural = _('membership types')

class Membership(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'))
    type = models.ForeignKey(MembershipType, verbose_name=_('type'))
    season = models.ForeignKey(Season, verbose_name=_('season'))

    def __unicode__(self):
        return u'%s %s %s' % (self.member, self.type, self.season)

    class Meta:
        verbose_name = _('membership')
        verbose_name_plural = _('memberships')

class Locker(models.Model):
    current_member = models.ForeignKey(Member)
    type = models.CharField(_('type'), max_length=200, choices=choices.LOCKER_TYPE_CHOICES)
    group = models.CharField(_('group'), max_length=200)
    number = models.CharField(_('number'), max_length=200)
