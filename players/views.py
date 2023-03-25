from django.shortcuts import render
# from django.http import HttpResponse
from .models import Arizona_Diamondback


def arizona(request):
    arizona_diamondbacks = Arizona_Diamondback.objects.all()
    return render(request, 'Arizona_Diamondbacks_index.html', {'arizona_diamondbacks': arizona_diamondbacks})

