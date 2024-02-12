import os

from libqtile import widget
from libqtile.lazy import lazy

from core.helper import load_module
from options import default_colorscheme, default_font

colorscheme_module_path = f"themes.colorschemes.{default_colorscheme}.colors"
colors = load_module(colorscheme_module_path)

home = os.path.expanduser("~")


# widget components
# -----------------

app_launcher_comp = widget.TextBox(
    background=colors.app_launcher_colors["bg"],
    fmt="󰣇",
    font=default_font,
    foreground=colors.app_launcher_colors["fg"],
    fontsize=40,
    mouse_callbacks={
        "Button1": lazy.spawn([home + "/.bin/rofi_run"]),
    },
    # margin=3,
    padding=10,
)

windowname_comp = widget.WindowName(
    width=500,
    background=colors.windowname_colors["bg"],
    # empty_group_string="╮(︶︿︶)╭  Nothing to See... ┬┴┬┴┤(･_├┬┴┬┴",
    fmt=" <i><b>{}</b></i>",
    fontsize=16,
    foreground=colors.windowname_colors["fg"],
    # max_chars=50,
    padding=10,
)


groups_comp = widget.GroupBox(
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
)

client_count_comp = widget.WindowCount(
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
)

layout_icon_comp = widget.CurrentLayoutIcon(
    background=colors.layout_colors["bg"],
    scale=1.0,
)

battery_comp = {
    "sep1": widget.TextBox(
        background=colors.battery_colors["bg_icon"],
    ),
    "icon": widget.TextBox(
        background=colors.battery_colors["bg_icon"],
        fmt="",
        fontsize="26",
        foreground=colors.battery_colors["fg_icon"],
        # padding=10,
    ),
    "sep2": widget.TextBox(
        background=colors.battery_colors["bg_icon"],
    ),
    "value": widget.Battery(
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
}

time_comp = {
    "sep1": widget.TextBox(
        background=colors.time_colors["bg_icon"],
    ),
    "icon": widget.TextBox(
        background=colors.time_colors["bg_icon"],
        fmt="",
        fontsize="26",
        foreground=colors.time_colors["fg_icon"],
        # padding=10,
    ),
    "sep2": widget.TextBox(
        background=colors.time_colors["bg_icon"],
    ),
    "value": widget.Clock(
        background=colors.time_colors["bg"],
        foreground=colors.time_colors["fg"],
        font=default_font,
        fontsize="16",
        format="%I:%M %p",
        padding=10,
    ),
}

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
    "value": widget.Clock(
        background=colors.date_colors["bg"],
        foreground=colors.date_colors["fg"],
        format="%a %d-%m-%Y ",
        fontsize="16",
        mouse_callbacks={
            "Button1": lazy.spawn(["alacritty", "-e", "calcure"]),
        },
        padding=10,
    ),
}

volume_comp = {
    "sep1": widget.TextBox(
        background=colors.volume_colors["bg"],
    ),
    "icon": widget.TextBox(
        background=colors.volume_colors["bg"],
        foreground=colors.volume_colors["fg"],
        fmt="󰓃",
        fontsize="26",
        mouse_callbacks={
            "button1": lazy.spawn("pavucontrol"),
        },
        # padding=5,
    ),
    "value": widget.Volume(
        background=colors.volume_colors["bg"],
        # emoji=true,
        fmt="{}",
        mouse_callbacks={
            "button1": lazy.spawn("pavucontrol"),
        },
        padding=10,
    ),
}

backlight_comp = {
    "sep1": widget.TextBox(
        background=colors.brightness_colors["bg"],
    ),
    "icon": widget.TextBox(
        background=colors.brightness_colors["bg"],
        fmt="󰃝",
        fontsize="26",
        foreground=colors.brightness_colors["fg"],
        # padding=5,
    ),
    "value": widget.Backlight(
        background=colors.brightness_colors["bg"],
        # emoji=true,
        backlight_name="intel_backlight",
        padding=10,
    ),
}

network_comp = {
    "sep1": widget.TextBox(
        background=colors.network_colors["bg"],
    ),
    "icon": widget.TextBox(
        background=colors.network_colors["bg"],
        fmt="󰤥",
        fontsize="26",
        foreground=colors.network_colors["fg"],
        mouse_callbacks={
            "button1": lazy.spawn("networkmanager_dmenu"),
        },
        # padding=5,
    ),
    "value": widget.Wlan(
        background=colors.network_colors["bg"],
        foreground=colors.network_colors["fg"],
        format="{essid}",
        interface="wlp1s0",
        mouse_callbacks={
            "button1": lazy.spawn("networkmanager_dmenu"),
        },
        padding=10,
    ),
}


# widget lists
# ------------

separator_auto = [widget.Spacer()]

separator_small = [
    widget.Spacer(
        length=10,
    )
]

app_launcher = [app_launcher_comp]

windowname = [windowname_comp]

client_count = [client_count_comp]

groups = [groups_comp]

layout_icon = [layout_icon_comp]

battery = [
    battery_comp["sep1"],
    battery_comp["icon"],
    battery_comp["sep2"],
    battery_comp["value"],
]

time = [
    time_comp["sep1"],
    time_comp["icon"],
    time_comp["sep2"],
    time_comp["value"],
]

date = [
    date_comp["sep1"],
    date_comp["icon"],
    date_comp["sep2"],
    date_comp["value"],
]

volume = [
    volume_comp["sep1"],
    volume_comp["icon"],
    volume_comp["value"],
]

backlight = [
    backlight_comp["sep1"],
    backlight_comp["icon"],
    backlight_comp["value"],
]

network = [
    network_comp["sep1"],
    network_comp["icon"],
    network_comp["value"],
]

tray = [
    widget.WidgetBox(
        name="traybox",
        close_button_location="right",
        fontsize=30,
        foreground=colors.tray_colors["bg"],
        text_closed="",
        text_open="",
        widgets=[
            widget.Systray(
                background=colors.tray_colors["bg"],
                padding=5,
            ),
        ]
        + [
            widget.TextBox(
                background=colors.tray_colors["bg"],
            ),
        ]
        + separator_small,
    ),
]

widgetbox_info = [
    widget.WidgetBox(
        name="infobox",
        close_button_location="right",
        fontsize=25,
        foreground=colors.widgetbox_colors["fg"],
        text_closed="",  # 󰸳
        text_open="",  # 󰸶
        # text_closed="",
        # text_open="",
        # padding=10,
        widgets=volume
        + separator_small
        + backlight
        + separator_small
        + network
        + separator_small,
    )
]
