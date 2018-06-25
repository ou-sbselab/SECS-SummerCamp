## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## dice-trace.py

## This file is used to demonstrate trace debugging.  We have an issue with our dice roll
## generator and need to figure out where the issue is...

## Since we have print statements everywhere, we basically already were trace debugging.  For the
## demo, all prints will be deleted and re-added (this file shows the final code).
import random

roll_1 = random.randint(1,6)  # Pick a random number between 1 and 6
print roll_1                  # Print that random number
print "--------------"

# Now, roll 10 die
for i in xrange(1,11):
  print "Roll %d: %d" % (i, random.randint(1,7))
