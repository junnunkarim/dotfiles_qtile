import importlib

from libqtile.config import Screen

from options import default_options, default_colorscheme
from .bar import top_bar
from core.helper import load_module

wallpaper_module_path = f"themes.colorschemes.{default_colorscheme}.wallpapers"
wall_mod = load_module(wallpaper_module_path)

wall = wall_mod.wall

screens = [
    Screen(top=top_bar, wallpaper=wall, wallpaper_mode="fill"),
]
