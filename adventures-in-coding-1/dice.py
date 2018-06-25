## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## dice.py

## This program demonstrates how to do a random die roll.  We will contrast this with
## dice_seed.py and dice_guesser.py.

import random

roll_1 = random.randint(1,6)  # Pick a random number between 1 and 6
print roll_1                  # Print that random number
print "--------------"

# Now, roll 10 die
for i in xrange(1,11):
  print "Roll %d: %d" % (i, random.randint(1,6))
