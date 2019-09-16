from django.contrib import admin
from denemee.apps.result.models import Matches


class MatchesAdmin(admin.ModelAdmin):
    list_display = ['date', 'score', 'fh_score', 'hour', 'home_team', 'away_team', 'ms_tahmin', 'iy_tahmin', 'tahmin45',
                    'tahmin35', 'tahmin25', 'tahmin15', 'tahmin05', 'tahmin_iy25', 'tahmin_iy15', 'tahmin_iy05',
                    'tahmin_kg']
    list_display_links = ['hour', 'home_team', 'away_team', 'ms_tahmin', 'iy_tahmin']
    ordering = ['hour']
    list_filter = ['hour']
    search_fields = ['home_team', 'away_team']

    class Meta:
        model = Matches


admin.site.register(Matches, MatchesAdmin)
# Register your models here.
