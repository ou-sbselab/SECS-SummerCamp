# Oakland University - SECS Summer Camp (Programming Gadgets)
### Erik Fredericks -- Summer, 2018

This series of Python scripts demonstrates the concepts used throughout Programming Gadgets, a module where participants are taught how to both program in Python on the Raspberry Pi.  

For each file, a bulleted list of key concepts is presented.

Note that you don't necessarily need the Sense hat to run these.  If a program requires it, you can use the built-in Sense hat emulator on Raspbian simply by replacing `from sense_hat import SenseHat` with `from sense_emu import SenseHat`.

### hello-web.py

* Hello world of Flask (web server)

### maze.py

* A marble maze game on the Sense hat's LED matrix, controlled by the accelerometer

### sense_acceleration.py

* Detecting a shaking motion and making the Pi angry when doing so

### sense_joystick.py

* Interacting with the joystick (Sense hat)

### sense_orientation.py

* Basic orientation detection (Sense hat)

### sense_sensors.py

* Using the various sensors (temperature, pressure, humidity, etc.) (Sense hat)

### stem-adventure-joystick.py

* Using the STEM adventure game from Adventures in Coding 1, the game is translated to be on the LED matrix, controllable by the joystick.

### weather.py

* Flask application for serving Sense hat sensor data on a webpage

### templates/

* Templates folder that holds the Flask (Jinja) templates -- specifically just the weather.html page.
