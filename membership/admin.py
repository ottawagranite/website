from django.contrib import admin
from membership.models import Member, Position, Team, Division, League

class MemberAdmin(admin.ModelAdmin):
    pass

class PositionAdmin(admin.ModelAdmin):
    pass

class TeamAdmin(admin.ModelAdmin):
    pass

class DivisionAdmin(admin.ModelAdmin):
    pass

class LeagueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Member, MemberAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(League, LeagueAdmin)
