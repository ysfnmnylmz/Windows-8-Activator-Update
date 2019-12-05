from django.contrib import admin
from .models import Matches


class MatchesAdmin(admin.ModelAdmin):
    list_display = ['date', 'hour', 'h_team', 'a_team']
    search_fields = ['h_team', 'a_team']
    ordering = ['-date']

    class Meta:
        model = Matches


admin.site.register(Matches, MatchesAdmin)
