from django.shortcuts import render, get_object_or_404
from .models import Matches
from denemee.apps.home.models import Teams, TeamPowerUp, TeamCharacteristic
from django.core import serializers


def matches_details(request, page_id=None, team=None, **kwargs):
    matches_details = get_object_or_404(Matches, id=page_id)
    home_team_up = get_object_or_404(TeamPowerUp, team=matches_details.h_team)
    home_team_chr = get_object_or_404(TeamCharacteristic, team=matches_details.h_team)
    away_team_up = get_object_or_404(TeamPowerUp, team=matches_details.a_team)
    away_team_chr = get_object_or_404(TeamCharacteristic, team=matches_details.a_team)
    home_team_chr_data = serializers.serialize("python", TeamCharacteristic.objects.filter(team=matches_details.h_team))
    away_team_chr_data = serializers.serialize("python", TeamCharacteristic.objects.filter(team=matches_details.a_team))
    payload = {
        'matches_details': matches_details,
        'home_team_up': home_team_up,
        'home_team_chr': home_team_chr,
        'away_team_up': away_team_up,
        'away_team_chr': away_team_chr,
        'home_team_chr_data': home_team_chr_data,
        'away_team_chr_data': away_team_chr_data,
    }
    return render(request, 'match_detail.html', payload)
