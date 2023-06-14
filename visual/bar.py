from libqtile import bar, widget

from core.utils import gaps_size
from .utils import raw_colors
color = raw_colors.gruvbox

top_bar = bar.Bar(
    [
        widget.TextBox(
            fmt="󰣇",
            fontsize=40,
            padding=10,
        ),
        widget.WindowName(
            fmt="<i>{}</i>",
            max_chars=40,
            #padding=200,
        ),
        widget.CurrentLayoutIcon(
            scale=0.7,
        ),
        widget.GroupBox(
            disable_drag=False,
            hide_unused=True,
            highlight_method='block',
            margin_x=3,
        ),
        widget.WindowCount(
            fmt='╹{}╻',
            #fmt='>(O・O)->{}',
            #fmt='(っ˘̩╭╮˘̩)っ{}',
            #fmt='(っO~O)っ{}',
            #fmt='☆⌒(ゝ。∂){}',
            #fmt='ʕ•ᴥ•ʔ{}',
            #fmt='( ˘▽ ˘)っ♨{}',
        ),
        widget.WidgetBox(
            fontsize=30,
            text_closed="", # 󰸳
            text_open="", # 󰸶
            widgets=[
                widget.Volume(
                    #emoji=True,
                ),
                widget.Backlight(
                    #emoji=True,
                    backlight_name='intel_backlight',
                ),
            ],
        ),
        widget.Spacer(),
        widget.Wlan(
            format='{essid}',
            interface='wlp1s0',
        ),
        widget.Battery(
            charge_char='',
            discharge_char='󱟞',
            full_char='',
            format='{char}{percent:2.0%}',
        ),
        widget.TextBox(
            fmt='',
            fontsize='26',
        ),
        widget.Clock(
            format="%I:%M %p"
        ),
        widget.TextBox(
            fmt='',
            fontsize='26',
        ),
        widget.Clock(
            format="%a %d-%m-%Y"
        ),
        widget.Systray(),
        #widget.QuickExit(),
    ],
    30,
    background = color["blue1"],
    margin = [gaps_size, gaps_size, 0, gaps_size], # [up, left, down, left]
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
