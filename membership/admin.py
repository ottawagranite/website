from django.contrib import admin
from membership.models import ( Address, AdditionalEmailAddress, PhoneNumber,
                                EmergencyContact, EmergencyContactPhoneNumber,
                                Season, Member, Membership, Locker, MembershipType )

admin.site.register(Address)
admin.site.register(AdditionalEmailAddress)
admin.site.register(PhoneNumber)
admin.site.register(EmergencyContact)
admin.site.register(EmergencyContactPhoneNumber)
admin.site.register(Season)
admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(MembershipType)
admin.site.register(Locker)
