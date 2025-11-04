import requests

def fetch_ability_details(ability_name):
    try:
        ability_slug = ability_name.lower().replace(' ', '-')
        
        response = requests.get(f'https://pokeapi.co/api/v2/ability/{ability_slug}/', timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            for entry in data.get('effect_entries', []):
                if entry.get('language', {}).get('name') == 'en':
                    effect = entry.get('short_effect', '')
                    if effect:
                        return effect
            
            for entry in data.get('flavor_text_entries', []):
                if entry.get('language', {}).get('name') == 'en':
                    flavor = entry.get('flavor_text', '').replace('\n', ' ').replace('\f', ' ')
                    if flavor:
                        return flavor
        
        return "Description not available"
    except Exception as e:
        return "Description not available"

def fetch_pokemon_data(pokemon_id):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}', timeout=5)
        if response.status_code == 200:
            data = response.json()

            types = [t['type']['name'] for t in data['types']]

            ability_list = []

            for ability in data['abilities']:
                ability_name = ability['ability']['name']
                display_name = ability_name.replace('-', ' ').title()
                is_hidden = ability['is_hidden']

                description = fetch_ability_details(ability_name)

                ability_list.append({
                    'name': display_name, 'description': description, 'is_hidden': is_hidden
                })

            pokemon_info = {
                'id': data['id'],
                'name': data['name'],
                'height': data['height'],
                'weight': data['weight'],
                'image': data['sprites']['front_default'],
                'type1': types[0] if len(types) > 0 else '',
                'type2': types[1] if len(types) > 1 else '',
                'shiny_image': data['sprites']['front_shiny'],
                'abilities': ability_list,
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