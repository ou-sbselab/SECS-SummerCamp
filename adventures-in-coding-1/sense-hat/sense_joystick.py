## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_joystick.py

## This file senses the joystick
from sense_hat import SenseHat
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

# Run until shaken
done = False
while not done:

  # A joystick push will end this
  for event in sense.stick.get_events():
    if event.direction == 'middle':
      done = True
      sense.show_message('ALL DONE')
    elif event.direction == 'up':
      sense.show_message('UP')
    elif event.direction == 'down':
      sense.show_message('DOWN')
    elif event.direction == 'left':
      sense.show_message('LEFT')
    elif event.direction == 'right':
      sense.show_message('RIGHT')
