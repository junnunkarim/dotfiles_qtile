import os
import shutil

from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from options import default_apps, default_options

mod, alt, ctrl = (
    default_options["mod"],
    default_options["alt"],
    default_options["ctrl"],
)
terminal = default_apps["terminal"] or guess_terminal()
home = os.path.expanduser("~")
scripts = home + "/.config/qtile/scripts/"

keys = [
    ##---------- System (super [+ shift]) ----------##
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # toggles
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "space", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle visibility of the bar"),
    Key(
        [mod, "shift"],
        "w",
        lazy.widget["infobox"].toggle(),
        desc="Toggle WidgetBox of the bar",
    ),
    Key(
        [mod, "shift"],
        "t",
        lazy.widget["traybox"].toggle(),
        desc="Toggle WidgetBox of the bar",
    ),
    # cycle through windows and groups
    Key(
        [mod],
        "Tab",
        lazy.screen.next_group(skip_empty=True),
        desc="Cycle through octive groups clockwise",
    ),
    Key(
        [mod],
        "grave",
        lazy.screen.prev_group(skip_empty=True),
        desc="Cycle through octive groups anti-clockwise",
    ),
    Key(
        [alt], "Tab", lazy.group.next_window(), desc="Move window focus to other window"
    ),
    Key(
        [alt],
        "grave",
        lazy.group.prev_window(),
        desc="Move window focus to other window",
    ),
    Key(
        [mod, "control", "shift"],
        "space",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    Key([mod], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "l", lazy.spawn("slock"), desc="Lock Screen"),
    # rofi menus
    Key(
        [mod],
        "d",
        lazy.spawn([scripts + "rofi_run"]),
        desc="Open App Launcher",
    ),
    Key(
        [mod],
        "x",
        lazy.spawn([scripts + "powermenu"]),
        desc="Open PowerMenu",
    ),
    Key(
        [mod],
        "h",
        lazy.spawn([scripts + "clipboard"]),
        desc="Open Clipboard",
    ),
    Key(
        [mod],
        "r",
        lazy.spawn([scripts + "rofi_calc"]),
        desc="Open Calculator",
    ),
    Key(
        [mod, "shift"],
        "b",
        lazy.spawn([scripts + "rofi_buku"]),
        desc="Open buku",
    ),
    Key(
        [mod],
        "t",
        lazy.spawn([scripts + "theme_switcher"]),
        desc="Open theme-switcher",
    ),
    Key([mod], "n", lazy.spawn("networkmanager_dmenu"), desc="Open Network Manager"),
    ##---------- System Keys ----------##
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn('brightnessctl -d "intel_backlight" set +2%'),
        desc="Raise Brightness",
    ),
    Key(
        [],
        "F2",
        lazy.spawn('brightnessctl -d "intel_backlight" set +2%'),
        desc="Raise Brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn('brightnessctl -d "intel_backlight" set 2%-'),
        desc="Lower Brightness",
    ),
    Key(
        [],
        "F1",
        lazy.spawn('brightnessctl -d "intel_backlight" set 2%-'),
        desc="Lower Brightness",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        # lazy.spawn("pactl set-sink-volume 0 -2%"),
        lazy.spawn("pulsemixer --change-volume -5 --max-volume 100"),
        desc="Lower Volume",
    ),
    Key(
        [],
        "F5",
        lazy.spawn("pulsemixer --change-volume -5 --max-volume 100"),
        desc="Lower Volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        # lazy.spawn("pactl set-sink-volume 0 +2%"),
        lazy.spawn("pulsemixer --change-volume +5 --max-volume 100"),
        desc="Raise Volume",
    ),
    Key(
        [],
        "F6",
        lazy.spawn("pulsemixer --change-volume +5 --max-volume 100"),
        desc="Raise Volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        # lazy.spawn("pactl set-sink-mute 0 toggle"),
        lazy.spawn("pulsemixer --toggle-mute"),
        desc="Mute Volume",
    ),
    Key([], "F7", lazy.spawn("pulsemixer --toggle-mute"), desc="Mute Volume"),
    Key(
        [],
        "Print",
        lazy.spawn(["flameshot", "full", "-p", home + "/Pictures/SS/"]),
        desc="Take Screenshot",
    ),
    Key([mod], "Print", lazy.spawn("flameshot gui"), desc="Open Flameshot GUI"),
    Key(
        [alt],
        "Print",
        lazy.spawn(["flameshot", "full", "-d", "5000", "-p", home + "/Pictures/SS/"]),
        desc="Take Screenshot after 5 seconds",
    ),
    Key(
        ["shift"],
        "Print",
        lazy.spawn(["flameshot", "full", "-d", "10000", "-p", home + "/Pictures/SS/"]),
        desc="Take Screenshot after 10 seconds",
    ),
    ##---------- Applications (super + alt) ----------##
    # web browser
    Key([mod, alt], "b", lazy.spawn("chromium"), desc="Open Chromium"),
    Key([mod, alt], "e", lazy.spawn("firefox"), desc="Open Firefox"),
    # file manager
    Key([mod, alt], "f", lazy.spawn("thunar"), desc="Open Thunar"),
    # cli programs
    Key(
        [mod, alt],
        "n",
        lazy.spawn([home + "/.bin/nnn_run"]),
        desc="Open NNN file manager",
    ),
    Key([mod, alt], "v", lazy.spawn("alacritty -e nvim"), desc="Open Neovim"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    # Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    # Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    # Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    # Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),
    ##---------- Other programs or scripts (super + ctrl) ----------##
    # bluelight filter
    Key(
        [mod, ctrl],
        "r",
        lazy.spawn("redshift -P -O 5000"),
        desc="Turn on Bluelight filter",
    ),
    Key([mod, ctrl], "n", lazy.spawn("redshift -x"), desc="Turn on Bluelight filter"),
    Key(
        [mod, ctrl],
        "v",
        lazy.spawn("redshift -P -O 3500"),
        desc="Turn on Bluelight filter",
    ),
    # X11 compositor
    Key([mod, ctrl], "p", lazy.spawn("picom"), desc="Turn on Picom"),
    Key([mod, ctrl], "u", lazy.spawn("pkill picom"), desc="Turn off Picom"),
    Key([mod, ctrl], "g", lazy.spawn("gpick"), desc="Open Color Picker"),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]
