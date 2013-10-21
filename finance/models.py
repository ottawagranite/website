from django.contrib.auth.models import User
from django.db import models

from finance.choices import CURRENCY_CHOICES, PAYMENT_TYPE
from membership.models import Member


class FeeType(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(decimal_places=2)


class Fee(models.Model):
    staff = models.ForeignKey(User)
    date = models.DateField()
    member = models.ForeignKey(Member)
    type = models.ForeignKey(FeeType)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(decimal_places=2)
    reference = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)


class Payment(models.Model):
    staff = models.ForeignKey(User)
    date = models.DateField()
    fee = models.ForeignKey(Fee)
    member = models.ForeignKey(Member)
    type = models.CharField(max_length=200, choices=PAYMENT_TYPE)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)
    amount = models.DecimalField(decimal_places=2)
    reference = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)
