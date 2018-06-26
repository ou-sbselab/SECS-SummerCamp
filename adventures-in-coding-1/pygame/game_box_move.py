## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## game_box_move.py

## Move the box around the screen
## Based on: https://nerdparadise.com/programming/pygame/part1

import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Run our loop until we hit the close button
done     = False
color    = (0, 128, 255)  # Start as blue
position = [30, 30]       # Start at x=30,y=30
clock    = pygame.time.Clock()
while not done:
  # Handle keys and events separately
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    # Make a random color when you hit the SPACE key
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  if keys[pygame.K_ESCAPE]:
    done = True
  if (keys[pygame.K_UP] and (position[1] >= 0)):
    position[1] -= 5
  if (keys[pygame.K_DOWN] and (position[1] <= (300 - 60))):
    position[1] += 5
  if (keys[pygame.K_LEFT] and (position[0] >= 0)):
    position[0] -= 5
  if (keys[pygame.K_RIGHT] and (position[0] <= (400 - 60))):
    position[0] += 5

  # Bounds checking for sanity's sake
  if (position[0] < 0): position[0] = 0
  if (position[0] > (400-60)): position[0] = 400-60
  if (position[1] < 0): position[1] = 0
  if (position[1] > (300-60)): position[1] = 300-60
  
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  # Clear the screen
  screen.fill((0,0,0))
  # Draw a square
  pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], 60, 60))

  # Flip --> make updates to screen visible
  pygame.display.flip()

  # Block execution to give us 60fps
  clock.tick(60)

