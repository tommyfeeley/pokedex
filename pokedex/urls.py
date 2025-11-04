from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail_view, name='pokemon_detail'),
    path('team/', views.team_builder_view, name='team_builder'),
    path('team/add/<int:pokemon_id>/', views.add_to_team, name='add_to_team'),
    path('team/remove/<int:pokemon_id>/', views.remove_from_team, name='remove_from_team'),
]