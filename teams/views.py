from django.shortcuts import render
from django.http import HttpResponse
from .models import Team


def index(request):
    teams = Team.objects.all()
    return render(request, 'homepage_index.html', {'teams': teams})
