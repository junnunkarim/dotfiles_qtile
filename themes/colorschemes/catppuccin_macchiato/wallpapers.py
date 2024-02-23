import os
import random

home = os.path.expanduser("~")
prefix = home + "/.config/wallpaper/"

wallpapers = [
    prefix + "scenery_bridge_river_city.jpg",
    prefix + "pixelart_evening_trees_pole_wires_makrustic.png",
    prefix + "pixelart_night_stars_clouds_trees_cozy_PixelArtJourney_catppuccin.png",
    prefix + "pixelart_pokemon_rayquaza_forest_16x9.png",
    # prefix + "pixelart_france_house_police-car.jpg",
    prefix + "pixelart_seabeach_evening.png",
    prefix + "pixelart_sky_clouds_stars_moon_16x9.jpg",
]

wall = random.choice(wallpapers)
