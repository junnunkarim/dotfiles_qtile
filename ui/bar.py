from libqtile import bar

from core.helper import load_module
from options import default_bar_type, default_colorscheme, default_options

colorscheme_module_path = f"themes.colorschemes.{default_colorscheme}.colors"
colors = load_module(colorscheme_module_path)

widgets_module_path = f"widgets.{default_bar_type}.widgets"
w = load_module(widgets_module_path)
widget_list = (
    w.separator_small
    + w.app_launcher
    + w.separator_small
    + w.windowname
    + w.separator_auto
    + w.client_count
    + w.separator_small
    + w.groups
    + w.separator_small
    + w.layout_icon
    + w.separator_auto
    + w.widgetbox
    + w.separator_small
    + w.battery
    + w.separator_small
    + w.time
    + w.separator_small
    + w.date
    + w.tray
    + w.separator_small
)

gaps_size = default_options["gaps_size"]

top_bar = bar.Bar(
    widget_list,
    30,
    background=colors.bar_colors["bg"],
    # opacity=0.9,
    margin=[gaps_size, gaps_size, 0, gaps_size],  # [up, left, down, left]
    border_width=[5, 5, 5, 5],  # Draw top and bottom borders
    border_color=[
        colors.bar_colors["bg"],
        colors.bar_colors["bg"],
        colors.bar_colors["bg"],
        colors.bar_colors["bg"],
    ],  # Borders are magenta
)
