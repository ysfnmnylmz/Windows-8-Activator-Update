from django.contrib import admin
from .models import Teams, Players, Squads, Leagues, TeamCharacteristic, TeamPowerUp, PlayerPowerUp


class TeamsInlinePlayers(admin.StackedInline):
    model = Players
    fields = ['name']
    classes = ['collapse']


class LeaguesAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Leagues


class TeamsInlineSquad(admin.StackedInline):
    model = Squads
    fields = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'p11']
    classes = ['collapse']


class TeamsAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [TeamsInlineSquad, TeamsInlinePlayers]

    class Meta:
        model = Teams

    class Media:
        js = (
            'libs/jquery/dist/jquery.min.js',
            'libs/jquery-ui/jquery-ui.min.js',
            'js/TeamsAdmin.js',
        )


class PlayersAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'team']
    search_fields = ['name', 'position']
    list_filter = ['team', 'position']

    class Meta:
        model = Players


class SquadsAdmin(admin.ModelAdmin):
    list_display = ['team', 'week']
    search_fields = ['team', 'week']
    list_filter = ['team', 'week']

    class Meta:
        model = Squads


admin.site.register(Teams, TeamsAdmin)
admin.site.register(Players, PlayersAdmin)
admin.site.register(Squads, SquadsAdmin)
admin.site.register(Leagues, LeaguesAdmin)
admin.site.register(TeamPowerUp)
admin.site.register(TeamCharacteristic)
admin.site.register(PlayerPowerUp)
