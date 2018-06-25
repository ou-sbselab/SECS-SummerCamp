## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## stem_adventure.py

## The purpose of this program is to pull together all the concepts from Day 1, including
## loops, lists, user input, decisions, etc.  Here, the user will navigate a 4x3 'dungeon'
## searching for the amulet of STEM.

####################################################
#                                                  #
#     Retrieve the fabled amulet of STEM           #
#                                                  #
####################################################

import random

# Index   0   1   2   3
rooms = [[1,  2,  3,  4],   # 0 
         [5,  6,  7,  8],   # 1
         [9,  10, 11, 12]]  # 2

# The player starts at [0][0]
current_row = 0
current_column = 0

# Pick a random room to hide the amulet
row_index = random.randint(0,3)
column_index = random.randint(0,3)
# The player starts at [0][0], so we need to pick a different room.
while ((row_index == 0) and (column_index == 0)):
  row_index = random.randint(0,3)
  column_index = random.randint(0,3)

# Our main game loop
done = False
while not done:
  print "You are in Room %s" % rooms[current_row][current_column]

  movement = raw_input("Direction: ")
  if (movement == 'k'):   # move up
    if (current_row >= 1):
      current_row -= 1
      
  elif (movement == 'j'): # move down
    if (current_row < 2):
      current_row += 1
      
  elif (movement == 'h'):   # move left
    if (current_column >= 1):
      current_column -= 1
      
  elif (movement == 'l'): # move right
    if (current_column < 3):
      current_column += 1

  # Check if we found the amulet
  if ((current_row == row_index) and (current_column == column_index)):
    print "You've discovered the amulet and saved the day!"
    done = True
  #else:
  #  print column_index, current_column, "::", row_index, current_row
  print "===================================\n"

