# 🎮 Pokemon Pokedex - Original 151

A retro Game Boy-styled web application built with Django that allows users to browse and explore the original 151 Pokemon with their stats, types, and more!

![Game Boy Style Pokedex](https://img.shields.io/badge/Style-Game%20Boy-9bbc0f?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Features

- Search Functionality - Search Pokemon by name or Pokedex number
- Type Badges - Color-coded type indicators (Fire, Water, Grass, etc.)
- Detailed Stats - View HP, Attack, Defense, Speed, and more with visual stat bars
- Pokemon Cries - Authentic Pokemon sound effects that play automatically
- Shiny Toggle - Switch between normal and shiny sprites on detail pages
- Navigation - Browse through Pokemon with Previous/Next buttons
- Retro Design - Authentic Game Boy green screen aesthetic with pixel font
- Lightning Fast - Database-backed for instant loading
- Team Builder - Add 6 Pokemon to your team, and check what types they are strong/weak against!

### Home Page - Pokemon Grid
*Grid view showing all 151 Pokemon with search functionality*

### Detail Page - Pokemon Stats
*Individual Pokemon page with stats, types, and shiny toggle*

## Getting Started

### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR_USERNAME/pokemon-pokedex.git
   cd pokemon-pokedex
```

2. **Create and activate virtual environment**
```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On Mac/Linux:
   source venv/bin/activate
```

3. **Install dependencies**
```bash
   pip install django requests
```

4. **Run migrations**
```bash
   python manage.py migrate
```

5. **Load Pokemon data from PokeAPI**
```bash
   python manage.py load_pokemon
```
   *This will fetch all 151 original Pokemon and their data. Takes about 30 seconds.*

6. **Run the development server**
```bash
   python manage.py runserver
```

7. **Visit the site**
   
   Open your browser to `http://127.0.0.1:8000/`

## Usage

### Browsing Pokemon
- Scroll through the grid of all 151 Pokemon
- Click any Pokemon to view detailed stats

### Searching
- Use the search bar to find Pokemon by name (e.g., "pika" finds Pikachu)
- Search by number (e.g., "25" finds Pikachu)
- Click "CLEAR" to reset search

### Detail Pages
- View comprehensive stats with visual bars
- Click "TOGGLE SHINY" to see shiny variants
- Use "PREVIOUS" and "NEXT" buttons to browse
- Pokemon cry plays automatically when page loads
- Click "PLAY CRY" button to replay the sound

## Tech Stack

- **Backend**: Django 5.1.5
- **Database**: SQLite
- **API**: [PokeAPI](https://pokeapi.co/)
- **Frontend**: HTML, CSS, JavaScript
- **Font**: Press Start 2P (Google Fonts)

## Project Structure
```
pokemon-pokedex/
├── pokemon_site/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── pokedex/              # Main app
│   ├── management/       # Custom management commands
│   │   └── commands/
│   │       └── load_pokemon.py
│   ├── templates/
│   │   └── pokedex/
│   │       ├── home.html
│   │       └── detail.html
│   ├── models.py         # Pokemon data model
│   ├── views.py          # View logic
│   ├── urls.py           # URL routing
│   ├── admin.py          # Admin interface
│   └── utils.py          # API utilities
└── manage.py
```

## Design Philosophy

This project recreates the nostalgic feel of the original Game Boy Pokemon games with:
- Classic Game Boy green color palette (#0f380f, #306230, #8bac0f, #9bbc0f)
- Pixel-perfect retro font (Press Start 2P)
- Scanline effects for authentic screen feel
- Pixelated sprite rendering
- Button press animations

## 🔧 Admin Panel

Access the Django admin panel to manage Pokemon data:

1. Create a superuser:
```bash
   python manage.py createsuperuser
```

2. Visit `http://127.0.0.1:8000/admin/`

3. Log in with your credentials

From the admin panel you can:
- Edit Pokemon stats, types, and images
- Search and filter Pokemon
- Add new Pokemon manually

## Known Issues

- Some older Pokemon may have missing or default sprites
- Shiny sprites for generation 1 Pokemon may differ from later games

##  License

This project is open source and available under the [MIT License](LICENSE).

##  Acknowledgments

- **PokeAPI** - For providing comprehensive Pokemon data
- **Nintendo/Game Freak** - For creating Pokemon
- **Press Start 2P Font** - Cody "CodeMan38" Boisclair

##  Contact

Your Name - [@tommyfeeley](https://twitter.com/tommyfeeley) - feeleytommy@gmail.com

Project Link: [https://github.com/tommyfeeley/pokemon-pokedex](https://github.com/tommyfeeley/pokedex/tree/main)
