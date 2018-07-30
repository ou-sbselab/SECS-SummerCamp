## OU SECS Summer Camp
## Programming Gadgets
## Summer 2018
## Erik Fredericks
## sense_joystick.py

## This file senses the joystick
from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep
import random

sense = SenseHat()

# Define the colors we want to show
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
white = (255, 255, 255)

# First, clear the screen
sense.clear()

# Run until the middle is pushed
done = False
while not done:

  # A joystick push will end this
  for event in sense.stick.get_events():
    if event.direction == 'middle' and event.action != ACTION_RELEASED:
      done = True
      sense.show_message('ALL DONE')
    elif event.direction == 'up' and event.action != ACTION_RELEASED:
      sense.show_message('UP')
    elif event.direction == 'down' and event.action != ACTION_RELEASED:
      sense.show_message('DOWN')
    elif event.direction == 'left' and event.action != ACTION_RELEASED:
      sense.show_message('LEFT')
    elif event.direction == 'right' and event.action != ACTION_RELEASED:
      sense.show_message('RIGHT')
