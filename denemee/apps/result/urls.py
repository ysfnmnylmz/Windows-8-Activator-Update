from django.urls import path
from django.conf.urls import url
from denemee.apps.result.views import yesterday

app_name = 'result'

urlpatterns = [
    path('', yesterday, name='yesterday'),
]
