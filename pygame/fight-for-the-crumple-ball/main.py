import pygame
from pygame.locals import *
import random as r
pygame.init()
__import__('os').system('clear')
size = 450
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("crumple ball fight")
sqs = int(size/5)
smsqs = int(sqs/5)
#Images
ball = pygame.transform.scale(pygame.image.load('crumpleball.jpg'), (sqs, sqs))
sball = pygame.transform.scale(ball, (smsqs, smsqs))
person = pygame.transform.scale(pygame.image.load('googlepfp.png'), (sqs, sqs))
#Items
'P1'
p1x = 0
p1y = 2
p1l = 10
p1_with_ball = False
p1_score = 0
p1e = 0
'P2'
p2x = 4
p2y = 2
p2l = 10
p2_with_ball = False
p2_score = 0
p2e = 0
'Ball'
bx = 2
by = 2
#Input vars
wait_for_opp_input = True
wait_for_ball_input = True
#Other variables
waitime = 500
#Functions
def colorize(image, newColor):
  image = image.copy()
  image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
  image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
  return image
def show_text(msg, x, y, color, size=20):
  pygame.font.init()
  font = pygame.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def reset(x='nopball'):
  if x == '+pball':
    global p1_with_ball
    global p2_with_ball
    p1_with_ball = False
    p2_with_ball = False
  global p1x
  global p1y
  global p2x
  global p2y
  global bx
  global by
  p1x = 0
  p1y = 2
  p2x = 4
  p2y = 2
  bx = 2
  by = 2
def if_began():
  return p1x == 0 and p1y == 2 and p2x == 4 and p2y == 2 and bx == 2 and by == 2 and p1_score == 0 and p2_score == 0
