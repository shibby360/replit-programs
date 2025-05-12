import pygame
from pygame.locals import *
import random as r
pygame.init()
screen = pygame.display.set_mode((280,280))
pygame.display.set_caption("pong")
#Ball
ball_X = 140
ball_Y = 140
radius = 10
speed_X = 5
speed_Y = 5
#Left Paddle
L_P_W = 60
L_P_H = 30
L_P_X = 0
L_P_Y = 110
L_P_D = 5
L_P_U = 5
L_P_G_D = False
L_P_G_U = False
#Right Paddle
R_P_W = 60
R_P_H = 30
R_P_X = 280-R_P_H
R_P_Y = 110
R_P_D = 5
R_P_U = 5
R_P_G_D = False
R_P_G_U = False
#Others
delay = 25
#Player scores
p1_score = 0
p2_score = 0
def show_text(msg, x, y, color, size=20):
  pygame.font.init()
  font = pygame.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
while True:
  screen.fill((0, 0, 0))
  if p1_score == 20:
    import os
    os.system('clear')
    print('Player 1 has won!')
    continue
  if p2_score == 20:
    import os
    os.system('clear')
    print('Player 2 has won!')
    continue
  pygame.draw.circle(screen, (255, 255, 255), (ball_X, ball_Y), radius)
  pygame.draw.rect(screen, (255, 0, 0), (L_P_X, L_P_Y, L_P_H, L_P_W))
  pygame.draw.rect(screen, (0, 255, 0), (R_P_X, R_P_Y, R_P_H, R_P_W))
  show_text(str(p1_score), 0, 0, (255, 0, 0))
  show_text(str(p2_score), 0, 180, (0, 255, 0))
  #Moving
  if R_P_G_D:
    R_P_Y += R_P_D
  if R_P_G_U:
    R_P_Y -= R_P_U
  if L_P_G_D:
    L_P_Y += L_P_D
  if L_P_G_U:
    L_P_Y -= L_P_U
  ball_X += speed_X
  ball_Y += speed_Y
  #Ball collsion
  'Wall'
  if ball_X >= 280 - radius:
    p1_score += 1
    ball_X = 140
    ball_Y = 140
    speed_X = 5
    speed_Y = 5
  if ball_X <= 0 + radius:
    p2_score += 1
    ball_X = 140
    ball_Y = 140
    speed_X = 5
    speed_Y = 5
  if ball_Y not in range(0+radius, 280-radius):
    speed_Y = -speed_Y
  'Paddles'
  if ball_X >= R_P_X - radius and ball_Y >= R_P_Y and ball_Y < R_P_Y + R_P_W:
    speed_X = -5
    #print('Bounced of right paddle')
  if ball_X <= L_P_X + radius + L_P_H and ball_Y >= L_P_Y and ball_Y < L_P_Y + L_P_W:
    #print('Bounced of left paddle')
    speed_X = 5
  #Both Paddle Collision(Paddle to wall)
  if R_P_Y <= 0:
    R_P_U = 0
  if R_P_Y >= 280-R_P_W:
    R_P_D = 0
  if L_P_Y <= 0:
    L_P_U = 0
  if L_P_Y >= 280-L_P_W:
    L_P_D = 0
  pygame.time.delay(delay)
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      L_P_D = 5
      L_P_U = 5
      R_P_D = 5
      R_P_U = 5
      if event.key == K_w:
        L_P_G_U = True
      if event.key == K_s:
        L_P_G_D = True
      if event.key == K_UP:
        R_P_G_U = True
      if event.key == K_DOWN:
        R_P_G_D = True
    if event.type == KEYUP:
      if event.key == K_w:
        L_P_G_U = False
      if event.key == K_s:
        L_P_G_D = False
      if event.key == K_UP:
        R_P_G_U = False
      if event.key == K_DOWN:
        R_P_G_D = False
    if event.type == QUIT:
      pygame.quit()
      exit()