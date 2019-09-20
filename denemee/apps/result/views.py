from django.shortcuts import render, get_object_or_404
from denemee.apps.result.models import Matches
from time import strftime
from datetime import datetime, timedelta


def yesterday(request):
    y_matches = Matches.objects.filter(date=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))
    payload = {
        'y_matches': y_matches
    }
    return render(request, 'yesterday.html', payload)
