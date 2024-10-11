import board
import time
from neopixel import NeoPixel


np = NeoPixel(board.D2, 30, auto_write=False, brightness=0.3)


red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
purple = (255, 127,0)
orange = (255, 64, 0)

def fade_in(color):
    red_ratio = color[0] / 50
    red_orig = color[0]
    green_ratio = color[1] / 50
    green_orig = color[1]
    blue_ratio = color[2] / 50
    blue_orig = color[2]
    for i in range(1,51):
     red = red_orig + i * red_ratio
     green = green_orig + i * green_ratio
     blue = blue_orig + i * blue_ratio
     np.fill((red, green, blue))
     np.show()
     time.sleep(.05)
    
    

def fadeout(color):
    red_ratio = color[0] / 50
    red_orig = color[0]
    green_ratio = color[1] / 50
    green_orig = color[1]
    blue_ratio = color[2] / 50
    blue_orig = color[2]
    for i in range(1,51):
     red = red_orig - i * red_ratio
     green = green_orig - i * green_ratio
     blue = blue_orig - i * blue_ratio
     np.fill((red,green,blue))
     np.show()
     time.sleep(.05)
