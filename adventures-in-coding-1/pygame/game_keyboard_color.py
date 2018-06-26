## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## game_keyboard_color.py

## Handling a KEYDOWN event
## Based on: https://nerdparadise.com/programming/pygame/part1

import pygame
import random
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Run our loop until we hit the close button
done = False
color = (0, 128, 255)
while not done:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

    # Make a random color when you hit the SPACE key
    if (event.type == pygame.KEYUP):
      if (event.key == pygame.K_SPACE):
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
      elif (event.key == pygame.K_ESCAPE):
        done = True

  # Draw a square
  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

  # Flip --> make updates to screen visible
  pygame.display.flip()

