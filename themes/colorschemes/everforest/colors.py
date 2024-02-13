from themes.raw_colorschemes import everforest

c = everforest

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
    "bg": c["red1"],
    "border": c["red1"],
}

battery_colors = {
    "fg": c["black"],
    "fg_icon": c["black"],
    "bg": c["blue1"],
    "bg_icon": c["blue2"],
    "border": c["blue1"],
}

time_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["aqua1"],
    "bg_icon": c["aqua2"],
    "border": c["aqua2"],
}

date_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["yellow1"],
    "bg_icon": c["yellow2"],
    "border": c["yellow2"],
}

tray_colors = {
    "fg": other_colors["dark"],
    "fg_icon": c["black"],
    "bg": c["yellow1"],
    "border": c["red2"],
}

groupbox_colors = {
    "bg": c["green1"],
    "bg_focus": c["green1"],
    "bg_urgent": c["black"],
    "fg": c["gray1"],
    "fg_focus": c["black"],
    "fg_occupied": c["black"],
    "fg_urgent": c["red1"],
    "border": c["green1"],
    "hover": c["aqua1"],
}

windowname_colors = {
    "fg": c["gray1"],
    "fg_focus": c["black0"],
    "fg_minimize": c["red1"],
    "bg": c["black"],
    "bg_focus": c["gray1"],
    "bg_minimize": c["red1"],
    "border": c["black"],
}

titlebar_colors = {
    "border": c["black"],
    "border_focus": c["green1"],
    "border_floating": c["orange1"],
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
    "bg": c["red1"],
    "fg": c["black"],
}

brightness_colors = {
    "bg": c["orange1"],
    "fg": c["black"],
}

network_colors = {
    "bg": c["yellow1"],
    "fg": c["black"],
}

windowcount_colors = {
    "bg": c["blue1"],
    "fg": c["black"],
}

layout_colors = {
    "bg": c["blue1"],
}
