from django.shortcuts import render, get_object_or_404
import requests
from bs4 import BeautifulSoup as bs
from django.db.models import Q
from denemee.apps.matches.models import Matches
from denemee.apps.home.models import Leagues
from time import strftime, gmtime
from datetime import datetime, timedelta, date


def home(request):
    today = strftime("%Y-%m-%d", gmtime())
    matches = Matches.objects.filter(date=today)
    leagues = Leagues.objects.all()
    payload = {
        'matches': matches,
        'leagues': leagues
    }
    return render(request, 'index.html', payload)
