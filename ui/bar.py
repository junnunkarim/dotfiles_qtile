import importlib.util
import os

from libqtile import bar, widget
from libqtile.lazy import lazy

# import themes.colorschemes
from options import default_apps, default_colorscheme, default_options


# dynamically load colorschemes
def load_colorscheme_module():
    try:
        colorscheme_module = importlib.import_module(
            f"themes.colorschemes.{default_colorscheme}.colors"
        )
        return colorscheme_module
    except ImportError:
        print(f"Error: Could not import colorscheme module '{default_colorscheme}'")
        return None


colors = load_colorscheme_module()

# from themes.colorschemes.gruvbox.colors import (
#     app_launcher_colors,
#     bar_colors,
#     battery_colors,
#     date_colors,
#     groupbox_colors,
#     other_colors,
#     time_colors,
#     titlebar_colors,
#     tray_colors,
#     windowname_colors,
# )

home = os.path.expanduser("~")
gaps_size = default_options["gaps_size"]

top_bar = bar.Bar(
    [
        widget.Spacer(
            length=10,
        ),
        widget.TextBox(
            background=colors.app_launcher_colors["bg"],
            fmt="󰣇",
            font="Iosevka Nerd Font Mono",
            foreground=colors.app_launcher_colors["fg"],
            fontsize=40,
            mouse_callbacks={
                "Button1": lazy.spawn([home + "/.bin/rofi_run"]),
            },
            # margin=3,
            padding=10,
        ),
        widget.Spacer(
            length=10,
        ),
        widget.WindowName(
            width=500,
            background=colors.windowname_colors["bg"],
            # empty_group_string="╮(︶︿︶)╭  Nothing to See... ┬┴┬┴┤(･_├┬┴┬┴",
            fmt=" <i><b>{}</b></i>",
            fontsize=16,
            foreground=colors.windowname_colors["fg"],
            # max_chars=50,
            padding=10,
        ),
        # centers the groupbox
        widget.Spacer(),
        widget.WindowCount(
            background=colors.windowcount_colors["bg"],
            foreground=colors.windowcount_colors["fg"],
            fmt="╹ <b>{}</b> ╻",
            show_zero=True,
            padding=5,
            # fmt="(っO~O)っ {}",
            # fmt='>(O・O)->{}',
            # fmt='(っ˘̩╭╮˘̩)っ{}',
            # fmt='(っO~O)っ{}',
            # fmt='☆⌒(ゝ。∂){}',
            # fmt='ʕ•ᴥ•ʔ{}',
            # fmt='( ˘▽ ˘)っ♨{}',
        ),
        widget.Spacer(
            length=10,
        ),
        widget.GroupBox(
            active=colors.groupbox_colors["fg_occupied"],
            inactive=colors.groupbox_colors["fg"],
            background=colors.groupbox_colors["bg"],
            block_highlight_text_color=colors.groupbox_colors["bg"],
            this_current_screen_border=colors.groupbox_colors["fg_focus"],
            urgent_text=colors.groupbox_colors["fg_urgent"],
            urgent_border=colors.groupbox_colors["bg_urgent"],
            fontsize=25,
            padding=10,
            highlight_method="block",
            hide_unused=False,
            disable_drag=True,
            # highlight_color=[color["green0"], color["green2"]],
            # this_screen_border=color["green2"],
        ),
        widget.Spacer(
            length=10,
        ),
        widget.CurrentLayoutIcon(
            background=colors.layout_colors["bg"],
            scale=1.0,
        ),
        # centers the groupbox
        widget.Spacer(),
        widget.WidgetBox(
            close_button_location="right",
            fontsize=30,
            foreground=colors.widgetbox_colors["fg"],
            text_closed="",  # 󰸳
            text_open="",  # 󰸶
            # padding=10,
            widgets=[
                widget.TextBox(
                    background=colors.volume_colors["bg"],
                ),
                widget.TextBox(
                    background=colors.volume_colors["bg"],
                    foreground=colors.volume_colors["fg"],
                    fmt="󰓃",
                    fontsize="26",
                    mouse_callbacks={
                        "button1": lazy.spawn("pavucontrol"),
                    },
                    # padding=5,
                ),
                widget.Volume(
                    background=colors.volume_colors["bg"],
                    # emoji=true,
                    fmt="{}",
                    mouse_callbacks={
                        "button1": lazy.spawn("pavucontrol"),
                    },
                    padding=10,
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    background=colors.brightness_colors["bg"],
                ),
                widget.TextBox(
                    background=colors.brightness_colors["bg"],
                    fmt="󰃝",
                    fontsize="26",
                    foreground=colors.brightness_colors["fg"],
                    # padding=5,
                ),
                widget.Backlight(
                    background=colors.brightness_colors["bg"],
                    # emoji=true,
                    backlight_name="intel_backlight",
                    padding=10,
                ),
                widget.Spacer(
                    length=10,
                ),
                widget.TextBox(
                    background=colors.network_colors["bg"],
                ),
                widget.TextBox(
                    background=colors.network_colors["bg"],
                    fmt="󰤥",
                    fontsize="26",
                    foreground=colors.network_colors["fg"],
                    mouse_callbacks={
                        "button1": lazy.spawn("networkmanager_dmenu"),
                    },
                    # padding=5,
                ),
                widget.Wlan(
                    background=colors.network_colors["bg"],
                    foreground=colors.network_colors["fg"],
                    format="{essid}",
                    interface="wlp1s0",
                    mouse_callbacks={
                        "button1": lazy.spawn("networkmanager_dmenu"),
                    },
                    padding=10,
                ),
                widget.Spacer(
                    length=10,
                ),
            ],
        ),
        widget.Spacer(
            length=10,
        ),
        widget.TextBox(
            background=colors.battery_colors["bg_icon"],
        ),
        widget.TextBox(
            background=colors.battery_colors["bg_icon"],
            fmt="",
            fontsize="26",
            foreground=colors.battery_colors["fg_icon"],
            # padding=10,
        ),
        widget.TextBox(
            background=colors.battery_colors["bg_icon"],
        ),
        widget.Battery(
            background=colors.battery_colors["bg"],
            foreground=colors.battery_colors["fg"],
            # charge_char="󱐋",
            # discharge_char="-",
            # full_char="",
            # format="{char} {percent:2.0%}",
            format="{percent:2.0%}",
            fontsize="16",
            mouse_callbacks={
                "Button1": lazy.spawn("xfce4-power-manager-settings"),
            },
            padding=10,
        ),
        widget.Spacer(
            length=10,
        ),
        widget.TextBox(
            background=colors.time_colors["bg_icon"],
        ),
        widget.TextBox(
            background=colors.time_colors["bg_icon"],
            fmt="",
            fontsize="26",
            foreground=colors.time_colors["fg_icon"],
            # padding=10,
        ),
        widget.TextBox(
            background=colors.time_colors["bg_icon"],
        ),
        widget.Clock(
            background=colors.time_colors["bg"],
            foreground=colors.time_colors["fg"],
            font="Iosevka Nerd Font Mono",
            fontsize="16",
            format="%I:%M %p",
            padding=10,
        ),
        widget.Spacer(
            length=10,
        ),
        widget.TextBox(
            background=colors.date_colors["bg_icon"],
        ),
        widget.TextBox(
            background=colors.date_colors["bg_icon"],
            fmt="󰃶",
            fontsize="26",
            foreground=colors.date_colors["fg"],
            # padding=5,
        ),
        widget.TextBox(
            background=colors.date_colors["bg_icon"],
        ),
        widget.Clock(
            background=colors.date_colors["bg"],
            foreground=colors.date_colors["fg"],
            format="%a %d-%m-%Y ",
            fontsize="16",
            mouse_callbacks={
                "Button1": lazy.spawn(["alacritty", "-e", "calcure"]),
            },
            padding=10,
        ),
        # widget.Spacer(
        #     length=10,
        # ),
        widget.Systray(
            background=colors.tray_colors["bg"],
            padding=10,
        ),
        widget.Spacer(
            length=10,
        ),
        # widget.TextBox(
        #     background=color["blue0"],
        # ),
        # widget.QuickExit(),
    ],
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
