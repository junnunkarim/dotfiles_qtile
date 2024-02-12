from libqtile import widget
from libqtile.lazy import lazy

from core.helper import load_module
from custom.widgets import ExpandingClock
from options import default_colorscheme

colorscheme_module_path = f"themes.colorschemes.{default_colorscheme}.colors"
colors = load_module(colorscheme_module_path)


date_comp = {
    "sep1": widget.TextBox(
        background=colors.date_colors["bg_icon"],
    ),
    "icon": widget.TextBox(
        background=colors.date_colors["bg_icon"],
        fmt="󰃶",
        fontsize="26",
        foreground=colors.date_colors["fg"],
        # padding=5,
    ),
    "sep2": widget.TextBox(
        background=colors.date_colors["bg_icon"],
    ),
    "value": ExpandingClock(
        background=colors.date_colors["bg"],
        foreground=colors.date_colors["fg"],
        format="%a %d-%m-%Y",
        fontsize="16",
        # mouse_callbacks={
        #     "Button1": lazy.spawn(["alacritty", "-e", "calcure"]),
        # },
        padding=10,
    ),
}

date = [
    date_comp["sep1"],
    date_comp["icon"],
    date_comp["sep2"],
    date_comp["value"],
]
