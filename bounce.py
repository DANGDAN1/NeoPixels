import board
import time
from neopixel import NeoPixel
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)

i=0

red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
purple = (255, 127,0)
orange = (255, 64, 0)
color_list = [red, green, blue, yellow, cyan, magenta, purple, orange]


def bounce():
    for i in range(np.n):
        np.fill(black)
        np.show()
        np.
