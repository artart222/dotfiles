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

import subprocess
import os
from typing import List
import psutil
import random

from libqtile import qtile
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile import hook
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration


themes = {
    "onedark": {
        "background": "#282c34",
        "gray": "#979eab",
        "green": "#98c379",
        "red": "#e06c75",
        "blue": "#61afef",
        "dark_blue": "#309bff",
        "purple": "#b16fef",
        "orange": "#d19a66",
        "cyan": "#56b6c2",
        "pink": "#f96cc5",
        "yellow": "#e5c07b",
        "white": "#cccccc",
    },
    "enfocado": {
        "background": "#181818",
        "gray": "#3B3B3B",
        "green": "#83C746",
        "red": "#FF5E56",
        "blue": "#4F9CFE",
        "dark_blue": "#2b6CFE",
        "purple": "#B891F5",
        "orange": "#Fa9153",
        "cyan": "#56D8C9",
        "pink": "#FF81CA",
        "yellow": "#EFC541",
        "white": "#DEDEDE",
    },
    "nord": {
        "background": "#2E3441",
        "gray": "#3B4252",
        "green": "#A3BE8C",
        "red": "#BF616A",
        "blue": "#5E81AC",
        "dark_blue": "#1a71AC",
        "purple": "#B48EAD",
        "orange": "#D08770",
        "cyan": "#88C0D0",
        "pink": "#F48EAD",
        "yellow": "#EBCB8B",
        "white": "#ECEFF4",
    },
    "gruvbox": {
        "background": "#282828",
        "gray": "#3c3836",
        "green": "#8ec07c",
        "red": "#cc241d",
        "blue": "#458588",
        "dark_blue": "#157588",
        "purple": "#b16286",
        "orange": "#d79921",
        "cyan": "#83a598",
        "pink": "#d3869b",
        "yellow": "#DF9000",
        "white": "#ebdbb2",
    },
    "catpuccino": {
        "background": "#161321",
        "gray": "#6E6C7E",
        "green": "#ABE9B3",
        "red": "#F28FAD",
        "blue": "#96CDFB",
        "dark_blue": "#76BDFB",
        "purple": "#B891F5",
        "orange": "#F8BD96",
        "cyan": "#B5E8E0",
        "pink": "#DDB6F2",
        "yellow": "#FAE3B0",
        "white": "#D9E0EE",
    },
}


os.system("bash ~/dotfiles/qtile/display.sh")

# Auto starting some programs
@hook.subscribe.startup_once
def autostart():
    processes = [
        ["picom"],
        ["dropbox"],
        ["skypeforlinux"],
        ["discord"],
    ]
    for p in processes:
        subprocess.Popen(p)


@hook.subscribe.client_new
def client_new(client):
    if client.name == "Discord":
        client.togroup("0")
    if client.name == "Skype":
        client.togroup("0")


def set_battery_icon():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    isPlugged = battery.power_plugged
    icon = ""

    if isPlugged:
        if percent == 100:
            icon = ""
        elif 89 < percent < 100:
            icon = ""
        elif 79 < percent < 90:
            icon = ""
        elif 69 < percent < 80:
            icon = ""
        elif 59 < percent < 70:
            icon = ""
        elif 49 < percent < 60:
            icon = ""
        elif 39 < percent < 50:
            icon = ""
        elif 29 < percent < 40:
            icon = ""
        elif 19 < percent < 30:
            icon = ""
        elif 9 < percent < 20:
            icon = ""
        elif 0 <= percent < 10:
            icon = ""
    else:
        if percent == 100:
            icon = ""
        elif 89 < percent < 100:
            icon = ""
        elif 79 < percent < 90:
            icon = ""
        elif 69 < percent < 80:
            icon = ""
        elif 59 < percent < 70:
            icon = ""
        elif 49 < percent < 60:
            icon = ""
        elif 39 < percent < 50:
            icon = ""
        elif 29 < percent < 40:
            icon = ""
        elif 19 < percent < 30:
            icon = ""
        elif 9 < percent < 20:
            icon = ""
        elif 0 <= percent < 10:
            icon = ""
    return icon + " " + str(percent)


def get_brightness_level():
    result = subprocess.run(["brightnessctl", "g"], stdout=subprocess.PIPE)
    result = result.stdout.decode("utf-8")
    result = int(result)
    result = round((100 * result) / 255)
    result = str(result)
    result = result.strip()

    return " " + result


def find_language():
    result = subprocess.run(
        "setxkbmap -query | grep \"layout:\s\" | awk '{print $2}'",
        capture_output=True,
        shell=True,
    )
    result = result.stdout.decode("utf-8")
    result = str(result)
    result = result.strip()

    return result


mod = "mod4"  # mod4 is Windows/Super key
terminal = "kitty"
user_home = os.path.expanduser("~")

