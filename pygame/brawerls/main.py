import pygame
from pygame.locals import *
import random as r
pygame.init()
import os
os.system('clear')
screen = pygame.display.set_mode((280,280))
pygame.display.set_caption("brawling")
brawlers = ['Amber', 'Barley', 'Bea', 'Bibi', 'Byron', 'Carl', 'Colette', 'Crow', 'Darryl', 'Edgar', 'El_Primo', 'Frank', 'Gale', 'Gene', 'Jacky', 'Leon', 'Lou', 'Max', 'Mortis', 'Mr._P', 'Nani', 'Pam', 'Penny', 'Piper', 'Poco', 'Rico', 'Rosa', 'Sandy', 'Spike', 'Sprout', 'Surge', 'Tara']
brawlernum = 15
brawler = brawlers[brawlernum]
img_X = 112
img_Y = 112
inc = 10
size = 56
blue = (125, 175, 255)
red = (255, 0, 0)
blue2 = (144, 238, 144)
red2 = (255, 192, 203)
col = blue
col2 = blue2
bea_hornet = False
super_charge = 0
def colorize(image, newColor):
  image = image.copy()
  image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
  image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
  return image
while True:
  screen.fill((0, 0, 0))
  brawlerimg = pygame.image.load('brawlers/' + brawler + '_Skin-Default.png')
  brawlerimg = pygame.transform.scale(brawlerimg, (size, size))
  screen.blit(brawlerimg, (img_X, img_Y))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_RIGHT:
        img_X += inc
      if event.key == K_LEFT:
        img_X -= inc
      if event.key == K_DOWN:
        img_Y += inc
      if event.key == K_UP:
        img_Y -= inc
      if pygame.key.name(event.key) == ',':
        brawlernum -= 1
        if brawlernum < 0:
          brawlernum = 0
        brawler = brawlers[brawlernum]
      if pygame.key.name(event.key) == '.':
        brawlernum += 1
        if brawlernum >= len(brawlers):
          brawlernum = len(brawlers)-1
        brawler = brawlers[brawlernum]
      if pygame.key.name(event.key) == '=':
        size += inc
      if pygame.key.name(event.key) == '-':
        size -= inc
      if event.key == K_0:
        img_X = 112
        img_Y = 112
        size = 56
      if pygame.key.name(event.key) == '[':
        col = red
        col2 = red2
      if pygame.key.name(event.key) == ']':
        col = blue
        col2 = blue2
      if event.key == K_a:
        if brawler == 'Amber':
          pygame.draw.polygon(screen, col, ((img_X, img_Y+size), (img_X+size, img_Y+size), (img_X+size/2, img_Y+size*3)))
        if brawler == 'Barley':
          pygame.draw.circle(screen, col, (img_X+size/2, img_Y+(size*2)), size/2)
        if brawler == 'Bea':
          if not(bea_hornet):
            pygame.draw.rect(screen, col, (img_X+(size/4), img_Y+size, size/2, size/2))
            pygame.draw.polygon(screen, col, ((img_X+(size/4), img_Y+size*3/2), (img_X+(size*3/4), img_Y+size*3/2), (img_X+(size/2), img_Y+size*2)))
            bea_hornet = True
          else:
            pygame.draw.rect(screen, col, (img_X+(size/4), img_Y+size, size/2, size))
            pygame.draw.polygon(screen, col, ((img_X+(size/4), img_Y+size*3/2+(size/2)), (img_X+(size*3/4), img_Y+size*3/2+(size/2)), (img_X+(size/2), img_Y+size*2+size)))
            bea_hornet = False
        if brawler == 'Bibi':
          batlen = 70
          pygame.draw.line(screen, (165, 40, 40), (img_X+size/2, img_Y+size), (img_X+size/2-batlen, img_Y+size+batlen), 20)
          pygame.display.update()
          pygame.time.delay(1000)
          pygame.draw.line(screen, (165, 40, 40), (img_X+size/2, img_Y+size), (img_X+size/2, img_Y+size+batlen), 20)
          pygame.display.update()
          pygame.time.delay(1000)
          pygame.draw.line(screen, (165, 40, 40), (img_X+size/2, img_Y+size), (img_X+size/2+batlen, img_Y+size+batlen), 20)
        if brawler == 'Byron':
          pygame.draw.rect(screen, col2, (img_X+(size/4), img_Y+size, size/2, size/2))
          pygame.draw.polygon(screen, col2, ((img_X+(size/4), img_Y+size*3/2), (img_X+(size*3/4), img_Y+size*3/2), (img_X+(size/2), img_Y+size*2)))
        if brawler == 'Carl':
          carlweapimg = pygame.image.load('brawler-weapons/carl_pickaxe.png')
          carlweapimg = pygame.transform.scale(carlweapimg, (size, size))
          carlweapimg = colorize(carlweapimg, col)
          screen.blit(carlweapimg, (img_X, img_Y+size))
          pygame.display.update()
          pygame.time.delay(1000)
          screen.fill((0, 0, 0))
          screen.blit(brawlerimg, (img_X, img_Y))
          carlweapimg = pygame.transform.scale(carlweapimg, (size, size))
          carlweapimg = pygame.transform.rotate(carlweapimg, 90)
          carlweapimg = colorize(carlweapimg, col)
          screen.blit(carlweapimg, (img_X, img_Y+size*3))
          pygame.display.update()
          pygame.time.delay(1000)
          screen.fill((0, 0, 0))
          screen.blit(brawlerimg, (img_X, img_Y))
          carlweapimg = pygame.transform.scale(carlweapimg, (size, size))
          carlweapimg = pygame.transform.rotate(carlweapimg, 90)
          carlweapimg = colorize(carlweapimg, col)
          screen.blit(carlweapimg, (img_X, img_Y+size))
        if brawler == 'Colette':
          coletteweapimg = pygame.image.load('brawler-weapons/colette_heart.png')
          coletteweapimg = pygame.transform.scale(coletteweapimg, (size, size))
          coletteweapimg = colorize(coletteweapimg, col)
          screen.blit(coletteweapimg, (img_X, img_Y+size))
        if brawler == 'Crow':
          pygame.draw.polygon(screen, (0, 255, 0), ((img_X, img_Y+size), (img_X+size/3, img_Y+size), (img_X+size/6, img_Y+size*3/2)))
          pygame.draw.polygon(screen, (0, 255, 0), ((img_X+size/3, img_Y+size), (img_X+size/3+size/3, img_Y+size), (img_X+size/6+size/3, img_Y+size*3/2)))
          pygame.draw.polygon(screen, (0, 255, 0), ((img_X+size/3+size/3, img_Y+size), (img_X+size/3+size/3+size/3, img_Y+size), (img_X+size/6+size/3+size/3, img_Y+size*3/2)))
        if brawler == 'Darryl':
          darrylweapimg = pygame.image.load('brawler-weapons/darryl-pellet.png')
          darrylweapimg = pygame.transform.scale(darrylweapimg, (int(size*3/5), int(size*3/5)))
          screen.blit(darrylweapimg, (img_X+size/5, img_Y+size))
        if brawler == 'Edgar':
          pygame.draw.rect(screen, (0, 255, 0), (img_X, img_Y-size/2, size, size/4))
          pygame.draw.rect(screen, col, (img_X, img_Y+size, size, size*2))
          pygame.display.update()
          pygame.time.delay(1000)
          screen.fill((0, 0, 0))
          brawlerimg = pygame.image.load('brawlers/Edgar_Skin-Default.png')
          brawlerimg = pygame.transform.scale(brawlerimg, (size, size))
          brawlerimg = pygame.transform.flip(brawlerimg, True, False)
          screen.blit(brawlerimg, (img_X, img_Y))
          pygame.display.update()
          pygame.time.delay(1000)
          pygame.draw.rect(screen, (0, 255, 0), (img_X, img_Y-size/2, size, size/4))
          pygame.draw.rect(screen, col, (img_X, img_Y+size, size, size*2))
        if brawler == 'El_Primo':
          pygame.draw.rect(screen, col, (img_X, img_Y+size, size, size*2))
          pygame.display.update()
          pygame.time.delay(500)
          screen.fill((0, 0, 0))
          brawlerimg = pygame.image.load('brawlers/El_Primo_Skin-Default.png')
          brawlerimg = pygame.transform.scale(brawlerimg, (size, size))
          screen.blit(brawlerimg, (img_X, img_Y))
          pygame.display.update()
          pygame.time.delay(500)
          pygame.draw.rect(screen, col, (img_X, img_Y+size, size, size*2))
          pygame.display.update()
          pygame.time.delay(500)
          screen.fill((0, 0, 0))
          brawlerimg = pygame.image.load('brawlers/El_Primo_Skin-Default.png')
          brawlerimg = pygame.transform.scale(brawlerimg, (size, size))
          screen.blit(brawlerimg, (img_X, img_Y))
          pygame.display.update()
          pygame.time.delay(500)
          pygame.draw.rect(screen, col, (img_X, img_Y+size, size, size*2))
          pygame.display.update()
          pygame.time.delay(500)
          screen.fill((0, 0, 0))
          brawlerimg = pygame.image.load('brawlers/El_Primo_Skin-Default.png')
          brawlerimg = pygame.transform.scale(brawlerimg, (size, size))
          screen.blit(brawlerimg, (img_X, img_Y))
        if brawler == 'Frank':
          frankweapimg = pygame.image.load('brawler-weapons/frank-shockwave.png')
          frankweapimg = pygame.transform.scale(frankweapimg, (size, size))
          frankweapimg = pygame.transform.rotate(frankweapimg, 270)
          screen.blit(frankweapimg, (img_X, img_Y+size))
          frankweapimg = pygame.transform.rotate(frankweapimg, 360)
          frankweapimg = pygame.transform.scale(frankweapimg, (size*3, size))
          screen.blit(frankweapimg, (img_X-size, img_Y+size*2))
        if brawler == 'Gale':
          pygame.draw.rect(screen, col, (img_X, img_Y+size*2, size, 5))
        if brawler == 'Gene':
          pygame.draw.rect(screen, col, (img_X+size/4, img_Y+size, size/2, size*2))
        if brawler == 'Jacky':
          centerx = img_X+size/2
          centery = img_Y+size/2
          pygame.draw.circle(screen, col, (centerx, centery), size*3/2)
          screen.blit(brawlerimg, (img_X, img_Y))
        if brawler == 'Leon':
          pass
        pygame.display.update()
        pygame.time.delay(1000)
      super_charge += 10
    if event.type == QUIT:
      pygame.quit()
      exit()
#Put Darryl and Frank weapimg in remove.bg then recolor