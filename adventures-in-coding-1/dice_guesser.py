## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## dice_guesser.py

# This program builds on the dice rolling program but incorporates a guessing game.
# The user inputs the number of dice to roll (and we assume it is a valid number)
# and then will tell you if your guess is too high or too low.

import random

# Get the number of dice to roll:
num_dice = int(raw_input("Enter the number of dice to roll: "))
print "===================================" 

# Calculate the target value
total_value = 0
for i in xrange(0,num_dice):
  die_roll = random.randint(1,6)
  total_value += die_roll

# Run the game until we get it right
done = False
number_of_guesses = 0
while not done:
  guess = int(raw_input("Enter your guess: "))
  number_of_guesses += 1  # Increment the number of guesses

  # Check the guess
  if (guess == total_value):
    print "Good job!  It took you %d guesses!" % number_of_guesses
    done = True
  elif (guess > total_value):
    print "Too high!"
  else:
    print "Too low!"
  

  
  
  
