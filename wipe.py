import board
import time
from neopixel import NeoPixel

np = NeoPixel(board.D2, 30, auto_write=False, brightness=1)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (106, 49, 81)
orange = (255, 60, 0)
purple = (128, 0, 128)
black= (0,0,0)
white = (255,255,255)

color_list  = [red, yellow, green, cyan, blue, purple]

def wipe(wipe_color, speed):
     for i in range(np.n):
         np[i] = (wipe_color)
         np.show()
         time.sleep(speed)
     
while True:
    wipe(red, 0.5)
