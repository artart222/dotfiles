"""
Copyright (c) 2010 Aldo Cortesi
Copyright (c) 2011 Florian Mounier
Copyright (c) 2011 oitel
Copyright (c) 2011 Kenji_Takahashi
Copyright (c) 2011 Paul Colomiets
Copyright (c) 2012, 2014 roger
Copyright (c) 2012 nullzion
Copyright (c) 2013 Tao Sauvage
Copyright (c) 2014-2015 Sean Vig
Copyright (c) 2014 Nathan Hoad
Copyright (c) 2014 dequis
Copyright (c) 2014 Tycho Andersen
Copyright (c) 2020, 2021 Robert Andrew Ditthardt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

╭──────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                      │
│                                                                                      │
│      ░█████╗░██████╗░████████╗░█████╗░██████╗░████████╗██████╗░██████╗░██████╗░      │
│      ██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝╚════██╗╚════██╗╚════██╗      │
│      ███████║██████╔╝░░░██║░░░███████║██████╔╝░░░██║░░░░░███╔═╝░░███╔═╝░░███╔═╝      │
│      ██╔══██║██╔══██╗░░░██║░░░██╔══██║██╔══██╗░░░██║░░░██╔══╝░░██╔══╝░░██╔══╝░░      │
│      ██║░░██║██║░░██║░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗███████╗███████╗      │
│      ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚══════╝      │
│                                                                                      │
│ ░██████╗░████████╗██╗██╗░░░░░███████╗  ░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░ │
│ ██╔═══██╗╚══██╔══╝██║██║░░░░░██╔════╝  ██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░ │
│ ██║██╗██║░░░██║░░░██║██║░░░░░█████╗░░  ██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░ │
│ ╚██████╔╝░░░██║░░░██║██║░░░░░██╔══╝░░  ██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗ │
│ ░╚═██╔═╝░░░░██║░░░██║███████╗███████╗  ╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝ │
│ ░░░╚═╝░░░░░░╚═╝░░░╚═╝╚══════╝╚══════╝  ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░ │
│                                                                                      │
│                                                                                      │
╰──────────────────────────────────────────────────────────────────────────────────────╯
"""

import os
from libqtile.config import Key, Group, Drag, Click
from libqtile.lazy import lazy
from themes import find_theme

TERMINAL = "kitty"
theme_name = find_theme()
user_home = os.path.expanduser("~")

MOD = "mod4"  # MOD4 is Windows/Super key


groups = [Group(i) for i in "1234567890"]


keys = [
    # Switch between windows
    Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
    Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
    Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [MOD, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [MOD, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [MOD, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [MOD, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle floating for active window.
    Key([MOD, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [MOD, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([MOD], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([MOD], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([MOD, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([MOD, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [MOD],
        "space",
        lazy.spawn(f"rofi -theme ~/.config/rofi/themes/{theme_name} -show drun"),
        desc="Open rofi as app menu.",
    ),
    Key(
        [MOD],
        "f",
        lazy.spawn(
            f"fd --follow --exclude=.git --hidden | rofi -theme ~/.config/rofi/themes/{theme_name}\
                    -show file-browser-extended -file-browser-disable-status -file-browser-stdin",
            shell=True,
        ),
        desc="Open rofi as file browser menu.",
    ),
    Key(
        [MOD],
        "g",
        lazy.spawn(
            f"rofi -theme ~/.config/rofi/themes/{theme_name} -show emoji",
            shell=True,
        ),
        desc="Open rofi as emoji browser menu.",
    ),
    Key(
        [MOD],
        "c",
        lazy.spawn(
            f"rofi -theme ~/.config/rofi/themes/{theme_name} -show calc",
            shell=True,
        ),
        desc="Open rofi as calculator.",
    ),
    Key(
        [MOD],
        "n",
        lazy.spawn(
            "bash ~/.config/rofi/rofi-network-manager/rofi-network-manager.sh",
            shell=True,
        ),
        desc="Open rofi as network manager.",
    ),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer  --change-volume +5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer  --change-volume -5")),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key(
        ["mod1"],
        "Shift_L",
        lazy.spawn(f"/usr/bin/bash {user_home}/.config/qtile/scripts/language.sh"),
    ),
    # Screenshots
    Key(
        [],
        "Print",
        lazy.spawn(
            "/usr/bin/escrotum "
            + user_home
            + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"
        ),
        desc="Save screen to screenshots folder",
    ),
    # Capture region of screen or app
    Key(
        [MOD, "shift"],
        "Print",
        lazy.spawn(
            "/usr/bin/escrotum -s "
            + user_home
            + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"
        ),
        desc="Capture region of screen or app",
    ),
    # Capture region of screen or app to clipboard
    Key(
        [MOD, "control"],
        "Print",
        lazy.spawn(
            "/usr/bin/escrotum -s -C "
            + user_home
            + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"
        ),
        desc="Capture region of screen or app to clipboard",
    ),
    Key([MOD], "e", lazy.spawn("kitty -e nvim"), desc="Open NeoVim as text editor"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(toggle=False),
                desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

# Drag floating layouts.
mouse = [
    Drag(
        [MOD],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [MOD], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]
