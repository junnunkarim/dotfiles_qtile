import importlib
import random

from libqtile.config import Screen

from options import default_colorscheme

from .bar import top_bar


# dynamic module loading
def load_wallpapers_module():
    try:
        wallpapers_module = importlib.import_module(
            f"themes.colorschemes.{default_colorscheme}.wallpapers"
        )
        return wallpapers_module
    except ImportError:
        print(f"Error: Could not import colorscheme module '{default_colorscheme}'")
        return None


wall_mod = load_wallpapers_module()
wall = random.choice(wall_mod.wallpapers)


screens = [
    Screen(top=top_bar, wallpaper=wall, wallpaper_mode="fill"),
]
