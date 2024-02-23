import os
import random

home = os.path.expanduser("~")
prefix = home + "/.config/wallpaper/"

wallpapers = [
    prefix + "pixelart_pokemon_rayquaza_forest_16x9.png",
    prefix + "pixelart_night_stars_clouds_trees_cozy_PixelArtJourney.png",
    prefix + "pixelart_evening_trees_pole_wires_makrustic.png",
]

wall = random.choice(wallpapers)
