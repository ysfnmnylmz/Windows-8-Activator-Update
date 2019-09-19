from denemee.apps.result.models import Matches

from django.contrib import admin


class MatchesAdmin(admin.ModelAdmin):
    list_display = ['date', 'hour', 'home_team', 'away_team', 'competition']
    list_display_links = ['hour', 'home_team', 'away_team']
    ordering = ['date', 'hour']
    list_filter = ['date']
    search_fields = ['home_team', 'away_team']

    class Meta:
        model = Matches


admin.site.register(Matches, MatchesAdmin)
