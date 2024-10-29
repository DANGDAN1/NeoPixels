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
orange = (255, 30, 0)
color_list = [red, green, blue, yellow, cyan, magenta, purple, orange]

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
     
fade_in(orange)

def fire(bckgr,flicker,flicker2,speed,tim1):
    np.fill(bckgr)
    np.show()
    for i in range(tim1):
        np[random.randint(0,np.n-2)] = flicker
        np.show()
        time.sleep(speed)
        np[random.randint(0,np.n-2)] = flicker2
        np.show()
        time.sleep(speed)
        

fire((255,64,0),(255, 0, 0), (255, 55, 0),0.03,10)

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

fadeout(orange)

def lightning(color):
    np.fill(color)
    np.show()
    time.sleep(random.randint(3,5))
    for i in range(random.randint(4,5)):
        np.fill((255,255,255))
        np.show()
        time.sleep(random.randint(3,5)/100)
        np.fill(color)
        np.show()
        time.sleep(random.randint(3,5)/100)
        
lightning((0, 255, 255))


