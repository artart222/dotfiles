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
import random
import psutil

from libqtile import layout
from libqtile.config import Match, Screen
from libqtile import hook

from screen import bar_generator
from themes import find_theme, themes
from keys import groups, keys, mouse


os.system("bash ~/.config/qtile/scripts/display.sh")


@hook.subscribe.startup_once
def autostart():
    """Auto starting some programs"""
    processes = [
        ["picom"],
        ["dropbox"],
        ["discord"],
    ]
    for process in processes:
        subprocess.Popen(process)


@hook.subscribe.client_new
def client_new(client):
    """Moving some windows to other workspaces"""
    if client.name == "Discord":
        client.togroup("0")
    if client.name == "Skype":
        client.togroup("0")


def set_battery_icon():
    """Find best battery icon for qtile bar"""
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    is_pluged = battery.power_plugged
    icon = ""

    if is_pluged:
        if percent == 100:
            icon = "󰂅"
        elif 89 < percent < 100:
            icon = "󰂋"
        elif 79 < percent < 90:
            icon = "󰂊"
        elif 69 < percent < 80:
            icon = "󰢞"
        elif 59 < percent < 70:
            icon = "󰂉"
        elif 49 < percent < 60:
            icon = "󰢝"
        elif 39 < percent < 50:
            icon = "󰂈"
        elif 29 < percent < 40:
            icon = "󰂇"
        elif 19 < percent < 30:
            icon = "󰂆"
        elif 9 < percent < 20:
            icon = "󰢜"
        elif 0 <= percent < 10:
            icon = "󰢟"
    else:
        if percent == 100:
            icon = "󰁹"
        elif 89 < percent < 100:
            icon = "󰂂"
        elif 79 < percent < 90:
            icon = "󰂁"
        elif 69 < percent < 80:
            icon = "󰂀"
        elif 59 < percent < 70:
            icon = "󰁿"
        elif 49 < percent < 60:
            icon = "󰁾"
        elif 39 < percent < 50:
            icon = "󰁽"
        elif 29 < percent < 40:
            icon = "󰁼"
        elif 19 < percent < 30:
            icon = "󰁻"
        elif 9 < percent < 20:
            icon = "󰁺"
        elif 0 <= percent < 10:
            icon = "󱃍"
    return icon + " " + str(percent)


def get_brightness_level():
    """Finding brightness level of laptop display"""
    result = subprocess.run(["brightnessctl", "g"], stdout=subprocess.PIPE, check=True)
    result = result.stdout.decode("utf-8")
    result = int(result)
    result = round((100 * result) / 255)
    result = str(result)
    result = result.strip()

    return "󰃞 " + result


def find_language():
    """Finding system keyboard language"""
    result = subprocess.run(
        "setxkbmap -query | grep \"layout:\\s\" | awk '{print $2}'",
        capture_output=True,
        shell=True,
        check=True,
    )
    result = result.stdout.decode("utf-8")
    result = str(result)
    result = result.strip()

    return result


def find_network_name():
    result = subprocess.run(
        "nmcli device status | grep \"\\bconnected\" | cut -d' ' -f22-",
        capture_output=True,
        shell=True,
        check=True,
    )
    result = result.stdout.decode("utf-8")
    result = str(result)
    result = result.strip()
    return result


user_home = os.path.expanduser("~")


theme_name = find_theme()
theme = themes[theme_name]
os.system(
    f'sed -i "1s/.*/"\'include themes\\/{theme_name}\'.conf"/" ~/.config/kitty/kitty.conf'
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

screens = [
    Screen(
        wallpaper=f"~/Pictures/wallpapers/{wallpapers_list[random.randint(0, len(wallpapers_list))]}",
        wallpaper_mode="fill",
        top=bar_generator(
            theme,
            widget_defaults,
            user_home,
            set_battery_icon,
            get_brightness_level,
            find_language,
        ),
    ),
    Screen(
        wallpaper=f"~/Pictures/wallpapers/{wallpapers_list[random.randint(0, len(wallpapers_list))]}",
        wallpaper_mode="fill",
        top=bar_generator(
            theme,
            widget_defaults,
            user_home,
            set_battery_icon,
            get_brightness_level,
            find_language,
        ),
    ),
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
