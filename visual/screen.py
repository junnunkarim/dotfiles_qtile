import os

from libqtile.config import Screen

from .bar import top_bar

home = os.path.expanduser('~')
wallpaper_image= home + '/.config/wallpaper/pixelart_night_train_cozy_gas_nord_RoyalNaym.png'

screens = [
    Screen(
        top=top_bar,
        wallpaper=wallpaper_image,
        wallpaper_mode="fill"
    ),
]
