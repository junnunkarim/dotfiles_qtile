import subprocess
import json

from .wallpapers import wall

# Define the command as a list of strings
command = [
    "matugen",
    "image",
    "-j",
    "hex",
    # "-t",
    # "scheme-fruit-salad",
    # "scheme-neutral",
    # "scheme-fidelity",
    # "scheme-content",
    # "scheme-rainbow",
    # "scheme-monochrome",
    # "scheme-expressive",
    wall,
]

# Run the command and capture its output
output = subprocess.run(command, capture_output=True, text=True, check=True)

# Check if the command was successful
if output.returncode == 0:
    # Parse the JSON output
    json_output = json.loads(output.stdout)

    c = json_output["colors"]["dark"]

    # Widget Colors
    app_launcher_colors = {
        "fg": c["on_tertiary_container"],
        "bg": c["tertiary_container"],
    }

    tray_colors = {
        "fg": c["on_tertiary"],
        "fg_icon": c["on_tertiary"],
        "bg": c["tertiary"],
    }

    windowname_colors = {
        "fg": c["on_surface"],
        "bg": c["surface"],
    }

    windowcount_colors = {
        "fg": c["on_primary_fixed"],
        "bg": c["primary_fixed"],
    }

    groupbox_colors = {
        "fg_active": c["on_primary"],
        "fg_inactive": c["on_secondary_container"],
        "bg": c["primary"],
        "fg_focus": c["on_primary_container"],
        "bg_focus": c["primary_container"],
        "fg_urgent": c["on_error"],
        "bg_urgent": c["error"],
    }

    layout_colors = {
        "bg": c["inverse_primary"],
    }

    volume_colors = {
        "fg": c["on_tertiary_container"],
        "bg": c["tertiary_container"],
    }

    brightness_colors = {
        "fg": c["on_tertiary_container"],
        "bg": c["tertiary_container"],
    }

    network_colors = {
        "fg": c["on_tertiary_container"],
        "bg": c["tertiary_container"],
    }

    widgetbox_colors = {
        "bg": c["tertiary"],
        "fg": c["tertiary"],
    }

    battery_colors = {
        "fg": c["on_secondary"],
        "fg_icon": c["on_primary_container"],
        "fg_low": c["on_secondary_container"],
        "bg": c["secondary"],
        "bg_icon": c["primary_container"],
        "bg_low": c["secondary_container"],
    }

    time_colors = {
        "fg": c["on_secondary"],
        "fg_icon": c["on_primary_container"],
        "bg": c["secondary"],
        "bg_icon": c["primary_container"],
    }

    date_colors = {
        "fg": c["on_secondary"],
        "fg_icon": c["on_primary_container"],
        "bg": c["secondary"],
        "bg_icon": c["primary_container"],
    }

    client_colors = {
        "border": c["outline_variant"],
        "border_focus": c["primary"],
        "border_floating": c["tertiary"],
    }

    bar_colors = {
        "bg": c["surface"],
        "border": c["surface"],
    }
else:
    # Print an error message if the command failed
    print(f"Command failed with return code {output.returncode}")
