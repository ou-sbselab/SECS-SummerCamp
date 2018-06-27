## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_acceleration.py

## This file senses the Pi being shaken.  Don't shake the Pi.
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
  # Get acceleration
  acceleration = sense.get_accelerometer_raw()
  x = abs(acceleration['x'])
  y = abs(acceleration['y'])
  z = abs(acceleration['z'])

  # If any are greater than 1, we've shaken the Pi
  if ((x > 1) or (y > 1) or (z > 1)):
    sense.show_letter("!", red) 
  else:
    sense.clear()

  # A joystick push will end this
  for event in sense.stick.get_events():
    if event.direction == 'middle':
      done = True
      sense.show_message('o_o')
