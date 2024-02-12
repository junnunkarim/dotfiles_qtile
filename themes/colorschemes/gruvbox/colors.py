from themes.raw_colorschemes import gruvbox

c = gruvbox

other_colors = {
    "light": c["white"],
    "gray": c["gray1"],
    "dark": c["black"],
    "too_dark": c["black0"],
    "font": c["white"],
    "bg": c["black"],
    "border": c["black"],
}

# Widget Colors
app_launcher_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["red2"],
    "border": c["red1"],
}

battery_colors = {
    "fg": c["black"],
    "fg_icon": c["black"],
    "bg": c["blue2"],
    "bg_icon": c["blue1"],
    "border": c["blue1"],
}

time_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["aqua2"],
    "bg_icon": c["aqua1"],
    "border": c["aqua1"],
}

date_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["purple2"],
    "bg_icon": c["purple1"],
    "border": c["purple1"],
}

tray_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["black"],
    "border": c["orange1"],
}

groupbox_colors = {
    "bg": c["green1"],
    "bg_focus": c["green2"],
    "bg_urgent": c["green1"],
    "fg": c["gray1"],
    "fg_focus": c["black"],
    "fg_occupied": c["black"],
    "fg_urgent": c["red1"],
    "border": c["green1"],
    "hover": c["gray2"],
}

windowname_colors = {
    "fg": c["orange1"],
    "fg_focus": c["white"],
    "fg_minimize": c["red2"],
    "bg": c["black"],
    "bg_focus": c["orange2"],
    "bg_minimize": c["red1"],
    "border": c["black"],
}

titlebar_colors = {
    "border": c["black"],
    "border_focus": c["green2"],
    "border_floating": c["orange2"],
}

bar_colors = {
    "bg": c["black"],
    "border": c["black"],
}

widgetbox_colors = {
    "bg": c["red1"],
    "fg": c["red1"],
}

volume_colors = {
    "bg": c["red2"],
    "fg": c["black"],
}

brightness_colors = {
    "bg": c["orange2"],
    "fg": c["black"],
}

network_colors = {
    "bg": c["yellow2"],
    "fg": c["black"],
}

windowcount_colors = {
    "bg": c["blue2"],
    "fg": c["black"],
}

layout_colors = {
    "bg": c["blue2"],
}
