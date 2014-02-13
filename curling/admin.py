from django.contrib import admin

from curling.models import Club, Sheet, Colour, Rock, Player, Team, League, Game, \
    End, Throw, TeamPlayer


# class AuthorAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Author, AuthorAdmin)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(TeamPlayer)

admin.site.register(Club)
admin.site.register(Sheet)
admin.site.register(Colour)
admin.site.register(Rock)


admin.site.register(League)
admin.site.register(Game)
admin.site.register(End)
admin.site.register(Throw)