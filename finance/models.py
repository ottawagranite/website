from django.db import models
from django.utils.translation import ugettext_lazy as _

from finance.choices import CURRENCY_CHOICES, PAYMENT_TYPE
from django.conf import settings


class FeeType(models.Model):
    name = models.CharField(_('name'), max_length=100)
    currency = models.CharField(_('currenct'), max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(_('amount'), max_digits=7, decimal_places=2)


class Fee(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('staff'),
                              related_name='staff_fees')
    date = models.DateField(_('date'))
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=_('member'),
                               related_name='member_fees')
    type = models.ForeignKey(FeeType, verbose_name=_('type'))
    currency = models.CharField(_('currency'), max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(_('amount'), max_digits=7, decimal_places=2)
    reference = models.CharField(_('reference'), max_length=200, blank=True)
    note = models.TextField(_('note'), blank=True)


class Payment(models.Model):
    staff = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('staff'),
                              related_name="staff_payments")
    date = models.DateField(_('date'))
    fee = models.ForeignKey(Fee, verbose_name=_('fee'))
    member = models.ForeignKey(settings.AUTH_USER_MODEL,
                               verbose_name=_('member'),
                               related_name="member_payments")
    type = models.CharField(_('type'), max_length=200, choices=PAYMENT_TYPE)
    currency = models.CharField(_('currency'), max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(_('amount'), max_digits=7, decimal_places=2)
    reference = models.CharField(_('reference'), max_length=200, blank=True)
    note = models.TextField(_('note'), blank=True)
