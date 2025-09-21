from django.urls import path
from django.conf.urls import url
from .views import matches_details

app_name = 'matches'

urlpatterns = [
    url(r'(?P<page_id>\d+)-(?P<page_slug>[\w-]+)', matches_details, name='matches_details'),
]
