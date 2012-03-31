#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import re
import sys

# Set up a default color dict.
COLOR_DICT = {
    'f_black': "",
    'b_black': "",
    'f_red': "",
    'b_red': "",
    'f_green': "",
    'b_green': "",
    'f_yellow': "",
    'b_yellow': "",
    'f_blue': "",
    'b_blue': "",
    'f_magenta': "",
    'b_magenta': "",
    'f_cyan': "",
    'b_cyan': "",
    'f_white': "",
    'b_white': "",
    'f_reset': "",
    'b_reset': "",
    # Style Constants
    's_dim': "",
    's_normal': "",
    's_bright': "",
    's_reset_all': "",
}

try:
    from colorama import Fore, Back, Style, init, deinit
    HAS_COLORS = sys.stdout.isatty()
    COLOR_DICT = {
        # Foreground & Background ANSI Color Constants
        'f_black': Fore.BLACK,
        'b_black': Back.BLACK,
        'f_red': Fore.RED,
        'b_red': Back.RED,
        'f_green': Fore.GREEN,
        'b_green': Back.GREEN,
        'f_yellow': Fore.YELLOW,
        'b_yellow': Back.YELLOW,
        'f_blue': Fore.BLUE,
        'b_blue': Back.BLUE,
        'f_magenta': Fore.MAGENTA,
        'b_magenta': Back.MAGENTA,
        'f_cyan': Fore.CYAN,
        'b_cyan': Back.CYAN,
        'f_white': Fore.WHITE,
        'b_white': Back.WHITE,
        'f_reset': Fore.RESET,
        'b_reset': Back.RESET,
        # Style Constants
        's_dim': Style.DIM,
        's_normal': Style.NORMAL,
        's_bright': Style.BRIGHT,
        's_reset_all': Style.RESET_ALL,
    }
except ImportError:
    HAS_COLORS = False

# Setup function to strip ANSI sequences for centering

strip_ANSI_sub = re.compile(r"""
    \x1b     # literal ESC
    \[       # literal [
    [;\d]*   # zero or more digits or semicolons
    [A-Za-z] # a letter
    """, re.VERBOSE).sub

def strip_ANSI(s):
    return strip_ANSI_sub("", s)

def center(string, width):
    center_string = []
    for line in string.split("\n"):
        strip_line = strip_ANSI(line)
        lefts, rights = "", ""
        left_right = True
        while len(strip_line) < width:
            if left_right:
                strip_line = " " + strip_line
                lefts += " "
            else:
                strip_line += " "
                rights += " "
            left_right = not left_right
        center_string.append("".join([lefts, line, rights]))
    return '\n'.join(center_string)

