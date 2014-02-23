from django.contrib import admin
from ottawagranite.models import OttawaGraniteMember, OttawaGraniteLeague

class MemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'date_of_birth')
    list_filter = ('gender',)
    search_fields = ('last_name', 'first_name')

    def first_name(self, member):
        return member.user.first_name

    def last_name(self, member):
        return member.user.last_name

admin.site.register(OttawaGraniteMember, MemberAdmin)
admin.site.register(OttawaGraniteLeague)