while True:
  screen.fill((0, 0, 0))
  if if_began():
    if wait_for_opp_input:
      show_text('Press a for NPC red or c for 2 player', 0, 0, (255, 0, 0))
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_a:
            opptype = 'a'
            wait_for_opp_input = False
          if event.key == K_c:
            opptype = 'c'
            wait_for_opp_input = False
      pygame.display.update()
      continue
      screen.fill((0, 0, 0))
    elif wait_for_ball_input:
      show_text('CHOOSE YOUR BALL!', 0, 0, (255, 0, 0))
      def sizer(img):
        return pygame.transform.scale(img, (int(sqs/2), int(sqs/2)))
      show_text('The original!', 0, 50, (255, 0, 0))
      screen.blit(sizer(pygame.image.load('crumpleball.jpg')), (0, 70))
      show_text('Beach ball!', 150, 50, (255, 0, 0))
      screen.blit(sizer(pygame.image.load('beachball.png')), (150, 70))
      show_text('Press the number key to choose', 0, size-40, (255, 0, 0))
      for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_1:
            ball = pygame.transform.scale(pygame.image.load('crumpleball.jpg'), (sqs, sqs))
            sball = pygame.transform.scale(ball, (smsqs, smsqs))
            wait_for_ball_input = False
          if event.key == K_2:
            ball = pygame.transform.scale(pygame.image.load('beachball.png'), (sqs, sqs))
            sball = pygame.transform.scale(ball, (smsqs, smsqs))
            wait_for_ball_input = False
      pygame.display.update()
      continue
      screen.fill((0, 0, 0))
  rp1x = size*p1x/5
  rp1y = size*p1y/5
  rp2x = size*p2x/5
  rp2y = size*p2y/5
  screen.blit(person, (rp1x, rp1y))
  show_text(str(p1_score), rp1x, rp1y, (255, 255, 255))
  if p1_with_ball:
    screen.blit(sball, (rp1x+sqs*2/5, rp1y+sqs*2/5))
  screen.blit(colorize(person, (255, 0, 0)), (rp2x, rp2y))
  show_text(str(p2_score), rp2x, rp2y, (255, 255, 255))
  if p2_with_ball:
    screen.blit(sball, (rp2x+sqs*2/5, rp2y+sqs*2/5))
  if not p1_with_ball and not p2_with_ball:
    screen.blit(ball, (size*bx/5, size*by/5))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_UP:
        if p1_with_ball:
          by -= 1
        p1y -= 1
      if event.key == K_DOWN:
        if p1_with_ball:
          by += 1
        p1y += 1
      if event.key == K_RIGHT:
        if p1_with_ball:
          bx += 1
        p1x += 1
      if event.key == K_LEFT:
        if p1_with_ball:
          bx -= 1
        p1x -= 1
      if event.key == K_SPACE:
        if p1_with_ball:
          if p1x == 2 and (p1y == 0 or p1y == 4):
            p1_with_ball = False
            bx += r.randint(1, 2)
            show_text('Blue threw!', 0, 0, (0, 0, 255))
            pygame.display.update()
            pygame.time.delay(waitime)
            p1e += 1
          else:
            p2_with_ball = True
            p1_with_ball = False
            reset()
            show_text('Illegal throw by Blue!', 0, 0, (0, 0, 255))
            pygame.display.update()
            pygame.time.delay(waitime)
      if event.key == K_PERIOD:
        if p1e >= 5:
          if p1x == p2x:
            p2l -= 1
          p1_with_ball = True
          p2_with_ball = False
          bx = r.randint(3, 5)
          p1x = r.randint(3, 5)
          p1e -= 5
      #Tackling
      if p1x == p2x and p1y == p2y:
        show_text('Tackle by Blue!', 0, 0, (0, 0, 255))
        pygame.display.update()
        pygame.time.delay(waitime)
        p2l -= 1
        p2_with_ball = False
        p1_with_ball = True
        reset()
        continue
      if opptype == 'a':
        if event.key in [K_UP, K_DOWN, K_RIGHT, K_LEFT, K_o, K_PERIOD]:
          if p2x == 0:
            if p2_with_ball:
              p2x -= 1
            else:
              p2x += 1
          else:
            if p2x == 2:
              direc = r.choice(['up', 'down', 'left', 'left', 'left', 'left', 'left', 'throw', 'throw', 'drive', 'drive'])
            else:
              direc = r.choice(['up', 'down', 'left', 'left', 'left', 'left', 'left', 'drive', 'drive'])
            if direc == 'up':
              if p2_with_ball:
                by -= 1
              p2y -= 1
            if direc == 'down':
              if p2_with_ball:
                by += 1
              p2y += 1
            if direc == 'left':
              if p2_with_ball:
                bx -= 1
              p2x -= 1
            if direc == 'throw':
              if p2_with_ball:
                if p2x == 2 and (p2y == 0 or p2y == 4):
                  p2_with_ball = False
                  bx -= r.randint(1, 2)
                  show_text('Red threw!', 0, 0, (255, 0, 0))
                  pygame.display.update()
                  pygame.time.delay(waitime)
                  p2e += 1
                else:
                  p1_with_ball = True
                  p2_with_ball = False
                  reset()
                  show_text('Illegal throw by Red!', 0, 0, (255, 0, 0))
                  pygame.display.update()
                  pygame.time.delay(waitime)
              else:
                p2x -= 1
            if direc == 'drive' and p2e >= 5:
              if p1x == p2x:
                p1l -= 1
              p2_with_ball = True
              p1_with_ball = False
              bx = r.randint(-1, 1)
              p2x = r.randint(-1, 1)
              p2e -= 5
      if opptype == 'c':
        if event.key == K_w:
          if p2_with_ball:
            by -= 1
          p2y -= 1
        if event.key == K_s:
          if p2_with_ball:
            by += 1
          p2y += 1
        if event.key == K_d:
          if p2_with_ball:
            bx += 1
          p2x += 1
        if event.key == K_a:
          if p2_with_ball:
            bx -= 1
          p2x -= 1
        if event.key == K_t:
          if p2_with_ball:
            if p2x == 2 and (p2y == 0 or p2y == 4):
              p2_with_ball = False
              bx -= r.randint(1, 2)
              show_text('Red threw!', 0, 0, (255, 0, 0))
              pygame.display.update()
              pygame.time.delay(waitime)
              p2e += 1
            else:
              p1_with_ball = True
              p2_with_ball = False
              reset()
              show_text('Illegal throw by Red!', 0, 0, (255, 0, 0))
              pygame.display.update()
              pygame.time.delay(waitime)
        if event.key == K_r:
          if p2e >= 5:
            if p1x == p2x:
              p1l -= 1
            p2_with_ball = True
            p1_with_ball = False
            bx = r.randint(-1, 1)
            p2x = r.randint(-1, 1)
            p2e -= 5
      if p1x == p2x and p1y == p2y:
        show_text('Tackle by Red!', 0, 0, (255, 0, 0))
        pygame.display.update()
        pygame.time.delay(waitime)
        p1l -= 1
        p1_with_ball = False
        p2_with_ball = True
        reset()
        continue
    #Wall collision and scoring
    if p1x > 4:
      if p1_with_ball:
        p1_score += 1
        reset('+pball')
      else:
        p1x = 4
    if p1x < 0:
      p1x = 0
    if p1y > 4:
      p1y = 4
    if p1y < 0:
      p1y = 0
    if p2x > 4:
      p2x = 4
    if p2x < 0:
      if p2_with_ball:
        p2_score += 1
        reset('+pball')
      else:
        p2x = 0
    if p2y > 4:
      p2y = 4
    if p2y < 0:
      p2y = 0
    #Ball to player collision and collection
    if p1x == bx and p1y == by and not p2_with_ball:
      p1_with_ball = True
    if p2x == bx and p2y == by and not p1_with_ball:
      p2_with_ball = True
    #Death and win
    if p1l <= 0:
      show_text('RED WINS!!!', 0, 0, (255, 255, 255), 50)
      pygame.display.update()
      pygame.time.delay(10000)
      pygame.quit()
      exit()
    if p2l <= 0:
      show_text('BLUE WINS!!!', 0, 0, (255, 255, 255), 50)
      pygame.display.update()
      pygame.time.delay(10000) 
      pygame.quit()
      exit()
    if p1_score == 10:
      show_text('BLUE WINS!!!', 0, 0, (255, 255, 255), 50)
      pygame.display.update()
      pygame.time.delay(10000) 
      pygame.quit()
      exit()
    if p2_score == 10:
      show_text('RED WINS!!!', 0, 0, (255, 255, 255), 50)
      pygame.display.update()
      pygame.time.delay(10000)
      pygame.quit()
      exit()
    #Throw scoring
    if bx > 4:
      p1_score += 1
      p1e += 2
      reset('+pball')
    if bx < 0:
      p2_score += 1
      p2e += 2
      reset('+pball')
    #Quit event
    if event.type == QUIT or (event.type == KEYDOWN and event.key == K_x):
      pygame.quit()
      exit()