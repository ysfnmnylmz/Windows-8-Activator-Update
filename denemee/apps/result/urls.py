from django.urls import path
from django.conf.urls import url
from denemee.apps.result.views import yesterday, SearchMatch

app_name = 'result'

urlpatterns = [
    path('', yesterday, name='yesterday'),
    path('search/', SearchMatch.as_view(), name='search_result'),
]
