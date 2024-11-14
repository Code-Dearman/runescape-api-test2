from django.urls import path
from . import views

urlpatterns = [
    path('player-stats/<str:player_name>/', views.get_runescape_data, name='player_stats'),
]