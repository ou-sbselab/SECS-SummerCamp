## OU SECS Summer Camp
## Programming Gadgets
## Summer 2018
## Erik Fredericks
## maze.py

## Marble maze game on the Sense hat's LED matrix using the gyroscope

# Based on a tutorial from:
# https://projects.raspberrypi.org/en/projects/sense-hat-marble-maze

from sense_hat import SenseHat
from time import sleep

def move(pitch, roll, x, y, level):
  new_x = x
  new_y = y

  if (1 < pitch < 179) and (x != 0):
    new_x -= 1
  if (181 < pitch < 359) and (x != 7):
    new_x += 1

  if (1 < roll < 179) and (y != 7):
    new_y += 1
  if (179 < roll < 359) and (y != 0):
    new_y -= 1

  new_x,new_y = check_wall(x,y,new_x,new_y, level)
  return new_x, new_y

def check_wall(x, y, new_x, new_y, level):
  if level[new_y][new_x] != r:
    return new_x, new_y
  elif level[new_y][x] != r:
    return x, new_y
  elif level[y][new_x] != r:
    return new_x, y
  else:
    return x,y


sh = SenseHat()
sh.clear()

# Colors 
r = (255, 0, 0)    # Red
g = (0, 255, 0)    # Green
b = (0, 0, 255)    # Blue
o = (135, 113, 72) # OU Gold
k = (0, 0, 0)      # Blank

x = 1
y = 1

## Create our mazes -- 8x8
levels = [
           ## Level 1
           [[r, r, r, r, r, r, r, r],
            [r, k, k, k, k, k, k, r],
            [r, r, r, k, r, k, k, r],
            [r, k, r, k, r, r, r, r],
            [r, k, k, k, k, k, k, r],
            [r, k, r, r, r, r, k, r],
            [r, k, g, r, k, k, k, r],
            [r, r, r, r, r, r, r, r]],

           ## Level 2
           [[r, r, r, r, r, r, r, r],
            [r, k, k, k, k, k, k, r],
            [r, k, k, k, k, k, k, r],
            [r, k, k, k, k, k, k, r],
            [r, k, k, k, g, k, k, r],
            [r, k, k, k, k, k, k, r],
            [r, k, k, k, k, k, k, r],
            [r, r, r, r, r, r, r, r]],

           ## Level 3
           [[r, r, r, r, r, r, r, r],
            [r, k, k, k, k, k, k, r],
            [r, r, r, r, k, k, k, r],
            [r, r, k, r, r, k, r, r],
            [r, r, k, r, r, k, r, r],
            [r, r, r, r, r, g, r, r],
            [r, k, k, k, r, r, r, r],
            [r, r, r, r, r, r, r, r]]]
 
sh.show_message("L1")

curr_level = 0
done = False
while not done:
  level = levels[curr_level]

  orientation = sh.get_orientation()
  pitch       = orientation['pitch']
  roll        = orientation['roll']
  x, y        = move(pitch, roll, x, y, level)

  if (level[y][x] == g):
    curr_level += 1
    if (curr_level >= 3): 
      done = True
      sh.show_message("W")
      sh.clear()
    else:
      sh.show_message("L%d" % int(curr_level+1))
      sh.clear()
      x = 1
      y = 1
  else:
    level[y][x] = o

    sleep(0.15)

    # Flatten the maze
    sh.set_pixels(sum(level, []))

    level[y][x] = k





