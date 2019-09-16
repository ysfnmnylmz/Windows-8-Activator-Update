from django.urls import path
from django.conf.urls import url
from .views import home

app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
]
