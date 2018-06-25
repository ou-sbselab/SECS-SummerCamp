## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_letters.py

## Show single characters and the sleep command!
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Define the colors we want to show
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
white = (255, 255, 255)

sense.show_letter("O", red)
sleep(1)
sense.show_letter("U", red)
sleep(1)
sense.show_letter("-", green)
sleep(1)
sense.show_letter("S", blue)
sleep(1)
sense.show_letter("E", blue)
sleep(1)
sense.show_letter("C", blue)
sleep(1)
sense.show_letter("S", blue)
sleep(1)
