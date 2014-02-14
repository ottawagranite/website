from django.contrib import admin
from membership.models import Member, Address, EmailAddress, PhoneNumber, \
    EmergencyContact, EmergencyContactPhoneNumber, Season, Membership, Locker, \
    MembershipType, Position, Team, Division, League

admin.site.register(Member)
admin.site.register(Address)
admin.site.register(EmailAddress)
admin.site.register(PhoneNumber)
admin.site.register(EmergencyContact)
admin.site.register(EmergencyContactPhoneNumber)
admin.site.register(Season)
admin.site.register(Membership)
admin.site.register(MembershipType)
admin.site.register(Locker)
admin.site.register(Position)
admin.site.register(Team)
admin.site.register(Division)
admin.site.register(League)
