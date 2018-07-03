import pygame, sys, random

SCREEN_W = 640
SCREEN_H = 480

BRICK_W = 60
BRICK_H = 15

PADDLE_W = 60
PADDLE_H = 12

BALL_DIAMETER = 16
BALL_RADIUS   = BALL_DIAMETER / 2

MAX_PADDLE_X = SCREEN_W - PADDLE_W
MAX_BALL_X   = SCREEN_W - BALL_DIAMETER
MAX_BALL_Y   = SCREEN_H - BALL_DIAMETER

PADDLE_Y = SCREEN_H - PADDLE_H - 10

BLACK = (0,0,0)
GOLD  = (135,113,72)
WHITE = (255,255,255)
BLUE  = (0,0,255)

S_BALL_IN_PADDLE = 0
S_PLAYING = 1
S_WON = 2
S_GAME_OVER = 3

class OUBreakout:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption('OU Breakout')
    self.clock = pygame.time.Clock()

    if pygame.font:
      self.font = pygame.font.Font(None, 30)
    else:
      self.font = None

    self.initialize_game()

  def initialize_game(self):
    self.lives = 3
    self.score = 0
    self.state = S_BALL_IN_PADDLE

    self.paddle = pygame.Rect(300, PADDLE_Y, PADDLE_W, PADDLE_H)
    self.ball   = pygame.Rect(300, PADDLE_Y - BALL_DIAMETER, BALL_DIAMETER, BALL_DIAMETER)
    self.ball_velocity = [5,-5]
    self.create_bricks()

  def create_bricks(self):
    y_offset = 35
    self.bricks = []
  
    for i in range(7):
      x_offset = 35
      for j in range(8):
        self.bricks.append(pygame.Rect(x_offset,y_offset,BRICK_W,BRICK_H))
        x_offset += BRICK_W + 10
      y_offset += BRICK_H + 5

  def draw_bricks(self):
    for brick in self.bricks:
      pygame.draw.rect(self.screen, GOLD, brick)

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

      self.clock.tick(60)
      self.screen.fill(BLACK)

      self.draw_bricks()

      pygame.display.flip()

if __name__ == '__main__':
  game = OUBreakout()
  game.run()
