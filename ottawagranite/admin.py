from django.contrib import admin

from ottawagranite.models import OttawaGraniteMember, OttawaGraniteLeague


class MemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'gender', 'date_of_birth')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name')
admin.site.register(OttawaGraniteMember, MemberAdmin)
admin.site.register(OttawaGraniteLeague)