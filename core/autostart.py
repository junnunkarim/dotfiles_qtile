import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    autostart_script = os.path.expanduser("~/.config/qtile/core/autostart.sh")
    subprocess.Popen([autostart_script])
