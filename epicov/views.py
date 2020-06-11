from django.shortcuts import render
from epicov.models import Epicov
import datetime


def home(request):
    return render(request, 'epicov/home.html')


def team(request):
    return render(request, 'epicov/team.html')


def about(request):
    return render(request, 'epicov/about.html')


def project(request):
    return render(request, 'epicov/project.html')


def data(request):
    mapbox_access_token = 'pk.eyJ1IjoibmF2eWpvc2giLCJhIjoiY2s5ajNmaXBkMWc1czNnbzR6ZmN6MjAwaSJ9.b3pp4cYkRPLtkYZhkVqhoQ'
    # idx = [1, 1001, 5001, 6001, 7001]
    # q = Epicov.objects.filter(id__in=idx)
    q = Epicov.objects.exclude(lat=None)
    return render(request, 'epicov/data.html', {'mapbox_access_token': mapbox_access_token, 'q': q})

def map(request):
    mapbox_access_token = 'pk.eyJ1IjoibmF2eWpvc2giLCJhIjoiY2s5ajNmaXBkMWc1czNnbzR6ZmN6MjAwaSJ9.b3pp4cYkRPLtkYZhkVqhoQ'
    return render(request, 'epicov/map.html', {'mapbox_access_token': mapbox_access_token})
