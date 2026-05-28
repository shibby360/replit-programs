import random as r
import time as t
import pygame
import os
from pygame.locals import *
pygame.init()
size = 280
screen = pygame.display.set_mode((size, size+100))
pygame.display.set_caption('Mega box sim')
limit = 100
score = 0
os.system('clear')
#name = input('Whats ur name?: ')
def colorize(image, newColor):
  image = image.copy()
  image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
  image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
  return image
def img(img, fillcol=(0, 0, 0), chrmtc=False, spin=False):
  if chrmtc:
    raritycols = [(0, 255, 0), (0, 0, 255), (128, 0, 128), (255, 0, 0), (255, 255, 0)]
    coords = [0, size*1/5, size*2/5, size*3/5, size*4/5]
    countr = 0
    while countr < 5:
      pygame.draw.rect(screen, raritycols[countr], (0, coords[countr], size, int(size/5)))
      countr += 1
  else:
    screen.fill(fillcol)
  if spin:
    image = pygame.image.load(img)
    image = colorize(image, (0, 0, 0))
    image = pygame.transform.scale(image, (int(size/5), int(size/5)))
    screen.blit(image, (size*2/5, size*2/5))
    pygame.display.update()
    pygame.time.delay(500)
    image = pygame.transform.scale(image, (int(size*3/5), int(size*3/5)))
    screen.blit(image, (size/5, size/5))
    pygame.display.update()
    pygame.time.delay(500)
    image = pygame.transform.scale(image, (size, size))
    screen.blit(image, (0, 0))
    pygame.display.update()
    pygame.time.delay(500)
    screen.fill(fillcol)
    pygame.display.update()
  image = pygame.image.load(img)
  image = pygame.transform.scale(image, (size, size))
  screen.blit(image, (0, 0))
def show_text(msg, x, y, color, size=20):
  pygame.font.init()
  font = pygame.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def ask(question):
  answer = ''
  upper = False
  breaker = False
  while True:
    if breaker:
      screen.fill((0, 0, 0))
      show_text('Press 1,2,3,4,5', 0, 0, (255, 255, 255))
      show_text('Or x to quit', 0, 16, (255, 255, 255))
      show_text('anytime', 0, 32, (255, 255, 255))
      pygame.display.update()
      pygame.display.update()
      break
    screen.fill((0, 0, 0))
    strty = 0
    for i in question.split('\n'):
      show_text(i, 0, strty, (255, 255, 255))
      strty += 20
    show_text(answer + '|', 0, strty+32, (255, 255, 255))
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
      if event.type == KEYDOWN:
        if event.key == K_RETURN:
          breaker = True
        elif event.key == K_BACKSPACE:
          listed = list(answer)
          try:
            listed[-1] = ''
          except IndexError:
            pass
          answer = ''.join(listed)
        elif 'shift' in pygame.key.name(event.key):
          upper = True
        elif event.key == K_SPACE:
          answer += ' '
        elif len(pygame.key.name(event.key)) > 1:
          pass
        else:
          if upper:
            answer += pygame.key.name(event.key).capitalize()
            upper = False
          else:
            answer += pygame.key.name(event.key)
  return answer
name = ask('Whats ur name?: ')
while limit > 0:
  pygame.draw.rect(screen, (0, 0, 0), (0, size, size, 100))
  show_text(str(limit) + ' more Mega', 0, size, (255, 255, 255))
  show_text('boxes', 0, size+16, (255, 255, 255))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_1:
        b = 1
      if event.key == K_2:
        b = 2
      if event.key == K_3:
        b = 3
      if event.key == K_4:
        b = 4
      if event.key == K_5:
        b = 5
      if event.key == K_6:
        b = 6
      if event.key == K_x:
        pygame.quit()
        exit()
      limit -= 1
      def equal():
        return r.randint(1, 5)
      def unequal():
        if b == 6:
          return 6
        return r.choice([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
      a = unequal()
      if a == b:
        chromatics = ['Gale', 'Surge', 'Colette', 'Lou', 'Colonel Ruffs']
        t.sleep(0.5)
        if a == 6:
          c = 0
        else:
          c = r.randint(1, 15)
        if c <= 5 and c > 0:
          suprrs = ['Rosa', 'El Primo', 'Barley', 'Poco']
          choiz = r.choice(suprrs)
          img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (0, 255, 0))
          score += 2
        elif c > 5 and c <= 9:
          suprrs = ['Carl', 'Penny', 'Rico', 'Darryl', 'Jacky']
          choiz = r.choice(suprrs)
          img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (0, 0, 255))
          score += 2
        elif c > 9 and c <= 12:
          epics = ['Piper', 'Frank', 'Nani', 'Pam', 'Bea', 'Bibi', 'Gale', 'Surge', 'Edgar', 'Colette']
          choiz = r.choice(epics)
          if choiz in chromatics:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
          else:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (128, 0, 128))
          score += 3
        elif c > 12 and c <= 14:
          mythics = ['Max', 'Tara', 'Mortis', 'Gene', 'Mr. P', 'Sprout', 'Byron', 'Lou']
          choiz = r.choice(mythics)
          if choiz in chromatics:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
          else:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (255, 0, 0))
          score += 5
        elif c > 14:
          legends = ['Crow', 'Spike', 'Sandy', 'Leon', 'Amber', 'Colonel Ruffs']
          choiz = r.choice(legends)
          if choiz in chromatics:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
          else:
            img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (255, 255, 0), spin=True)
          score += 10
        elif c == 0:
          truelegends = ['Crow', 'Spike', 'Sandy', 'Leon', 'Amber']
          choiz = r.choice(truelegends)
          img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (255, 255, 0), spin=True)
          score += 10
      else:
        img('brawl coin.jpg')
      pygame.display.update()
  if limit < 0:
    screen.fill((0, 0, 0))
    break
f = open('high score.txt')
g = int(f.readline())
if score > g and name != 'None':
  f = open('high score.txt', 'w')
  fi = open('high score name.txt', 'w')
  f.write(str(score))
  fi.write(name)
  f.close()
  fi.close()
f = open('high score.txt')
f.close()
if name != 'None':
  openup = open('scores.txt', 'a')
  openup.write('{0}: {1}\n'.format(name, score))
  openup.close()

while True:
  screen.fill((0, 0, 0))
  show_text('Your score: ' + str(score), 0, 0, (255, 255, 255))
  show_text('Highest Score:', 0, 32, (255, 255, 255))
  show_text(str(g), 0, 48, (255, 255, 255))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
    if event.type == KEYDOWN:
      if event.key == K_x:
        pygame.quit()
        exit()