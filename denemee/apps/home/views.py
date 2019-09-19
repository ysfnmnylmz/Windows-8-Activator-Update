from django.shortcuts import render, get_object_or_404
from denemee.apps.result.models import Matches
from time import strftime
from datetime import datetime, timedelta


def home(request):
    matches = Matches.objects.filter(date=datetime.strftime(datetime.now(), '%Y-%m-%d'))
    payload = {
        'matches': matches
    }
    return render(request, 'index.html', payload)
