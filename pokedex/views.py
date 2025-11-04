from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Pokemon
from .type_chart import ALL_TYPES, TYPE_WEAKNESSES, TYPE_RESISTANCES, TYPE_CHART

def home_view(request):

    search_query = request.GET.get('search', '').strip()
    type_filter = request.GET.get('type', '').strip().lower()
    sort_by = request.GET.get('sort', '').strip()

    pokemon_queryset = Pokemon.objects.all()

    if type_filter:
        pokemon_queryset = pokemon_queryset.filter(Q(type1=type_filter) | Q(type2=type_filter))


    if search_query:
        if search_query.isdigit():
            pokemon_queryset = pokemon_queryset.filter(pokedex_number=int(search_query))
        else:
            pokemon_queryset = pokemon_queryset.filter(name__icontains=search_query)

    if sort_by:
        sort_mapping = {
            'name': 'name',
            '-name': '-name',
            'hp': 'hp',
            '-hp': '-hp',
            'speed': 'speed',
            '-speed': '-speed',
            'attack': 'attack',
            '-attack': '-attack',
            'defense': 'defense',
            '-defense': '-defense',
            'special_attack': 'special_attack',
            '-special_attack': '-special_attack',
            'special_defense':'special_defense',
            '-special_defense': '-special_defense',
        }

        if sort_by in sort_mapping:
            pokemon_queryset = pokemon_queryset.order_by(sort_mapping[sort_by])
    else:
        pokemon_queryset = pokemon_queryset.order_by('pokedex_number')

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
                'speed': pokemon.speed,
                'attack': pokemon.attack,
                'defense': pokemon.defense,
                'special_attack': pokemon.special_attack,
                'special_defense': pokemon.special_defense,
            }
        })

    context = {
        'page_title': 'Pokedex: Original 151!',
        'heading': 'Welcome to the Pokedex!',
        'pokemon_list': pokemon_list,
        'search_query': search_query,
        'type_filter': type_filter,
        'sort_by': sort_by,
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
            'abilities': pokemon_obj.abilities,
            'stats': {
                'hp': pokemon_obj.hp,
                'attack': pokemon_obj.attack,
                'defense': pokemon_obj.defense,
                'speed': pokemon_obj.speed,
                'special-attack': pokemon_obj.special_attack,
                'special-defense': pokemon_obj.special_defense,
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

def add_to_team(request, pokemon_id):
    if 'team' not in request.session:
        request.session['team'] = []
    team = request.session['team']

    if len(team) < 6 and pokemon_id not in team:
        team.append(pokemon_id)
        request.session['team'] = team
        request.session.modified = True

    return redirect('team_builder')

def remove_from_team(request, pokemon_id):
    if 'team' in request.session:
        team = request.session['team']
        if pokemon_id in team:
            team.remove(pokemon_id)
            request.session['team'] = team
            request.session.modified = True
    return redirect('team_builder')

def team_builder_view(request): 
    team_ids = request.session.get('team', [])
    team_pokemon = []
    team_types = []

    for pokemon_id in team_ids:
        try:
            pokemon = Pokemon.objects.get(pokedex_number=pokemon_id)
            team_pokemon.append({
                'id': pokemon.pokedex_number,
                'name': pokemon.name,
                'image': pokemon.image_url,
                'type1': pokemon.type1,
                'type2': pokemon.type2,
            })
            team_types.append(pokemon.type1)
            if pokemon.type2:
                team_types.append(pokemon.type2)
        except Pokemon.DoesNotExist:
            pass
    
    coverage = analyze_type_coverage(team_types)

    all_pokemon = []
    for pokemon in Pokemon.objects.all():
        all_pokemon.append({
                'id': pokemon.pokedex_number,
                'name': pokemon.name,
                'image': pokemon.image_url,
                'type1': pokemon.type1,
                'type2': pokemon.type2,
                'in_team': pokemon.pokedex_number in team_ids,
            })
        
    context = {
        'page_title': 'Team Builder', 
        'team_pokemon': team_pokemon,
        'team_size': len(team_pokemon),
        'all_pokemon': all_pokemon,
        'coverage': coverage
    }

    return render(request, 'pokedex/team_builder.html', context)

def analyze_type_coverage(team_types):

    offensive_coverage = {}
    defensive_weaknesses = {}
    defensive_resistances = {}

    for attack_type in ALL_TYPES:

        resist_count = 0
        weak_count = 0

        for team_type in set(team_types):
            if attack_type in TYPE_RESISTANCES.get(team_type, []):
                resist_count += 1
            if attack_type in TYPE_WEAKNESSES.get(team_type, []):
                weak_count += 1
        if weak_count > 0:
            defensive_weaknesses[attack_type] = weak_count
        if resist_count > 0:
            defensive_resistances[attack_type] = resist_count
    
    for team_type in set(team_types):
        super_effective_against = TYPE_CHART.get(team_type, {}).get('super_effective', [])
        for target_type in super_effective_against:
            offensive_coverage[target_type] = offensive_coverage.get(target_type, 0) + 1

    
    return {
        'offensive': offensive_coverage, 'weaknesses': defensive_weaknesses, 'resistances': defensive_resistances,
    }

