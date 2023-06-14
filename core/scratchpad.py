from libqtile.config import DropDown, Key, ScratchPad
from libqtile.lazy import lazy

from .keymaps import mod, keys

dropdowns = [
    DropDown("term", "alacritty", width=0.6, height=0.6, x=0.2, y=0.1, on_focus_lost_hide=False),
    DropDown("password_manager", "keepassxc", width=0.6, height=0.6, x=0.2, y=0.1, on_focus_lost_hide=False),
    DropDown("task_manager", "alacritty -e btop", width=0.8, height=0.8, x=0.1, y=0.1, on_focus_lost_hide=False),
]

keys.extend(
    [
        Key([mod, "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle("term")),
        Key([mod, "shift"], "BackSpace", lazy.group['scratchpad'].dropdown_toggle("password_manager")),
        Key([mod, "shift"], "h", lazy.group['scratchpad'].dropdown_toggle("task_manager")),
    ]
)

scratchpad = ScratchPad("scratchpad", dropdowns)
