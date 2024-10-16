import board
from neopixel import NeoPixel
import time
import random

np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)
i = 0

red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
purple = (255, 127,0)
orange = (255, 64, 0)

def pickachu(bg,fg,p3,p4)
    np.fill((bg))
    np.show()
    for i in range(p2):
        np[i] = random.randint(0, np.n - 2)] = p3
        np.show()
        time.sleep(p4)

while True:
    pickachu(
