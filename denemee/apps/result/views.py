from django.shortcuts import render, get_object_or_404
from denemee.apps.result.models import Matches
from time import strftime
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from datetime import datetime, timedelta


def yesterday(request):
    y_matches = Matches.objects.filter(date=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))
    payload = {
        'y_matches': y_matches
    }
    return render(request, 'yesterday.html', payload)


class SearchMatch(ListView):
    model = Matches
    template_name = 'match_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        for term in query.split():
            object_list = Matches.objects.filter(
                Q(home_team__icontains=term) | Q(away_score__contains=term)
            )
            return object_list