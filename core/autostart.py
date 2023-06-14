import subprocess
from libqtile import hook

@hook.subscribe.startup_once
def autostart():
    processes = [
        #["bash", ".fehbg"],
        ["xfce4-power-manager"],
        ["/usr/lib/xfce-polkit/xfce-polkit"],
        ["picom"],
        #["nm-applet"],
        ["/usr/bin/gnome-keyring-daemon", "--start"],
        ["greenclip", "daemon"],
    ]

    for p in processes:
        subprocess.Popen(p)
