#!/usr/bin/env python

import subprocess

from fileinput import FileInput
from pathlib import Path as path


# core string replacement function
# --------------------------------
def replace_string(
    replace: str, start_concatenate: str, end_concatenate: str, file_path: str
) -> None:
    file = path(file_path).expanduser()

    with FileInput(file, inplace=True) as file:
        for line in file:
            if line.startswith(start_concatenate):
                # Replace the string within quotes
                line = start_concatenate + replace + end_concatenate + "\n"
            print(line, end="")


# functions for changing gui/cli application colorsechemes/themes
# ---------------------------------------------------------------
def alacritty_color(replace: str) -> None:
    start_concatenate = 'import = ["/home/dragoonfx/.config/alacritty/colorschemes/'
    end_concatenate = '.toml"]'
    file_path = "~/.config/alacritty/colors.toml"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def btop_color(replace: str) -> None:
    start_concatenate = 'color_theme = "'
    end_concatenate = '"'
    file_path = "~/.config/btop/btop.conf"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def gtk_color(replace: str) -> None:
    start_concatenate = "gtk-theme-name="
    end_concatenate = ""
    file_path = "~/.config/gtk-3.0/settings.ini"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def helix_color(replace: str) -> None:
    start_concatenate = 'theme = "'
    end_concatenate = '"'
    file_path = "~/.config/helix/config.toml"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def kitty_color(replace: str) -> None:
    start_concatenate = "include ~/.config/kitty/colorschemes/"
    end_concatenate = ".conf"
    file_path = "~/.config/kitty/kitty.conf"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def konsole_color(replace: str) -> None:
    start_concatenate = "ColorScheme="
    end_concatenate = ""
    file_path = "~/.local/share/konsole/main.profile"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def nvim_color(replace: str) -> None:
    start_concatenate = 'local color = "'
    end_concatenate = '"'
    file_path = "~/.config/nvim/lua/core/colorscheme.lua"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def qtile_color(replace: str) -> None:
    start_concatenate = 'default_colorscheme = "'
    end_concatenate = '"'
    file_path = "~/.config/qtile/options.py"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def rofi_color(replace: str) -> None:
    start_concatenate = '@import "~/.config/qtile/external_configs/rofi/colorschemes/'
    end_concatenate = '.rasi"'
    file_path = "~/.config/qtile/external_configs/rofi/colors.rasi"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


def zathura_color(replace: str) -> None:
    start_concatenate = "include colorschemes/"
    end_concatenate = ""
    file_path = "~/.config/zathura/zathurarc"

    replace_string(replace, start_concatenate, end_concatenate, file_path)


# functions for hot reloading programs
# ------------------------------------
def reload_kitty() -> None:
    # kitty process ids
    get_process_id = [
        "pgrep",
        "kitty",
    ]

    select = subprocess.run(
        get_process_id, text=True, capture_output=True, check=True
    ).stdout.replace("\n", " ")

    # split the string into separate process ids
    process_ids = select.split()

    command = ["kill", "-SIGUSR1"] + process_ids

    print(subprocess.run(command, text=True, check=True))


def reload_qtile() -> None:
    command = [
        "qtile",
        "cmd-obj",
        "-o",
        "cmd",
        "-f",
        "reload_config",
    ]

    subprocess.run(command, text=True, check=True)


# all colorscheme switcher function
# ---------------------------------
def change_colorscheme(colorscheme: str) -> None:
    if colorscheme == "catppuccin_macchiato":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-catppuccin-macchiato")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "dracula":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-dracula")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "everblush":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("everblush")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "everforest":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-everforest")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "gruvbox":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-gruvbox")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "nord":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-nord")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "rose_pine":
        alacritty_color(colorscheme)
        btop_color(colorscheme)
        gtk_color(colorscheme)
        kitty_color(colorscheme)
        konsole_color(colorscheme)
        nvim_color("base16-rose-pine")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        zathura_color(colorscheme)
    elif colorscheme == "matugen":
        # alacritty_color(colorscheme)
        # btop_color(colorscheme)
        # gtk_color(colorscheme)
        kitty_color(colorscheme)
        # konsole_color(colorscheme)
        # nvim_color("base16-rose-pine")
        qtile_color(colorscheme)
        rofi_color(colorscheme)
        # zathura_color(colorscheme)
        pass
    else:
        pass


# main function
# --------------------------------
def main() -> None:
    prompt = [
        "rofi",
        "-dmenu",
        "-i",
        "-theme",
        f"{path('~/.config/qtile/external_configs/rofi/script_menu.rasi').expanduser()}",
    ]

    colorschemes = {
        "cancel": " Cancel",
        "catppuccin_macchiato": " Catppuccin (Macchiato)",
        "dracula": " Dracula",
        # "everblush": " Everblush",
        "everforest": " Everforest",
        "gruvbox": " Gruvbox",
        "nord": " Nord",
        "rose_pine": " Rose Pine",
        "matugen": " Matugen (Material You color)",
    }

    # variable to pass to dmenu or rofi
    option = "\n".join(colorschemes.values())

    select = subprocess.run(
        prompt, input=option, text=True, capture_output=True, check=True
    ).stdout.strip()

    choice = next((key for key, value in colorschemes.items() if value == select), "")

    change_colorscheme(choice)

    reload_kitty()
    reload_qtile()


if __name__ == "__main__":
    main()
