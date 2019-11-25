from django.shortcuts import render, get_object_or_404
import requests
from bs4 import BeautifulSoup as bs
from django.db.models import Q
from denemee.apps.result.models import Matches
from time import strftime, gmtime
from datetime import datetime, timedelta


def home(request):
    matches = Matches.objects.all()
    payload = {
        'matches': matches
    }
    return render(request, 'index.html', payload)
