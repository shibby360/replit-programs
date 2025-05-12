import pygame
from pygame.locals import *
import random as r
pygame.init()
__import__('os').system('clear')
screen = pygame.display.set_mode((280, 280))
pygame.display.set_caption('snake')
food_X = (r.randint(0, 140) // 10) * 10
food_Y = (r.randint(0, 140) // 10) * 10
snake_X = (r.randint(0, 140) // 10) * 10
snake_Y = (r.randint(0, 140) // 10) * 10
snake_UP = False
snake_DOWN = False
snake_LEFT = False
snake_RIGHT = False
snakelist = [[snake_X, snake_Y]]
score = 0
level = 1
delay = 100
snakecol = (0, 255, 0)
def show_text(msg, x, y, color, size=20):
  pygame.font.init()
  font = pygame.font.SysFont('freesans', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def move_Snake(direc):
  global snake_UP
  global snake_DOWN
  global snake_LEFT
  global snake_RIGHT
  if direc == 'up' and not snake_DOWN:
    snake_UP = True
    snake_DOWN = False
    snake_LEFT = False
    snake_RIGHT = False
  if direc == 'down' and not snake_UP:
    snake_LEFT = False
    snake_RIGHT = False
    snake_UP = False
    snake_DOWN = True
  if direc == 'left' and not snake_RIGHT:
    snake_RIGHT = False
    snake_UP = False
    snake_DOWN = False
    snake_LEFT = True
  if direc == 'right' and not snake_LEFT:
    snake_RIGHT = True
    snake_UP = False
    snake_DOWN = False
    snake_LEFT = False
#Change snake color on score 10 and increase speed
#Animate Game over
while True:
  screen.fill((0, 0, 0))
  if snake_UP:
    snake_Y -= 5
  if snake_LEFT:
    snake_X -= 5
  if snake_DOWN:
    snake_Y += 5
  if snake_RIGHT:
    snake_X += 5
  if [snake_X, snake_Y] in snakelist[1:] and len(snakelist) != 1:
    screen.fill((0, 0, 0))
    show_text('GAME OVER', 0, 0, (255, 0, 0), 50)
    pygame.display.update()
    pygame.time.delay(10000)
    break
  show_text('Score: ' + str(score), 0, 0, (255, 255, 255))
  show_text('Level: ' + str(level), 0, 20, (255, 255, 255))
  pygame.draw.rect(screen, (255, 0, 0), (food_X, food_Y, 10, 10))
  for segment in snakelist:
    pygame.draw.rect(screen, snakecol, segment+[10,10])
  if snake_X >= 280:
    snake_X = 10
  if snake_X <= 0:
    snake_X = 270
  if snake_Y >= 280:
    snake_Y = 10
  if snake_Y <= 0:
    snake_Y = 270
  if snake_X in range(food_X-10, food_X+10) and snake_Y in range(food_Y-10, food_Y+10):
    food_X = (r.randint(0, 140) // 10) * 10
    food_Y = (r.randint(0, 140) // 10) * 10
    snakelist.append([snake_X, snake_Y])
    score += 1
    if score == 10:
      level += 1
      delay -= 50
      score = 0
      if level == 4:
        delay = 100
      if level == 1:
        snakecol = (0, 255, 0)
      elif level == 2:
        snakecol = (155, 0, 0)
      else:
        snakecol = (0, 255, 180)
  else:
    snakelist.insert(0, [snake_X, snake_Y])
    snakelist.pop()
  pygame.time.delay(delay)
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_UP:
        move_Snake('up')
      if event.key == K_LEFT:
        move_Snake('left')
      if event.key == K_DOWN:
        move_Snake('down')
      if event.key == K_RIGHT:
        move_Snake('right')
    if event.type == QUIT:
      pygame.quit()
      exit()