theme_name = "enfocado"
theme = themes[theme_name]


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle floating for active window.
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="toggle floating"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key(
        [mod],
        "space",
        lazy.spawn("rofi -theme {} -show drun".format(theme_name)),
        desc="Open rofi as app menu.",
    ),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pulsemixer  --change-volume +5")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pulsemixer  --change-volume -5")),
    Key([], "XF86AudioMute", lazy.spawn("pulsemixer --toggle-mute")),
    Key(
        ["mod1"],
        "Shift_L",
        lazy.spawn("/usr/bin/bash /home/artin/dotfiles/qtile/language.sh"),
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
        [mod, "shift"],
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
        [mod, "control"],
        "Print",
        lazy.spawn(
            "/usr/bin/escrotum -s -C "
            + user_home
            + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"
        ),
        desc="Capture region of screen or app to clipboard",
    ),
    Key([mod], "e", lazy.spawn("kitty -e nvim"), desc="Open NeoVim as text editor"),
]


groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(toggle=False),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=False),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


layouts = [
    layout.Columns(
        border_focus=theme["white"],
        border_normal=theme["background"],
        border_width=1,
        margin=8,
    ),
    layout.Max(),
]


wallpapers_list = os.listdir(user_home + "/Pictures/wallpapers")
wallpapers_list.remove("LICENSE")
wallpapers_list.remove("README.md")
wallpapers_list.remove(".git")


widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=14,
    padding=8,
)

qtile_bar = bar.Bar(
    [
        # Workspaces and spacer
        widget.GroupBox(),
        widget.Spacer(),
        # Updates
        widget.CheckUpdates(
            **widget_defaults,
            display_format=" {updates} updates",
            no_update_string=" 0 updates",
            update_interval=60,
            custom_command="checkupdates",
            colour_no_updates=theme["green"],
            colour_have_updates=theme["green"],
            mouse_callbacks={
                "button1": lambda: qtile.cmd_spawn("yay -Syyu --noconfirm")
            },
        ),
        # Battery
        widget.GenPollText(
            **widget_defaults,
            update_interval=1,
            func=set_battery_icon(),
            foreground=theme["blue"],
        ),
        # CPU
        widget.TextBox(
            **widget_defaults,
            fmt="CPU",
            decorations=[
                RectDecoration(
                    colour=theme["green"], radius=0, filled=True, padding_y=5
                )
            ],
            foreground=theme["background"],
        ),
        widget.CPU(
            **widget_defaults,
            format="{load_percent}",
            mouse_callbacks={"button1": lambda: qtile.cmd_spawn("kitty -e htop")},
            decorations=[
                RectDecoration(colour=theme["gray"], radius=0, filled=True, padding_y=5)
            ],
        ),
        # Screen brightness
        widget.GenPollText(
            **widget_defaults,
            update_interval=1,
            func=get_brightness_level(),
            foreground=theme["red"],
        ),
        widget.Memory(
            **widget_defaults,
            format="{MemUsed: .0f}{mm}M",
            foreground=theme["cyan"],
            mouse_callbacks={"button1": lambda: qtile.cmd_spawn("kitty -e htop")},
        ),
        widget.TextBox(
            **widget_defaults,
            fmt="",
            foreground=theme["purple"],
        ),
        widget.PulseVolume(
            **widget_defaults,
            update_interval=0.1,
            foreground=theme["purple"],
        ),
        widget.TextBox(
            **widget_defaults,
            fmt="",
            decorations=[
                RectDecoration(
                    colour=theme["orange"], radius=0, filled=True, padding_y=5
                )
            ],
        ),
        widget.GenPollText(
            **widget_defaults,
            update_interval=1,
            func=find_language(),
            foreground=theme["background"],
            decorations=[
                RectDecoration(
                    colour=theme["yellow"], radius=0, filled=True, padding_y=5
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.TextBox(
            **widget_defaults,
            fmt="",
            decorations=[
                RectDecoration(
                    colour=theme["dark_blue"],
                    radius=0,
                    filled=True,
                    padding_y=5,
                )
            ],
        ),
        widget.Clock(
            **widget_defaults,
            format="%H:%M %p",
            decorations=[
                RectDecoration(colour=theme["blue"], radius=0, filled=True, padding_y=5)
            ],
        ),
        widget.Systray(
            **widget_defaults,
        ),
    ],
    28,
    opacity=0.8,
    margin=4,
    background=theme["background"],
)

screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/{}".format(
            wallpapers_list[random.randint(0, len(wallpapers_list))]
        ),
        wallpaper_mode="fill",
        top=qtile_bar,
    ),
    Screen(
        wallpaper="~/Pictures/wallpapers/{}".format(
            wallpapers_list[random.randint(0, len(wallpapers_list))]
        ),
        wallpaper_mode="fill",
        top=qtile_bar,
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "qtile"
