import requests

def fetch_pokemon_data(pokemon_id):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}', timeout=5)
        if response.status_code == 200:
            data = response.json()

            types = [t['type']['name'] for t in data['types']]

            pokemon_info = {
                'id': data['id'],
                'name': data['name'],
                'height': data['height'],
                'weight': data['weight'],
                'image': data['sprites']['front_default'],
                'type1': types[0] if len(types) > 0 else '',
                'type2': types[1] if len(types) > 1 else '',
                'shiny_image': data['sprites']['front_shiny'],
                'stats': {

                }
            }

            for stat in data['stats']:
                stat_name = stat['stat']['name']
                stat_value = stat['base_stat']
                pokemon_info['stats'][stat_name] = stat_value
            return pokemon_info
        
    except requests.RequestException:
        pass
    return None