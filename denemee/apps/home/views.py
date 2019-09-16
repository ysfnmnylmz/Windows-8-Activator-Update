from django.shortcuts import render, get_object_or_404


def home(request):
    payload = {

    }
    return render(request, 'index.html', payload)
