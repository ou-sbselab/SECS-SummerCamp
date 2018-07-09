## OU SECS Summer Camp
## Programming gadgets
## Summer 2018
## Erik Fredericks
## stem_adventure-joystick.py

## We're going to gadget-up the STEM adventure game from 
## the Adventures in Coding 1 module.

####################################################
#                                                  #
#     Retrieve the fabled amulet of STEM           #
#                                                  #
####################################################

import random
import time
from sense_hat import SenseHat, ACTION_RELEASED

# Create the SenseHat object
sense = SenseHat()

# Index   0   1   2   3
rooms = [[1,  2,  3,  4],   # 0 
         [5,  6,  7,  8],   # 1
         [9,  10, 11, 12]]  # 2

# Color constants
r = (255, 0, 0)
g = (0, 255, 0)
x = (0, 0, 0)

# Draw the map to the Sense Hat
def draw_map(sense, curr_row, curr_col):
  sense.clear()
  dungeon = [[r, r, r, r, r, r, r, r],
             [r, r, r, r, r, r, r, r],
             [r, r, r, r, r, r, r, r],
             [r, r, x, x, x, x, r, r],
             [r, r, x, x, x, x, r, r],
             [r, r, x, x, x, x, r, r],
             [r, r, r, r, r, r, r, r],
             [r, r, r, r, r, r, r, r]]

  # Offsets because we're not drawing to [0][0]
  row_offset = 3
  col_offset = 2
  dungeon[curr_row + row_offset][curr_col + col_offset] = g
  sense.set_pixels(sum(dungeon,[]))


if __name__ == '__main__':
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
    draw_map(sense, current_row, current_column) # Draw the map to the Hat
    joy_pressed = False


    # Wait for the user to press something, otherwise the above while loop will just keep looping
    while not joy_pressed:
      # Check if the user pressed the joystick
      for event in sense.stick.get_events():
        if event.direction == 'middle':  # Pressed middle
          joy_pressed = True
          done = True
          sense.show_message("YOU ESCAPED WITHOUT THE AMULET :(")
        elif event.direction == 'up' and event.action != ACTION_RELEASED:    # Pressed UP
          #sense.show_message("UP")
          if (current_row >= 1):
            joy_pressed = True
            current_row -= 1
        elif event.direction == 'down' and event.action != ACTION_RELEASED:  # Pressed DOWN
          #sense.show_message("DOWN")
          if (current_row < 2):
            joy_pressed = True
            current_row += 1
        elif event.direction == 'left' and event.action != ACTION_RELEASED:  # Pressed LEFT
          #sense.show_message("LEFT")
          if (current_column >= 1):
            joy_pressed = True
            current_column -= 1
        elif event.direction == 'right' and event.action != ACTION_RELEASED: # Pressed RIGHT
          #sense.show_message("RIGHT")
          if (current_column < 3):
            joy_pressed = True
            current_column += 1


    """ --> This is the old keyboard code.  Left in for posterity
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
    """

    # Check if we found the amulet
    if ((current_row == row_index) and (current_column == column_index)):
      print "You've discovered the amulet and saved the day!"
      done = True

      # Animate a win screen
      for i in range(8):
        for j in range(8):
          sense.set_pixel(i, j, (0,0,255))
          time.sleep(0.02)
      sense.show_message("You've discovered the amulet and saved the day!")


    #else:
    #  print column_index, current_column, "::", row_index, current_row
    print "===================================\n"
