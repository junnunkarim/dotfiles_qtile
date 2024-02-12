import os
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    # processes = [
    #     # ["bash", ".fehbg"],
    #     # ["xfce4-power-manager"],
    #     # ["/usr/lib/xfce-polkit/xfce-polkit"],
    #     # ["/usr/bin/gnome-keyring-daemon", "--start"],
    #     ["/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1"],
    #     ["picom -b"],
    #     ["redshift -P -O 5500"],
    #     ["greenclip", "daemon"],
    #     # ["nm-applet"],
    # ]

    # for p in processes:
    #     subprocess.Popen(p)

    autostart_script = os.path.expanduser("~/.config/qtile/core/autostart.sh")
    subprocess.Popen([autostart_script])
