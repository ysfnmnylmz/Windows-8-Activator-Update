from django.shortcuts import render, get_object_or_404
from denemee.apps.result.models import Matches


def home(request):
    matches = Matches.objects.all()
    payload = {
        'matches': matches
    }
    return render(request, 'index.html', payload)
