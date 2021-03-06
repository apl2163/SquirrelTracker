# st/urls.py
from django.urls import path,re_path
from . import views

app_name = 'st'
urlpatterns = [
    # ex: /st/map
    path('map', views.map, name='map'),
    # ex: /st/sightings
    path('sightings', views.index, name='index'),
    # ex: /st/sightings/add
    path('sightings/add',views.create.as_view(), name='create'),
    # ex: /st/sightings/stats
    path('sightings/stats',views.stats,name='stats'),
    # ex: /st/sightings/37F-PM-1014-03
    re_path(r'sightings/(?P<pk>[a-zA-Z0-9-]+)',views.update, name='update'),
]

