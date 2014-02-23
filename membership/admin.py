from django.contrib import admin
from membership.models import ( Address, EmailAddress, PhoneNumber,
                                EmergencyContact, EmergencyContactPhoneNumber,
                                Season, Membership, Locker, MembershipType )

admin.site.register(Address)
admin.site.register(EmailAddress)
admin.site.register(PhoneNumber)
admin.site.register(EmergencyContact)
admin.site.register(EmergencyContactPhoneNumber)
admin.site.register(Season)
admin.site.register(Membership)
admin.site.register(MembershipType)
admin.site.register(Locker)
