import importlib
import os

from libqtile.config import Screen

from options import default_apps, default_colorscheme, default_options

from .bar import top_bar


# dynamically load wallpapers
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


screens = [
    Screen(top=top_bar, wallpaper=wall_mod.wallpapers[0], wallpaper_mode="fill"),
]
