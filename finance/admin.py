from django.contrib import admin

from finance.models import FeeType, Fee, Payment


admin.site.register(FeeType)
admin.site.register(Fee)
admin.site.register(Payment)
