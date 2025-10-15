from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Pokemon

def home_view(request):

    search_query = request.GET.get('search', '').strip()
    type_filter = request.GET.get('type', '').strip().lower()

    pokemon_queryset = Pokemon.objects.all()

    if type_filter:
        pokemon_queryset = pokemon_queryset.filter(Q(type1=type_filter) | Q(type2=type_filter))


    if search_query:
        if search_query.isdigit():
            pokemon_queryset = pokemon_queryset.filter(pokedex_number=int(search_query))
        else:
            pokemon_queryset = pokemon_queryset.filter(name__icontains=search_query)

    pokemon_list = []

    for pokemon in pokemon_queryset:
        pokemon_list.append({
            'id': pokemon.pokedex_number,
            'name': pokemon.name,
            'image': pokemon.image_url,
            'type1': pokemon.type1,
            'type2': pokemon.type2,
            'stats': {
                'hp': pokemon.hp,
            }
        })

    context = {
        'page_title': 'Pokedex: Original 151!',
        'heading': 'Welcome to the Pokedex!',
        'pokemon_list': pokemon_list,
        'search_query': search_query,
        'type_filter': type_filter,
    }

    return render(request, 'pokedex/home.html', context)

def pokemon_detail_view(request, pokemon_id):

    pokemon_obj = get_object_or_404(Pokemon, pokedex_number=pokemon_id)

    pokemon = {
        'id': pokemon_obj.pokedex_number,
            'name': pokemon_obj.name,
            'image': pokemon_obj.image_url,
            'shiny_image': pokemon_obj.shiny_image_url,
            'height': pokemon_obj.height,
            'weight': pokemon_obj.weight,
            'type1': pokemon_obj.type1,
            'type2': pokemon_obj.type2,
            'stats': {
                'hp': pokemon_obj.hp,
                'attack': pokemon_obj.attack,
                'defense': pokemon_obj.defense,
                'speed': pokemon_obj.speed,
                'special-attack': pokemon_obj.special_attack,
                'special_defense': pokemon_obj.special_defense,
            }
    }
    prev_pokemon = None
    next_pokemon = None

    if pokemon_id > 1:
        prev_pokemon = pokemon_id - 1

    if pokemon_id < 151:
        next_pokemon = pokemon_id + 1

    context = {
        'page_title': f'#{pokemon_id} — {pokemon_obj.name.title()}',
        'pokemon': pokemon,
        'pokemon_id': pokemon_id,
        'prev_pokemon':prev_pokemon,
        'next_pokemon': next_pokemon,
    }

    return render(request, 'pokedex/detail.html', context)