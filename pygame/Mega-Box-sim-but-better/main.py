import random as r
import time as t
import pygame
import os
from pygame.locals import *
pygame.init()
size = 180
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption('Mega box sim')
limit = 100
score = 0
os.system('clear')
name = input('Whats ur name?: ')
def chromatic(text):
  lentxt = 0
  while lentxt < len(text):
    lentxt += 1
    if lentxt % 5 == 0:
      color = '\x1b[0;32m'
    elif lentxt % 5 == 1:
      color = '\x1b[0;34m'
    elif lentxt % 5 == 2:
      color = '\x1b[0;35m'
    elif lentxt % 5 == 3:
      color = '\x1b[0;31m'
    elif lentxt % 5 == 4:
      color = '\x1b[0;33m'
    print(color + text[lentxt - 1], end='')
  print()
def img(img, fillcol=(0, 0, 0), chrmtc=False):
  if chrmtc:
    raritycols = [(0, 255, 0), (0, 0, 255), (128, 0, 128), (255, 0, 0), (255, 255, 0)]
    coords = [0, size*1/5, size*2/5, size*3/5, size*4/5]
    countr = 0
    while countr < 5:
      pygame.draw.rect(screen, raritycols[countr], (0, coords[countr], size, int(size/5)))
      countr += 1
  else:
    screen.fill(fillcol)
  image = pygame.image.load(img)
  image = pygame.transform.scale(image, (size, size))
  screen.blit(image, (0, 0))
while limit > 0:
  limit -= 1
  a = r.randint(1, 5)
  b = int(input('\033[0;0mChoose a number between 1 and 5: '))
  if a == b:
    chromatics = ['Gale', 'Surge', 'Colette', 'Lou']
    print('You got a brawler!')
    t.sleep(0.5)
    c = r.randint(1, 15)
    if c <= 5:
      print('\033[0;32mYou got a rare.')
      suprrs = ['Rosa', 'El Primo', 'Barley', 'Poco']
      choiz = r.choice(suprrs)
      img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (0, 255, 0))
      print('You got: ' + choiz)
      score += 2
    elif c > 5 and c <= 9:
      print('\033[0;34mYou got a super rare.')
      suprrs = ['Carl', 'Penny', 'Rico', 'Darryl', 'Jacky']
      choiz = r.choice(suprrs)
      img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (0, 0, 255))
      print('You got: ' + choiz)
      score += 2
    elif c > 9 and c <= 12:
      epics = ['Piper', 'Frank', 'Nani', 'Pam', 'Bea', 'Bibi', 'Gale', 'Surge', 'Edgar']
      choiz = r.choice(epics)
      if choiz in chromatics:
        chromatic('You got a chromatic!')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
        chromatic('You got: ' + choiz)
      else:
        print('\033[0;35mYou got an epic!')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (128, 0, 128))
        print('You got: ' + choiz)
      score += 3
    elif c > 12 and c <= 14:
      mythics = ['Max', 'Tara', 'Mortis', 'Gene', 'Mr. P', 'Sprout', 'Colette', 'Byron']
      choiz = r.choice(mythics)
      if choiz in chromatics:
        chromatic('You got a chromatic!')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
        chromatic('You got: ' + choiz)
      else:
        print('\033[0;31mYou got a mythic!')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (255, 0, 0))
        print('You got: ' + choiz)
      score += 5
    elif c > 14:
      legends = ['Crow', 'Spike', 'Sandy', 'Leon', 'Lou', 'Amber']
      choiz = r.choice(legends)
      if choiz in chromatics:
        chromatic('You got a chromatic!')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', chrmtc=True)
        chromatic('You got: ' + choiz)
      else:
        yellow = '\033[1;33m'
        print(yellow + '    _  _    _                _')
        print(yellow + '|  |_ | _  |_ |\\ | |\\  /_\\  |_| \/ |')
        print(yellow + '|_ |_ |__| |_ | \\| |/ /   \\ |\\   | .')
        img('brawlers/' + choiz.replace(' ', '_') + '_Skin-Default.png', (255, 255, 0))
        print('You got: ' + choiz)
      score += 10
  else:
    print('YOU GOT NOTHING.')
    img('brawl coin.jpg')
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
print('\033[0;0m Your score: ' + str(score))
f = open('high score.txt')
g = int(f.readline())
if score > g:
  f = open('high score.txt', 'w')
  fi = open('high score name.txt', 'w')
  f.write(str(score))
  fi.write(name)
  f.close()
  fi.close()
f = open('high score.txt')
print('Highest Score: ' + f.readline())
f.close()
if name != 'None':
  openup = open('scores.txt', 'a')
  openup.write('{0}: {1}\n'.format(name, score))