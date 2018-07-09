## OU SECS Summer Camp
## Programming Gadgets
## Summer 2018
## Erik Fredericks
## weather.py

## Flask application that shows the weather via a templated website.
from flask import Flask
from flask import render_template
from sense_hat import SenseHat

app = Flask(__name__)
sense = SenseHat()

@app.route('/')
@app.route('/<name>')
def weather(name=None):
  pressure = sense.get_pressure()
  temperature = sense.get_temperature()
  humidity = sense.get_humidity()

  return render_template('weather.html', name=name, \
                                         pressure=pressure, \
                                         temperature=temperature, \
                                         humidity=humidity)
