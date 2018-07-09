## OU SECS Summer Camp
## Programming Gadgets
## Summer 2018
## Erik Fredericks
## sense_orientation.py

from sense_hat import SenseHat
import time
sense = SenseHat()


while True:
  orient = sense.get_orientation()
  pitch  = orient['pitch']
  roll   = orient['roll']
  yaw    = orient['yaw']
  print "pitch [%f] roll [%f] yaw [%f]" % (pitch, roll, yaw)

  time.sleep(0.1)
