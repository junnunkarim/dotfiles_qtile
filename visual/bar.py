import os

from libqtile import bar, widget
from libqtile.lazy import lazy

from core.utils import gaps_size
from .utils import raw_colors

color = raw_colors.gruvbox
home = os.path.expanduser('~')

top_bar = bar.Bar(
    [
        widget.TextBox(
            background=color["aqua0"],
        ),
        widget.TextBox(
            background=color["aqua0"],
            fmt="󰣇",
            font="Iosevka Nerd Font Mono",
            foreground=color["white0"],
            fontsize=40,
            mouse_callbacks={
                "Button1" : lazy.spawn([home + '/.bin/powermenu']),
            },
            padding=2,
        ),
        widget.TextBox(
            background=color["aqua0"],
        ),

        widget.WindowName(
            width=400,
            background=color["aqua2"],
            empty_group_string='╮(︶︿︶)╭  Nothing to See... ┬┴┬┴┤(･_├┬┴┬┴',
            fmt=" <i>{}</i>",
            foreground=color["black0"],
            max_chars=42,
            #padding=200,
        ),
        widget.TextBox(
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            fmt=" ",
            foreground=color["aqua2"],
            padding=-1,
        ),

        widget.Spacer(),

        widget.TextBox(
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["green2"],
            padding=-1,
        ),
        widget.CurrentLayoutIcon(
            background=color["green2"],
            scale=0.7,
        ),
        widget.TextBox(
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["green2"],
            padding=-1,
        ),

        widget.GroupBox(
            active=color["white"],
            background=color["black"],
            block_highlight_text_color=color["green2"],
            disable_drag=False,
            hide_unused=True,
            #highlight_color=[color["green0"], color["green2"]],
            highlight_method='block',
            margin_x=3,
            padding_x=10,
            #this_screen_border=color["green2"],
            this_current_screen_border=color["black"],
        ),

        widget.TextBox(
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["green2"],
            padding=-1,
        ),
        widget.WindowCount(
            background=color["green2"],
            fmt='╹{}╻',
            foreground=color["black"],
            show_zero=True,
            #fmt='>(O・O)->{}',
            #fmt='(っ˘̩╭╮˘̩)っ{}',
            #fmt='(っO~O)っ{}',
            #fmt='☆⌒(ゝ。∂){}',
            #fmt='ʕ•ᴥ•ʔ{}',
            #fmt='( ˘▽ ˘)っ♨{}',
        ),
        widget.TextBox(
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            fmt=" ",
            foreground=color["green2"],
            padding=-1,
        ),

        widget.Spacer(),

        widget.WidgetBox(
            close_button_location="right",
            fontsize=30,
            foreground=color["yellow2"],
            text_closed="", # 󰸳
            text_open="", # 󰸶
            widgets=[
                widget.TextBox(
                    fmt=" ",
                    font="Iosevka Nerd Font Mono",
                    fontsize=29,
                    foreground=color["red0"],
                    padding=-1,
                ),
                widget.TextBox(
                    background=color["red0"],
                    fmt='󰓃',
                    fontsize='26',
                    foreground=color["white0"],
                    mouse_callbacks={
                        "Button1" : lazy.spawn("pavucontrol"),
                    },
                ),
                widget.Volume(
                    background=color["red0"],
                    #emoji=True,
                    fmt="{} ",
                    mouse_callbacks={
                        "Button1" : lazy.spawn("pavucontrol"),
                    },
                ),

                widget.TextBox(
                    background=color["red1"],
                    fmt=' 󰃟',
                    fontsize='26',
                    foreground=color["white0"],
                ),
                widget.Backlight(
                    background=color["red1"],
                    #emoji=True,
                    backlight_name='intel_backlight',
                ),
                widget.TextBox(
                    fmt="",
                    font="Iosevka Nerd Font Mono",
                    fontsize=29,
                    foreground=color["red1"],
                    padding=-1,
                ),

                widget.TextBox(
                    fmt=" ",
                    font="Iosevka Nerd Font Mono",
                    fontsize=29,
                    foreground=color["yellow2"],
                    padding=-1,
                ),
                widget.TextBox(
                    background=color["yellow2"],
                    fmt='󰤥',
                    fontsize='26',
                    foreground=color["black0"],
                    mouse_callbacks={
                        "Button1" : lazy.spawn("networkmanager_dmenu"),
                    },
                ),
                widget.Wlan(
                    background=color["yellow2"],
                    foreground=color["black0"],
                    format='{essid}',
                    interface='wlp1s0',
                    mouse_callbacks={
                        "Button1" : lazy.spawn("networkmanager_dmenu"),
                    },
                ),
                widget.TextBox(
                    fmt=" ",
                    font="Iosevka Nerd Font Mono",
                    fontsize=29,
                    foreground=color["yellow2"],
                    padding=-1,
                ),
            ],
        ),

        widget.TextBox(
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["yellow1"],
            padding=-1,
        ),
        widget.Battery(
            background=color["yellow1"],
            charge_char='',
            discharge_char='󱟞',
            foreground=color["black0"],
            full_char='',
            format='{char} {percent:2.0%}',
            mouse_callbacks={
                "Button1" : lazy.spawn("xfce4-power-manager-settings"),
            },
        ),

        widget.TextBox(
            background=color["yellow1"],
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["yellow0"],
            padding=-1,
        ),
        widget.TextBox(
            background=color["yellow0"],
            fmt='',
            fontsize='26',
            foreground=color["white0"],
        ),
        widget.Clock(
            background=color["yellow0"],
            foreground=color["white0"],
            format="%I:%M %p"
        ),

        widget.TextBox(
            background=color["yellow0"],
            fmt=" ",
            font="Iosevka Nerd Font Mono",
            fontsize=29,
            foreground=color["blue1"],
            padding=-1,
        ),
        widget.TextBox(
            background=color["blue1"],
            fmt='',
            fontsize='26',
            foreground=color["white0"],
        ),
        widget.Clock(
            background=color["blue1"],
            format=" %a %d-%m-%Y ",
            foreground=color["white0"],
            mouse_callbacks={
                "Button1" : lazy.spawn(["alacritty", "-e", "calcure"]),
            },
        ),

        widget.Systray(
            background=color["blue0"],
            padding=10,
        ),
        widget.TextBox(
            background=color["blue0"],
        ),
        #widget.QuickExit(),
    ],
    35,
    background = color["black"],
    margin = [gaps_size, gaps_size, 0, gaps_size], # [up, left, down, left]
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
