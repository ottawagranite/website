from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractPhoneNumber(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of phone number'), choices=settings.PHONE_NUMBER_TYPE_CHOICES)
    number = models.TextField(_('number'), help_text=_('The phone number'), max_length=100)

    def __unicode__(self):
        return u'%s %s' % (self.type, self.number)

    class Meta:
        abstract = True
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')


class AbstractEmailAddress(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of email address'), choices=settings.EMAIL_ADDRESS_TYPE_CHOICES)
    address = models.EmailField(_('address'), help_text=_('The email address'))

    def __unicode__(self):
        return u'%s %s' % (self.type, self.address)

    class Meta:
        abstract = True
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')


class AbstractAddress(models.Model):
    type = models.CharField(_('type'), help_text=_('The type of address'), choices=settings.ADDRESS_TYPE_CHOICES)
    street = models.CharField(_('street'))
    city = models.CharField(_('city'), help_text=_('City or Town'))
    province = models.CharField(_('province'), help_text=_('Province or State'))
    country = models.CharField(_('country'), default='Canada')
    postal_code = models.CharField(_('postal code'), help_text=_('Format: A1A 1A1'))

    def __unicode__(self):
        return u'%s %s %s' % (self.type, self.street, self.city)

    class Meta:
        abstract = True
        verbose_name = _('address')
        verbose_name_plural = _('addresses')


########################################
class Member(models.Model):
    salutation = models.CharField(_('salutation'), max_length=100, choices=settings.SALUTATION_CHOICES)
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    gender = models.CharField(_('gender'), max_length=100, choices=settings.GENDER_CHOICES)

    date_of_birth = models.DateField(_('date of birth'))
    comments = models.TextField(_('comments'), blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')


class Address(AbstractAddress):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='address')

    class Meta:
        verbose_name = _('address')
        verbose_name_plural = _('addresses')


class EmailAddress(AbstractEmailAddress):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='email')

    class Meta:
        verbose_name = _('email address')
        verbose_name_plural = _('email addresses')


class PhoneNumber(AbstractPhoneNumber):
    publish = models.BooleanField(_('publish'), default=False)
    member = models.ForeignKey(Member, verbose_name=_(''), related_name='phone_number')

    class Meta:
        verbose_name = _('phone number')
        verbose_name_plural = _('phone numbers')


class EmergencyContact(models.Model):
    member = models.ForeignKey(Member, verbose_name=_('member'), related_name='emergency_contact')
    name = models.TextField(_('name'))
    relationship = models.TextField(_('relationship'))

    class Meta:
        abstract = True
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
    member = models.ForeignKey(Member)
    type = models.ForeignKey(MembershipType)
    season = models.ForeignKey(Season)

    def __unicode__(self):
        return u'%s %s %s' % (self.member, self.type, self.season)

    class Meta:
        verbose_name = _('membership')
        verbose_name_plural = _('memberships')
