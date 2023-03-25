from . import views
from django.urls import path


urlpatterns = [
    path('arizona-diamondbacks', views.arizona)
]
