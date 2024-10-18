import random
import time
import board
from digitalio import DigitalInOut, Direction

#Initialization
red = DigitalInOut(board.D2)
red.direction = Direction.OUTPUT
blue = DigitalInOut(board.D3)
blue.direction = Direction.OUTPUT
yellow = DigitalInOut(board.D4)
yellow.direction = Direction.OUTPUT
white = DigitalInOut(board.D5)
white.direction = Direction.OUTPUT

white = DigitalInOut(board.D6)
green = DigitalInOut(board.D7)
yellow = DigitalInOut(board.D8)
blue = DigitalInOut(board.D9)
red= DigitalInOut(board.D11)

white.direction = Direction.INPUT
green.direction = Direction.INPUT
yellow.direction = Direction.INPUT
blue.direction = Direction.INPUT
red.direction = Direction.INPUT

my_list = []
game = []

def add_to_sequence(list):
    list.append(random.randint(0,3))

def display_sequence(my_trip):
    p = " "
    for x in my_trip:
        if x == 0:
            p = "Red"
            red.value = not red.value
            time.sleep(.3)
            red.value = not red.value
        elif x == 1:
            p = "Green"
            green.value = not green.value
            time.sleep(.3)
            green.value = not green.value
            time.sleep(.3)
        elif x == 2:
            p = "Yellow"
            yellow.value = not yellow.value
            time.sleep(.3)
            yellow.value = not yellow.value
            time.sleep(.3)
        else:
            p = "Blue"
            blue.value = not blue.value
            time.sleep(.3)
            blue.value = not blue.value
            time.sleep(.3)



# main / infinite loop
def try_sequence(inputlist):
    user = " "
    for x in my_list:
        if x == 0:
            p = "Red"
            red.value = not red.value
            time.sleep(.3)
            red.value = not red.value
        elif x == 1:
            p = "Green"
            green.value = not green.value
            time.sleep(.3)
            green.value = not green.value
            time.sleep(.3)
        elif x == 2:
            p = "Yellow"
            yellow.value = not yellow.value
            time.sleep(.3)
            yellow.value = not yellow.value
            time.sleep(.3)
        else:
            p = "Blue"
            blue.value = not blue.value
            time.sleep(.3)
            blue.value = not blue.value
            time.sleep(.3)
while True:
    if white.value:
        display_sequence(my_list)
        time.sleep(.3)      
    if blue.value:
        time.sleep(.3)
        add_to_sequence(my_list)
    if green.value:
        time.sleep(.3)
        add_to_sequence(my_list)        
    if yellow.value:
        time.sleep(.3)
        add_to_sequence(my_list)        
    if red.value:
        time.sleep(.3)
        add_to_sequence(my_list)        
    if blue.value:
         time.sleep(.3)
        add_to_sequence(my_list)  
