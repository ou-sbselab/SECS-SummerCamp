## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## dice_seed.py

## This file demonstrates the purpose of a random seed.  It is basically the same as
## dice.py, except we introduce a seed value.
import random

# Seed the random fucntion
random.seed(1)

# Do the die rolls as we did in dice.py
roll_1 = random.randint(1,6)
print roll_1
print "--------------"

for i in xrange(1,11):
  print "Roll %d: %d" % (i, random.randint(1,6))
