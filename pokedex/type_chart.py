TYPE_CHART = {
    'normal': {
        'super_effective': [],
        'not_very_effective': ['rock', 'steel'],
        'no_effect': ['ghost']
    },
    'fire': {
        'super_effective': ['grass', 'steel', 'bug', 'ice'],
        'not_very_effective': ['rock', 'water', 'fire', 'dragon'],
        'no_effect': []
    },
    'water': {
        'super_effective': ['fire', 'ground', 'rock'],
        'not_very_effective': ['water', 'grass', 'dragon'],
        'no_effect': []
    },
    'grass': {
        'super_effective': ['water', 'ground', 'rock'],
        'not_very_effective': ['fire', 'grass', 'poison', 'flying', 'bug', 'dragon', 'steel'],
        'no_effect': []
    },
    'electric': {
        'super_effective': ['water', 'flying'],
        'not_very_effective': ['electric', 'grass', 'dragon'],
        'no_effect': ['ground']
    },
    'fighting': {
        'super_effective': ['normal', 'ice', 'rock', 'dark', 'steel'],
        'not_very_effective': ['poison', 'flying', 'psychic', 'bug', 'fairy'],
        'no_effect': ['ghost']
    },
    'psychic': {
        'super_effective': ['fighting', 'poison'],
        'not_very_effective': ['psychic', 'steel'],
        'no_effect': ['dark']
    },
    'bug': {
        'super_effective': ['grass', 'psychic', 'dark'],
        'not_very_effective': ['fire', 'fighting', 'poison', 'flying', 'ghost', 'steel', 'fairy'],
        'no_effect': []
    },
    'ice': {
        'super_effective': ['dragon', 'flying', 'grass', 'ground'],
        'not_very_effective': ['fire', 'water', 'ice', 'steel'],
        'no_effect': []
    },
    'ground': {
        'super_effective': ['fire', 'electric', 'poison', 'rock', 'steel'],
        'not_very_effective': ['grass', 'bug'],
        'no_effect': ['flying']
    },
    'rock': {
        'super_effective': ['fire', 'ice', 'flying', 'bug'],
        'not_very_effective': ['ground', 'steel', 'fighting'],
        'no_effect': []
    },
    'poison': {
        'super_effective': ['grass', 'fairy'],
        'not_very_effective': ['rock', 'ghost', 'ground', 'poison'],
        'no_effect': ['steel']
    },
    'ghost': {
        'super_effective': ['psychic', 'ghost'],
        'not_very_effective': ['dark'],
        'no_effect': ['normal']
    },
    'flying': {
        'super_effective': ['grass', 'fighting', 'bug'],
        'not_very_effective': ['rock', 'steel', 'electric'],
        'no_effect': []
    },
    'dragon': {
        'super_effective': ['dragon'],
        'not_very_effective': [ 'steel'],
        'no_effect': ['fairy']
    },
    'dark': {
        'super_effective': ['psychic', 'ghost'],
        'not_very_effective': ['fighting', 'dark', 'fairy'],
        'no_effect': []
    },
    'steel': {
        'super_effective': ['ice', 'rock', 'fairy'],
        'not_very_effective': ['fire', 'steel', 'water', 'electric'],
        'no_effect': []
    },
    'fairy': {
        'super_effective': ['fighting', 'dragon', 'dark'],
        'not_very_effective': ['fire', 'steel', 'poison'],
        'no_effect': []
    }
}

TYPE_RESISTANCES = {
    'normal': [],
    'fire': ['fire', 'grass', 'ice', 'bug', 'steel', 'fairy'],
    'water': ['fire', 'water', 'ice', 'steel'],
    'grass': ['electric', 'flying', 'steel'],
    'electric': ['electric', 'flying', 'steel'],
    'ice': ['ice'],
    'fighting': ['bug', 'rock', 'dark'],
    'poison': ['grass', 'fighting', 'poison', 'bug', 'fairy'],
    'ground': ['poison', 'rock'],
    'flying': ['grass', 'fighting', 'bug'],
    'psychic': ['fighting', 'psychic'],
    'bug': ['grass', 'fighting', 'ground'],
    'rock': ['normal', 'fire', 'poison', 'flying'],
    'ghost': ['poison', 'bug'],
    'dragon': ['fire', 'water', 'electric', 'grass'],
    'dark': ['ghost', 'dark'],
    'steel': ['normal', 'grass', 'ice', 'flying','psychic', 'bug', 'rock', 'dragon', 'steel', 'fairy'],
    'fairy': ['fighting', 'bug', 'dark']
}

TYPE_WEAKNESSES = {
    'normal': ['fighting'],
    'fire': ['water', 'ground', 'rock'],
    'water': ['electric', 'grass'],
    'grass': ['fire', 'ice', 'poison', 'flying', 'bug'],
    'electric': ['ground'],
    'ice': ['fire', 'fighting', 'rock', 'steel'],
    'fighting': ['flying', 'psychic', 'fairy'],
    'poison': ['ground', 'psychic'],
    'ground': ['water', 'grass', 'ice'],
    'flying': ['electric', 'ice', 'rock'],
    'psychic': ['bug', 'ghost', 'dark'],
    'bug': ['fire', 'flying', 'rock'],
    'rock': ['water', 'ground', 'grass', 'fighting', 'steel'],
    'ghost': ['ghost', 'dark'],
    'dragon': ['ice', 'dragon', 'fairy'],
    'dark': ['fighting', 'bug', 'fairy'],
    'steel': ['fire', 'fighting', 'ground'],
    'fairy': ['poison', 'steel']
}

ALL_TYPES = [
    'normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting',
    'poison', 'ground', 'rock', 'steel', 'fairy', 'dark', 'ghost',
    'dragon', 'flying', 'bug', 'psychic'
]