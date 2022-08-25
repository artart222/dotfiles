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


from libqtile import qtile
from libqtile import bar
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration


def bar_generator(
    colors,
    widget_settings,
    user_home,
    battery_icon,
    brightness_level,
    keyboard_language,
):
    """Generates bars same settings!!!"""
    return bar.Bar(
        [
            # Workspaces and spacer
            widget.GroupBox(),
            widget.Spacer(),
            # Updates
            widget.CheckUpdates(
                **widget_settings,
                display_format=" {updates} updates",
                no_update_string=" 0 updates",
                update_interval=60,
                custom_command="checkupdates",
                colour_no_updates=colors["green"],
                colour_have_updates=colors["green"],
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn("yay -Syyu --noconfirm")
                },
            ),
            # Battery
            widget.GenPollText(
                **widget_settings,
                update_interval=1,
                func=battery_icon,
                foreground=colors["blue"],
            ),
            # CPU
            widget.TextBox(
                **widget_settings,
                fmt="CPU",
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e htop")},
                decorations=[
                    RectDecoration(
                        colour=colors["green"], radius=0, filled=True, padding_y=5
                    )
                ],
                foreground=colors["background"],
            ),
            widget.CPU(
                **widget_settings,
                format="{load_percent}",
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e htop")},
                decorations=[
                    RectDecoration(
                        colour=colors["gray"], radius=0, filled=True, padding_y=5
                    )
                ],
            ),
            # Screen brightness
            widget.GenPollText(
                **widget_settings,
                update_interval=1,
                func=brightness_level,
                foreground=colors["red"],
            ),
            widget.Memory(
                **widget_settings,
                format="{MemUsed: .0f}{mm}M",
                foreground=colors["cyan"],
                mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e htop")},
            ),
            widget.TextBox(
                **widget_settings,
                fmt="",
                foreground=colors["purple"],
            ),
            widget.PulseVolume(
                **widget_settings,
                update_interval=0.1,
                foreground=colors["purple"],
            ),
            widget.TextBox(
                **widget_settings,
                fmt=" ",
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"/usr/bin/bash {user_home}/.config/qtile/scripts/language.sh"
                    )
                },
                decorations=[
                    RectDecoration(
                        colour=colors["orange"], radius=0, filled=True, padding_y=5
                    )
                ],
            ),
            widget.GenPollText(
                **widget_settings,
                update_interval=1,
                func=keyboard_language,
                foreground=colors["background"],
                mouse_callbacks={
                    "Button1": lambda: qtile.cmd_spawn(
                        f"/usr/bin/bash {user_home}/.config/qtile/scripts/language.sh"
                    )
                },
                decorations=[
                    RectDecoration(
                        colour=colors["yellow"], radius=0, filled=True, padding_y=5
                    )
                ],
            ),
            # widget.GenPollText(
            #     **widget_settings,
            #     update_interval=5,
            #     func=find_network_name,
            #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e nmtui")},
            # ),
            widget.Spacer(length=8),
            widget.TextBox(
                **widget_settings,
                fmt="",
                decorations=[
                    RectDecoration(
                        colour=colors["dark_blue"],
                        radius=0,
                        filled=True,
                        padding_y=5,
                    )
                ],
            ),
            widget.Clock(
                **widget_settings,
                format="%H:%M %p",
                decorations=[
                    RectDecoration(
                        colour=colors["blue"], radius=0, filled=True, padding_y=5
                    )
                ],
            ),
            widget.Systray(
                **widget_settings,
            ),
        ],
        28,
        opacity=0.8,
        margin=4,
        background=colors["background"],
    )
