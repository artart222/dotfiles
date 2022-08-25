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
import json


def find_theme():
    """Find system global theme from config.json file"""
    with open(
        f"{os.path.abspath(os.path.expanduser('~'))}/.config/qtile/config.json",
        "r",
        encoding="utf-8",
    ) as inp_file:
        configs = json.load(inp_file)
        return configs["theme"]


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
    "catppuccin": {
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
