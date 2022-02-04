"""
This file is originally coded by yasserprogamer.

I coded this file to color console and terminal texts
and change cursor mode and other things.... 
"""

import random as rand
import version

class window:

    ConsoleTitle = ""

    def setTitle(title = f"{version.version} ({version.version})"):
        """
        Set or change console's title.

        For example:
        setTitle('Hello World')
        will change terminal's title to "Hello World".
        """
        window.ConsoleTitle = title
        return print(f"\033]2;{title}\x07", end="\r")

    def addToTitle(text = ""):
        return print(f"\033]2;{window.ConsoleTitle} - {text}\x07", end="\r")

    def restoreTitle():
        return print(f"\033]2;{window.ConsoleTitle}\x07", end="\r")


class Color:
    Underline = underline = UNDERLINE = '\033[4m'
    Nounderline = NOUNDERLINE = '\033[24m'
    Bold = Bright = bold = bright = '\033[1m'
    NoBold = NoBright = nobold = nobright = '\033[22m'
    White = white = '\033[38;2;255;255;255m'
    Black = black = '\033[38;2;00;00;00m'
    Red = red = '\033[38;2;255;00;00m'#[91m
    Yellow = yellow = '\033[38;2;255;255;00m'
    Gold = gold = '\033[38;2;255;215;00m'
    Cyan = cyan = '\033[38;2;00;255;255m'
    Lime = Green = LightGreen = '\033[38;2;00;255;00m'
    Blue = blue = '\033[38;2;00;00;255m'
    purple = Purple = PURPLE = '\033[38;2;128;00;128m'
    orange = Orange = ORANGE = '\033[38;2;255;165;00m'
    def RandomRGBGenerator():
        r = rand.randint(0, 255)
        g = rand.randint(0, 255)
        b = rand.randint(0, 255)
        result = str(r)+';'+str(g)+';'+str(b)
        return result
    random = RANDOM = Random =  '\033[38;2;'+RandomRGBGenerator()+'m'
    reset = '\033[39m'

class Cursor:
    visible = '\033[?25h'
    hidden = '\033[?25l'

class Lines:
    def delete(number = 0):
        return f'\033[{number}M'