## OU SECS Summer Camp
## Adventures in Coding 2
## Summer 2018
## Erik Fredericks
## breakout-levels.py

## The full game plus sane paddle collisions and multiple levels.

# Based on a tutorial from:
# http://codentronix.com/2011/04/14/game-programming-with-python-and-pygame-making-breakout/

import pygame, sys

### CONSTANTS 
SCREEN_W = 640
SCREEN_H = 480
# Bricks
BRICK_W = 60
BRICK_H = 15
# Paddle
PADDLE_W = 60
PADDLE_H = 12
# Ball
BALL_DIAMETER = 16
BALL_RADIUS   = int(BALL_DIAMETER / 2)  # keep for easy lookup
# Keep track of maximum locations
MAX_PADDLE_X  = SCREEN_W - PADDLE_W
MAX_BALL_X    = SCREEN_W - BALL_DIAMETER
MAX_BALL_Y    = SCREEN_H - BALL_DIAMETER
# Paddle Y coordinates
PADDLE_Y      = SCREEN_H - PADDLE_H - 10
# Colors
BLACK = (0,0,0)
GRAY  = (102,102,102)  
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
GOLD  = (135,113,72)   
# Game states
S_BALL_IN_PADDLE = 0
S_PLAYING        = 1
S_WON            = 2
S_GAME_OVER      = 3

