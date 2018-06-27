## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## sense_sensors.py

## This file senses the environment with a few various sensors.
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

# Sense barometric pressure first (millibars)
pressure = sense.get_pressure()
print "Pressure: [%f]" % pressure

# And temp (celsius)
temperature = sense.get_temperature()
print "Temperature (C): [%f]" % temperature
print "Temperature (F): [%f]" % (temperature * (9.0 / 5.0) + 32.0)

# And then humidity (percent)
humidity = sense.get_humidity()
print "Humidity: [%f]" % humidity

# Show on the LED display
# First round the numbers so they're easily readable
t = round(temperature, 1)
p = round(pressure, 1)
h = round(humidity, 1)

# Put it all together and show
message = "Temp: [%.1f] Pressure: [%.1f] Humidity: [%.1f]" % (t,p,h)
sense.show_message(message, scroll_speed=0.15)
