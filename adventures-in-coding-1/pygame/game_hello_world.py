## OU SECS Summer Camp
## Adventures in Coding 1
## Summer 2018
## Erik Fredericks
## game_hello_world.py

## The HELLO WORLD of video games -- showing a screen!
## Based on: https://nerdparadise.com/programming/pygame/part1

import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))

# Run our loop until we hit the close button
done = False
while not done:
  # Check for events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True

  # Draw a square
  pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))

  # Flip --> make updates to screen visible
  pygame.display.flip()