### GAME CLASS
class OUBreakout(object):
  # Initialize game
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("OU Breakout")
    self.clock = pygame.time.Clock()
    self.level = 1

    if pygame.font:
      self.font = pygame.font.Font(None, 30)
    else:
      self.font = None

    self.initialize_game()

  # Setup the game variables
  def initialize_game(self):
    self.lives = 3
    self.score = 0
    self.state = S_BALL_IN_PADDLE

    self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_W, PADDLE_H)
    self.ball   = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)
    self.ball_velocity = [5, -5]

    self.create_bricks()

  # Create brick locations based on current level.
  # Level 1: Fill
  # Levels 2 and 3: Array fill
  def create_bricks(self):
    self.bricks = []

    if self.level == 1:  # Same fill as breakout.py
      y_ofs = 35
      for i in range(7):
        x_ofs = 35
        for j in range(8):
          self.bricks.append((pygame.Rect(x_ofs,y_ofs,BRICK_W,BRICK_H),GOLD))
          x_ofs += BRICK_W + 10
        y_ofs += BRICK_H + 5

    # x = no brick, G = gold brick, B = blue brick
    elif self.level == 2:
      self.brick_layout = [['x','x','x','x','x','x','x','x'],
                           ['x','G','G','G','x','x','x','x'],
                           ['x','G','x','G','x','G','x','G'],
                           ['x','G','x','G','x','G','x','G'],
                           ['x','G','x','G','x','G','x','G'],
                           ['x','G','G','G','x','G','x','G'],
                           ['x','x','x','x','x','G','G','G']]
    # x = no brick, G = gold brick, B = blue brick
    elif self.level == 3:
      self.brick_layout = [['x','x','x','x','x','x','x','x'],
                           ['x','B','B','B','B','B','B','x'],
                           ['x','x','x','x','x','x','G','x'],
                           ['x','B','B','B','B','B','B','x'],
                           ['x','G','x','x','x','x','x','x'],
                           ['x','B','B','B','B','B','B','x'],
                           ['x','x','x','x','x','x','x','x']]
    else: # error check to demonstrate level breaking
      print("An error occurred!")

    # Setup bricks if not the full fill
    # A better way to do this would be to have a single method for designing a level
    # but this shows two separate ways.
    if self.level == 2 or self.level == 3:
      y_ofs = 35
      self.bricks = []
      for i in range(7):
        x_ofs = 35
        for j in range(8):
          if self.brick_layout[i][j] == "G":
            self.bricks.append((pygame.Rect(x_ofs,y_ofs,BRICK_W,BRICK_H),GOLD))
          elif self.brick_layout[i][j] == "B":
            self.bricks.append((pygame.Rect(x_ofs,y_ofs,BRICK_W,BRICK_H),BLUE))
          x_ofs += BRICK_W + 10
        y_ofs += BRICK_H + 5
     
  # Handle user input
  def check_input(self):
    keys = pygame.key.get_pressed()

    # Quit
    if keys[pygame.K_ESCAPE]:
      sys.exit()

    # Move paddle left
    if keys[pygame.K_LEFT]:
      self.paddle.left -= 5
      if self.paddle.left < 0:
        self.paddle.left = 0

    # Move paddle right 
    if keys[pygame.K_RIGHT]:
      self.paddle.left += 5
      if self.paddle.left > MAX_PADDLE_X:
        self.paddle.left = MAX_PADDLE_X
    
    # Launch the ball
    if keys[pygame.K_SPACE] and self.state == S_BALL_IN_PADDLE:
      self.ball_velocity = [5, -5]
      self.state = S_PLAYING

    # Restart the game
    elif keys[pygame.K_RETURN] and (self.state == S_GAME_OVER or self.state == S_WON):
      self.level = 1
      self.initialize_game()

  # Move the ball within the screen
  def move_ball(self):
    self.ball.left += self.ball_velocity[0]
    self.ball.top  += self.ball_velocity[1]
  
    # Check bounds
    if self.ball.left <= 0:
      self.ball.left = 0
      self.ball_velocity[0] = -self.ball_velocity[0]
    elif self.ball.left >= MAX_BALL_X:
      self.ball.left = MAX_BALL_X
      self.ball_velocity[0] = -self.ball_velocity[0]

    if self.ball.top < 0:
      self.ball.top = 0
      self.ball_velocity[1] = -self.ball_velocity[1]

  # Collide with the bricks and paddle
  def handle_collisions(self):
    for brick in self.bricks:
      if self.ball.colliderect(brick[0]):
        self.score += 3
        self.ball_velocity[1] = -self.ball_velocity[1]
        self.bricks.remove(brick)
        break

    # Check if we have to update the level or let the player win
    if len(self.bricks) == 0 and self.level == 3:
      self.state = S_WON
    elif len(self.bricks) == 0 and self.level < 3:
      self.level += 1
      self.initialize_game()

    # Paddle collision
    if self.ball.colliderect(self.paddle):
      self.ball.top = PADDLE_Y - BALL_DIAMETER

      # Change Y-direction
      self.ball_velocity[1] = -self.ball_velocity[1]

      # Change X-direction if:
      # * Ball is moving right and it hits less than the halfway point
      # * Ball is moving left and hits beyond halfway point
      if ((self.ball_velocity[0] > 0) and ((self.ball.left+BALL_RADIUS) < self.paddle.left + (PADDLE_W / 2))) or \
         ((self.ball_velocity[0] < 0) and ((self.ball.left+BALL_RADIUS) >= self.paddle.left + (PADDLE_W / 2))): 
        self.ball_velocity[0] = -self.ball_velocity[0]

    # Oops, player missed the ball
    elif self.ball.top > self.paddle.top:
      self.lives -= 1
      if self.lives > 0:
        self.state = S_BALL_IN_PADDLE
      else:
        self.state = S_GAME_OVER

  # Draw stats to screen 
  def show_stats(self):
    if self.font:
      font_surface = self.font.render("SCORE: %d LIVES: %d LEVEL: %d" % (self.score, self.lives, self.level), False, WHITE)
      self.screen.blit(font_surface, (205,5))

  # Show the player a message
  def show_message(self,message):
    if self.font:
      size = self.font.size(message)
      font_surface = self.font.render(message, False, WHITE)
      x = (SCREEN_W - size[0]) / 2
      y = (SCREEN_H - size[1]) / 2
      self.screen.blit(font_surface, (x,y))

  # Draw whatever is in our bricks list
  def draw_bricks(self):
    for brick in self.bricks:
      pygame.draw.rect(self.screen, brick[1], brick[0])  # brick[0] = Rect, brick[1] = Color

  # Main game function
  def run(self):
    while True:  # Our forever loop
  
      # Handle clicking the 'X'
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      # Lock to 60 fps and redraw
      self.clock.tick(60)
      self.screen.fill(BLACK)

      # Handle user input
      self.check_input()

      # Game state machine
      if self.state == S_PLAYING: # ball in play
        self.move_ball()
        self.handle_collisions()
      elif self.state == S_BALL_IN_PADDLE: # ball on paddle
        self.ball.left = self.paddle.left + self.paddle.width / 2
        self.ball.top  = self.paddle.top  - self.ball.height
        self.show_message("PRESS SPACE TO LAUNCH THE BALL")
      elif self.state == S_GAME_OVER: # game over
        self.show_message("GAME OVER.  PRESS ENTER TO PLAY AGAIN")
      elif self.state == S_WON: # game won
        self.show_message("YOU WON.  PRESS ENTER TO PLAY AGAIN")

      # Draw the brick, paddle, ball
      self.draw_bricks()
      pygame.draw.rect(self.screen, BLUE, self.paddle)
      pygame.draw.circle(self.screen, WHITE, (self.ball.left + BALL_RADIUS, self.ball.top + BALL_RADIUS), BALL_RADIUS)

      # Constantly update stats
      self.show_stats()

      # Flip the draw buffer
      pygame.display.flip()

### MAIN
if __name__ == '__main__':
  breakout = OUBreakout()
  breakout.run()
