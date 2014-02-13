from django.contrib import admin

from ottawagranite.models import OttawaGraniteMember


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member__last_name', 'member__first_name', 'member__gender', 'member__date_of_birth')
    list_filter = ('member__gender',)
    search_fields = ('member__first_name', 'member__last_name')
admin.site.register(OttawaGraniteMember, MemberAdmin)
