from django.db import models

# Create your models here.

class Member(models.Model):
    """This class represents a club member."""
    active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
