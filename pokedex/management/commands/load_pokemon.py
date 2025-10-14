from django.core.management.base import BaseCommand
from pokedex.models import Pokemon
from pokedex.utils import fetch_pokemon_data

class Command(BaseCommand):
    help = 'Loading all 151 Pokemon into database using PokeAPI'

    def handle(self, *args, **options): 
        self.stdout.write('Starting to load pokemon.')

        loaded = 0
        failed = 0

        for i in range(1,152):
            self.stdout.write(f'Fetching pokemon #{i}.')

            pokemon_data = fetch_pokemon_data(i)

            if pokemon_data:

                pokemon, created = Pokemon.objects.update_or_create(
                    pokedex_number=pokemon_data['id'],
                    defaults={
                        'name': pokemon_data['name'],
                        'height': pokemon_data['height'],
                        'weight': pokemon_data['weight'],
                        'image_url': pokemon_data['image'],
                        'shiny_image_url': pokemon_data.get('shiny_image', ''),
                        'type1': pokemon_data['type1'],
                        'type2': pokemon_data['type2'],
                        'hp': pokemon_data['stats'].get('hp', 0),
                        'attack': pokemon_data['stats'].get('attack',0),
                        'defense': pokemon_data['stats'].get('defense', 0),
                        'special_attack': pokemon_data['stats'].get('special-attack', 0),
                        'special_defense': pokemon_data['stats'].get('special-defense', 0),
                        'speed': pokemon_data['stats'].get('speed', 0),

                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created {pokemon.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Updated {pokemon.name}'))
                
                loaded += 1
            else:
                self.stdout.write(self.style.ERROR(f'Failed to fetch pokemon #{i}'))
                failed += 1
        self.stdout.write(self.style.SUCCESS(f'--COMPLETE--'))
        self.stdout.write(self.style.SUCCESS(f'Loaded: {loaded}'))
        self.stdout.write(self.style.ERROR(f'Failed: {failed}'))