import os

from libqtile.config import Screen

from .bar import top_bar

home = os.path.expanduser('~')
wallpaper_image= home + '/.config/wallpaper/pixelart_house_chibi_person_game_jmw327.png'

screens = [
    Screen(
        top=top_bar,
        wallpaper=wallpaper_image,
        wallpaper_mode="fill"
    ),
]
