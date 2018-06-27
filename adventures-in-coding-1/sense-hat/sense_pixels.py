## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_letters.py

## Let's play with pixels (based on projects.raspberrypi.org)
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

# Set our demo pixels
sense.set_pixel(0, 2, blue)
sense.set_pixel(7, 4, red)

sleep(5)

# Clear the screen again
sense.clear()

for i in range(0,50000):
  row = random.randint(0,7) # random row index
  col = random.randint(0,7) # random column index
  
  # pick a random color
  color = (random.randint(0,255),
           random.randint(0,255),
           random.randint(0,255))

  sense.set_pixel(row, col, color)

sense.clear()
