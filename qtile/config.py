from typing import List

from libqtile import qtile
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook

import subprocess
import os
import random
import psutil

os.system("bash ~/dotfiles/scripts/display.sh")

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

def fix_firefox_name(text):
    return text.split("— ")[-1]

def set_battery_icon():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    isPlugged = battery.power_plugged
    icon = ""

    if isPlugged:
        if percent == 100:
            icon = ""
        elif percent > 89 and percent < 100:
            icon = ""
        elif percent > 79 and percent < 90:
            icon = ""
        elif percent > 69 and percent < 80:
            icon = ""
        elif percent > 59 and percent < 70:
            icon = ""
        elif percent > 49 and percent < 60:
            icon = ""
        elif percent > 39 and percent < 50:
            icon = ""
        elif percent > 29 and percent < 40:
            icon = ""
        elif percent > 19 and percent < 30:
            icon = ""
        elif percent > 9 and percent < 20:
            icon = ""
        elif percent > 0 and percent < 10:
            icon = ""
    else:
        if percent == 100:
            icon = ""
        elif percent > 89 and percent < 100:
            icon = ""
        elif percent > 79 and percent < 90:
            icon = ""
        elif percent > 69 and percent < 80:
            icon = ""
        elif percent > 59 and percent < 70:
            icon = ""
        elif percent > 49 and percent < 60:
            icon = ""
        elif percent > 39 and percent < 50:
            icon = ""
        elif percent > 29 and percent < 40:
            icon = ""
        elif percent > 19 and percent < 30:
            icon = ""
        elif percent > 9 and percent < 20:
            icon = ""
        elif percent > 0 and percent < 10:
            icon = ""
    return str(percent) + "% " + icon + " "


mod = "mod4" # mod4 is Windows/Super key
terminal = guess_terminal()
user_home = os.path.expanduser("~")


keys = [
    # Switch between windows
    Key(
        [mod], "h",
        lazy.layout.left(),
        desc = "Move focus to left"
    ),
    Key(
        [mod], "l",
        lazy.layout.right(),
        desc = "Move focus to right"
    ),
    Key(
        [mod], "j",
        lazy.layout.down(),
        desc = "Move focus down"
    ),
    Key(
        [mod], "k",
        lazy.layout.up(),
        desc = "Move focus up"
    ),
    Key(
        [mod], "space",
        lazy.layout.next(),
        desc = "Move window focus to other window"
    ),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc = "Move window to the left"
    ),
    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc = "Move window to the right"
    ),
    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc = "Move window down"
    ),
    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc = "Move window up"
    ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        desc = "Grow window to the left"
    ),
    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        desc = "Grow window to the right"
    ),
    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        desc = "Grow window down"
    ),
    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        desc = "Grow window up"
    ),
    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc = "Reset all window sizes"
    ),

    # Toggle floating for active window.
    Key([mod, "shift"], "f",
        lazy.window.toggle_floating(),
        desc = "toggle floating"
    ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),
    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
    ),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),
    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
    ),

    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
    ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),
    Key([mod], "space",
        lazy.spawn("rofi -show drun"),
        desc="Open rofi as app menu."
    ),

    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10+")
    ),
    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10-")
    ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("pulsemixer  --change-volume +5")
    ),
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("pulsemixer  --change-volume -5")
    ),
    Key([], "XF86AudioMute",
        lazy.spawn("pulsemixer --toggle-mute")
    ),

    Key(["mod1"], "Shift_L",
        lazy.spawn("/usr/bin/bash /home/artin/main.sh")
    ),

    # Screenshots
    Key([], "Print",
        lazy.spawn("/usr/bin/escrotum " + user_home + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"),
        desc='Save screen to screenshots folder'
    ),

    # Capture region of screen or app
    Key([mod, "shift"], "Print",
        lazy.spawn("/usr/bin/escrotum -s " + user_home + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"),
        desc='Capture region of screen or app'
    ),

    # Capture region of screen or app to clipboard
    Key([mod, "control"], "Print",
        lazy.spawn("/usr/bin/escrotum -s -C " + user_home + "/Pictures/Screenshots/screenshot_%d_%m_%Y_%H_%M_%S.png"),
        desc='Capture region of screen or app to clipboard'
    ),

    Key([mod], "e",
        lazy.spawn("kitty -e nvim"),
        desc='Open NeoVim as text editor'
    ),
]

number_of_monitors = int(subprocess.getoutput("DISPLAY=:0 xrandr -q | grep ' connected' | wc -l"))
groups = [Group(i) for i in "1234567890"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name,
            lazy.group[i.name].toscreen(toggle=False),
            desc="Switch to group {}".format(i.name)
        ),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)
        ),
    ])


layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=8),
    layout.Max(),
    layout.Floating(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


wallpapers_list = os.listdir(user_home + "/Pictures/wallpapers")
wallpapers_list.remove("LICENSE")
wallpapers_list.remove("README.md")
wallpapers_list.remove(".git")


screens = [
    Screen(
        wallpaper="~/Pictures/wallpapers/{}".format(wallpapers_list[random.randint(0, len(wallpapers_list))]),
        wallpaper_mode = "fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    fmt=" ",
                    foreground="#42a5f5",
                    fontsize=14,
                    font="caskaydiacove nerd font",
                ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(
                    format="{name}",
                    parse_text=fix_firefox_name,
                ),
                widget.DF(
                    partition="/",
                    visible_on_warn=False,
                    format="{uf}{m}b  ",
                    font="caskaydiacove nerd font",
                    foreground="#ba68c8",
                    fontsize=14,
                ),
                widget.CPU(
                    format="{load_percent}% ﬙",
                    fontsize=14,
                    foreground="#ec407a",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e htop")}
                ),
                widget.Memory(
                    format="{memused: .0f}{mm}ib  ",
                    fontsize=14,
                    foreground="#fbc02d",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e htop")}
                ),
                widget.Net(
                    format="{down}  ",
                    fontsize=14,
                    foreground="#61c766",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e nmtui")}
                ),
                widget.PulseVolume(
                    update_interval=0.1,
                    foreground="#6c77bb",
                    font="caskaydiacove nerd font",
                    fontsize=14,
                ),
                widget.TextBox(
                    fmt=" ",
                    foreground="#6c77bb",
                    font="caskaydiacove nerd font",
                    fontsize=14,
                ),
                widget.CheckUpdates(
                    display_format="{updates}  ",
                    no_update_string="0  ",
                    fontsize=14,
                    update_interval=60,
                    custom_command='checkupdates',
                    # distro='Arch_yay',
                    colour_no_updates="#fdd835",
                    colour_have_updates="#fdd835",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("yay -Syyu --noconfirm")}
                ),
                # battery
                widget.GenPollText(
                    update_interval=1,
                    func=lambda: set_battery_icon(),
                    foreground="#ec7875",
                    fontsize=14,
                    font="caskaydiacove nerd font",
                ),
# setxkbmap -query | grep "layout:\s" | awk '{print $2}'
                # widget.genpolltext(
                #     update_interval=1,
                #     func=lambda: set_battery_icon(),
                #     foreground="#ec7875",
                #     fontsize=14,
                # ),
                widget.Clock(
                    format="%H:%M %p  ",
                    fontsize=14,
                    foreground="#42a5f5",
                    font="caskaydiacove nerd font",
                ),
                widget.Systray(),
            ],
            28,
            opacity=0.8,
            margin=3,
        ),
    ),
    Screen(
        wallpaper="~/Pictures/wallpapers/{}".format(wallpapers_list[random.randint(0, len(wallpapers_list))]),
        wallpaper_mode = "fill",
        top=bar.Bar(
            [
                widget.TextBox(
                    fmt=" ",
                    foreground="#42a5f5",
                    fontsize=14,
                    font="caskaydiacove nerd font",
                ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.Spacer(),
                widget.WindowName(
                    format="{name}",
                    parse_text=fix_firefox_name,
                ),
                widget.DF(
                    partition="/",
                    visible_on_warn=False,
                    format="{uf}{m}b  ",
                    font="caskaydiacove nerd font",
                    foreground="#ba68c8",
                    fontsize=14,
                ),
                widget.CPU(
                    format="{load_percent}% ﬙",
                    fontsize=14,
                    foreground="#ec407a",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e htop")}
                ),
                widget.Memory(
                    format="{memused: .0f}{mm}ib  ",
                    fontsize=14,
                    foreground="#fbc02d",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e htop")}
                ),
                widget.Net(
                    format="{down}  ",
                    fontsize=14,
                    foreground="#61c766",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("kitty -e nmtui")}
                ),
                widget.PulseVolume(
                    update_interval=0.1,
                    foreground="#6c77bb",
                    font="caskaydiacove nerd font",
                    fontsize=14,
                ),
                widget.TextBox(
                    fmt=" ",
                    foreground="#6c77bb",
                    font="caskaydiacove nerd font",
                    fontsize=14,
                ),
                widget.CheckUpdates(
                    display_format="{updates}  ",
                    no_update_string="0  ",
                    fontsize=14,
                    update_interval=60,
                    custom_command='checkupdates',
                    # distro='Arch_yay',
                    colour_no_updates="#fdd835",
                    colour_have_updates="#fdd835",
                    font="caskaydiacove nerd font",
                    mouse_callbacks = {"button1": lambda: qtile.cmd_spawn("yay -Syyu --noconfirm")}
                ),
                # battery
                widget.GenPollText(
                    update_interval=1,
                    func=lambda: set_battery_icon(),
                    foreground="#ec7875",
                    fontsize=14,
                    font="caskaydiacove nerd font",
                ),
# setxkbmap -query | grep "layout:\s" | awk '{print $2}'
                # widget.genpolltext(
                #     update_interval=1,
                #     func=lambda: set_battery_icon(),
                #     foreground="#ec7875",
                #     fontsize=14,
                # ),
                widget.Clock(
                    format="%H:%M %p  ",
                    fontsize=14,
                    foreground="#42a5f5",
                    font="caskaydiacove nerd font",
                ),
                widget.Systray(),
            ],
            28,
            opacity=0.8,
            margin=3,
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True
wmname = "qtile"
