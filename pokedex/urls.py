from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pokemon/<int:pokemon_id>/', views.pokemon_detail_view, name='pokemon_detail'),
]