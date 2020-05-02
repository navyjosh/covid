from django.urls import path
from .views import home, about, project, data, map

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('project/', project, name='project'),
    path('data/', data, name='data'),
    path('map/', map, name='map')
]
