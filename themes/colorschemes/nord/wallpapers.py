import os
import random

home = os.path.expanduser("~")
prefix = home + "/.config/wallpaper/"

wallpapers = [
    prefix + "mist_forest_nord.jpg",
    prefix + "pixelart_night_train_cozy_gas_RoyalNaym_nord.png",
]

wall = random.choice(wallpapers)
