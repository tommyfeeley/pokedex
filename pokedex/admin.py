from django.contrib import admin
from .models import Pokemon
# Register your models here.

@admin.register(Pokemon)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('pokedex_number', 'name', 'type1', 'type2', 'hp', 'attack', 'defense')
    list_filter = ('type1', 'type2')
    search_fields = ('name', 'pokedex_number')
    ordering = ('pokedex_number',)

    fieldsets = (
        ('Basic info', {
            'fields': ('pokedex_number', 'name', 'image_url')
        }),
        ('Physical info', {
            'fields': ('height', 'weight')
        }),
        ('Types', {
            'fields': ('type1', 'type2')
        }),
        ('Stats', {
            'fields': ('hp', 'attack', 'defense', 'special_attack', 'special_defense', 'speed')
        }),

    )