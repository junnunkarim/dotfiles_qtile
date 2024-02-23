import os
import random

# Set the seed value
# seed_value = 41
# random.seed(seed_value)

home = os.path.expanduser("~")
prefix = home + "/.config/wallpaper/"

wallpapers = [
    prefix + "pixelart_pokemon_rayquaza_forest_16x9.png",
    prefix + "pixelart_night_stars_clouds_trees_cozy_PixelArtJourney.png",
    prefix + "pixelart_night_stars_shooting-star_river_boat_couple_relaxing.png",
    prefix + "scenery_bridge_river_city.jpg",
    prefix + "pixelart_evening_trees_pole_wires_makrustic.png",
    prefix + "afternoon_light_philip_straub.jpg",
    prefix + "anime_Sunset.jpg",
    prefix + "mist_forest_nord.jpg",
    prefix + "pixelart_mountains_forest_grassland_dreamlike_star_night.jpg",
    prefix + "pixelart_night_cozy_fireflies_stars_dog.png",
    prefix + "pixelart_thron_dark_someone.png",
    prefix + "forest_stairs.jpg",
    prefix + "floating_flower.jpg",
    prefix + "forest_hut.jpg",
    prefix + "home_at_the_end_of_the_world.jpg",
    prefix + "pixelart_dock-no4_house_destroyed_warm-color.png",
]

wall = random.choice(wallpapers)
# wall = wallpapers[0]
