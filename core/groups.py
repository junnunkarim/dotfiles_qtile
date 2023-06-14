from libqtile import hook, qtile
from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keymaps import mod, keys
from .scratchpad import scratchpad

groups = [
    Group(
        '1',
        #label="",
        label="",
        matches=[
            Match(wm_class="Alacritty"),
            Match(wm_class="org.wezfurlong.wezterm"),
            Match(wm_class="geany"),
            Match(wm_class="jetbrains-idea-ce"),
            Match(wm_class="Emacs"),
        ],
    ),
    Group(
        '2',
        #label="",
        label="",
        matches=[
            Match(wm_class="thunar"),
            Match(wm_class="qbittorrent"),
        ],
    ),
    Group(
        '3',
        #label="",
        label="",
        matches=[
            Match(wm_class="firefox"),
            Match(wm_class="chromium"),
            Match(wm_class="nyxt"),
            Match(wm_class="vieb"),
        ],
    ),
    Group(
        '4',
        #label="ﮑ",
        label="",
        matches=[
            Match(title="GNU Image Manipulation Program"), # gimp
            Match(wm_class="vlc"),
            Match(wm_class="mpv")
        ],
    ),
    Group(
        '5',
        #label="龎",
        label="",
        matches=[
            Match(wm_class="calibre-gui"),
            Match(wm_class="DesktopEditors"),
            Match(wm_class="org.pwmt.zathura"),
            Match(wm_class="sioyek"),
        ],
    ),
    Group(
        '6',
        #label="ﮠ",
        label="",
        matches=[
            Match(wm_class="telegram-desktop"),
        ],
    ),
    Group(
        '7',
        #label="",
        label="",
        matches=[
            Match(wm_class="Ryujinx"),
            Match(wm_class="yuzu"),
            Match(wm_class="retroarch"),
        ],
    ),
    Group(
        '8',
        #label="煉",
        label="",
        matches=[
            Match(wm_class="Gparted"),
            Match(wm_class="xfce4-power-manager-settings"),
            Match(wm_class="lxappearance"),
        ],
    ),
    Group(
        '9',
        #label="",
        label="",
        matches=[],
    ),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to and move focused window to group {}".format(i.name)),
    ])

# add scratchpads in the group
# can't add it directly because of the upper for statement
groups.append(scratchpad)

# Switch to a window's assigned group when it is opened
@hook.subscribe.client_managed
def auto_switch(window):
    if window.group.name != qtile.current_group.name:
        window.group.cmd_toscreen()
