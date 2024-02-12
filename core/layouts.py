from libqtile import layout
from libqtile.config import Match

from options import default_options

gaps_size = default_options["gaps_size"]

layouts = [
    layout.Max(border_focus="#d08770", border_width=2, margin=gaps_size),
    layout.Tile(
        add_after_last=True,
        border_focus="#d08770",
        border_width=2,
        margin=gaps_size,
        max_ratio=0.50,
        ratio=0.50,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=10),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="blueman-manager"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="gpick"),
        Match(wm_class="lxappearance"),
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="protonvpn"),
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="xfce4-about"),
        Match(wm_class="xfce4-power-manager-settings"),
        Match(title="branchdialog"),  # gitk
        Match(title="GNU Image Manipulation Program"),  # gimp
        Match(title="pinentry"),  # GPG key password entry
    ]
)
