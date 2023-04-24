from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("v1/", views.v1, name="view 1"),
path("",views.home, name="home"),
path("summoner/", views.summoner, name="summoner"),
path("v1/<str:region>/<str:summonerName>", views.summonerName, name="summonerName"),




]