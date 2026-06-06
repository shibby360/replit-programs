pyfigsupport = input('Is pyfiglet supported(y/n)?: ')
if pyfigsupport == 'y':
  import pyfiglet
  var = pyfiglet.Figlet(font="standard")
  def intro(col, text):
    print(col)
    print(var.renderText(text))
opptypedecision = input('Smart opponent or not(y/n)?: ')
if opptypedecision == 'y':
  opptype = 'Smart'
else:
  opptype = 'rand'
import sys
import time
import pygame
import os
from pygame.locals import *
#import getch as g
import random as r
pygame.init()
screen = pygame.display.set_mode((480,580))
pygame.display.set_caption("Fighting Game")
Green="\033[0;32m"
Red = "\033[1;31m"
Blue="\033[0;34m"
Orange ="\033[0;33m"
def print(str, end='\n'):
  for c in str + end:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0)
def show_text(msg, x, y, color, size=32):
  pygame.font.init()
  font = pygame.font.SysFont('monospace', size)
  text = font.render(msg, True, color)
  screen.blit(text, (x, y))
def sayall():
  print(Blue + "Your distance: {0}\nYour health: {1}\nOpponent's distance: {2}\nOppnent's Health: {3}\nYour energy: {4}\nYour opponent's energy: {5}".format(playdist, playhealth, oppdist, opphealth, playener, oppener))
import random
playdist = 50
playhealth = 100
playener = 50
oppdist = 50
opphealth = 100
oppener = 50
playavatar = input('Which avatar(Ninja, Stick man)?: ').lower()
class playavatar:
  img = playavatar
if playavatar.img == 'ninja':
  setattr(playavatar, 'size', 160)
if playavatar.img == 'stick man':
  setattr(playavatar, 'size', 240)
class oppavatar:
  img = r.choice(['ninja', 'stick man'])
if playavatar.img == 'ninja':
  setattr(oppavatar, 'size', 160)
if playavatar.img == 'stick man':
  setattr(oppavatar, 'size', 240)
def animate(image, who, avatar, type='inbattle'):
  animations = []
  for i in range(10):
    imagee = pygame.image.load(avatar + '/' + image + '_00' + str(i) + '.png')
    if who == 'opp':
      image2 = pygame.transform.flip(imagee, True, False)
      image3 = pygame.transform.scale(image2, (oppavatar.size, oppavatar.size))
    else:
      image2 = imagee
      image3 = pygame.transform.scale(image2, (playavatar.size, playavatar.size))
    animations.append(image3)
  for i in animations:
    screen.fill((0, 0, 0))
    if type == 'inbattle':
      if who == 'opp':
        show_text('Opponent Attacking', 0, 0, (255, 0, 0))
        if oppavatar.size == 160:
          screen.blit(i, (160, 160))
        else:
          screen.blit(i, (120, 120))
      else:
        show_text('Player Attacking', 0, 0, (0, 255, 0))
        if playavatar.size == 160:
          screen.blit(i, (160, 160))
        else:
          screen.blit(i, (120, 120))
    elif type == 'end':
      show_text('End Results...', 0, 0, (255, 255, 0))
    pygame.time.delay(200)
    pygame.display.update()
def play():
  import AAAstuff
  global playdist
  global playhealth
  global playener
  global oppdist
  global opphealth
  global oppener
  print(Green + "Press p to punch, k to kick, g to grab, r to ram, and f to turn the fan on.")
  #move = g.getche().upper()
  #with input
  move = input().upper()
  print('')
  #Player Attack
  if move == "P":
    print("You punched.")
    oppdist -= 10
    opphealth -= 25
    playener -= 5
    sayall()
    animate('Punch_', 'play', playavatar.img)
  elif move == "K":
    print("You kicked.")
    oppdist -= 10
    opphealth -= 35
    playener -= 10
    sayall()
    animate('Kick_', 'play', playavatar.img)
  elif move == "G":
    print("You grabbed.")
    playdist = oppdist + 5
    oppdist -= 30
    playhealth -= 10
    playener -= 15
    sayall()
    animate('Climb', 'play', playavatar.img)
  elif move == "R":
    print("You rammed.")
    playdist += 25
    playhealth -= 50
    opphealth -= 25
    oppdist = 5
    playener -= 20
    sayall()
    animate('Ram_', 'play', playavatar.img)
  elif move == "F":
    print("Fan is on.")
    playhealth += 50
    playener += 20
    sayall()
    animate('Fan', 'play', playavatar.img)
  else:
    print("Turn Skipped! Type the whole word and a capital on the first letter only next time.")
    animate('Idle_', 'play', playavatar.img)
  AAAstuff.playmove = move
def opp(le_type):
  print(Red, end='')
  global playdist
  global playhealth
  global playener
  global oppdist
  global opphealth
  global oppener
  #Opponent Attack
  if playener <= 0:
    le_type = 'rand'
  if le_type == 'rand':
    oppmovenum = random.randrange(0, 5)
    if oppmovenum == 0:
      oppmove = "Punch"
    elif oppmovenum == 1:
      oppmove = "Kick"
    elif oppmovenum == 2:
      oppmove = "Grab"
    elif oppmovenum == 3:
      oppmove = "Ram"
    elif oppmovenum == 4:
      oppmove = "Skip"
    elif oppmovenum == 5:
      oppmove = "Fan on"
  elif le_type == 'Smart':
    import AAAstuff
    playersmove = AAAstuff.playmove
    if playersmove == 'P' or playersmove == 'K':
      oppmove = 'Fan on'
    elif playersmove == 'G':
      oppmove = 'Ram'
    elif playersmove == 'R':
      oppmove = 'Grab'
    else:
      oppmove = 'Kick'
  if oppmove == "Punch":
    print("The opponent punched.")
    playdist -= 10
    playhealth -= 25
    oppener -= 5
    sayall()
    animate('Punch_', 'opp', oppavatar.img)
  elif oppmove == "Kick":
    print("The opponent kicked.")
    playdist -= 10
    playhealth -= 25
    oppener -= 10
    sayall()
    animate('Kick_', 'opp', oppavatar.img)
  elif oppmove == "Grab":
    print("The opponent grabbed.")
    oppdist += playdist + 5
    playdist -= 30
    opphealth -= 10
    oppener -= 15
    sayall()
    animate('Climb', 'opp', oppavatar.img)
  elif oppmove == "Ram":
    print("The opponent rammed.")
    oppdist += 25
    opphealth -= 50
    playhealth -= 25
    playdist = 5
    oppener -= 20
    sayall()
    animate('Ram_', 'opp', oppavatar.img)
  elif oppmove == "Fan on":
    print("Fan is on.")
    opphealth += 50
    oppener += 20
    sayall()
    animate('Fan', 'opp', oppavatar.img)
  elif oppmove == "Skip":
    print("The opponent's turn was skipped. Its just luck!")
    animate('Idle_', 'opp', oppavatar.img)
print(Blue + "This is a game I created. You will be wrestling someone on a bed. When you throw them off the bed, you will win. You have five moves. You can either punch, kick, grab, ram, or turn on the fan. Press ENTER to continue.")
input()
name = input(Orange + "What is your name? ")
print("Hello, " + name)
sayall()
while playdist > 0 and playhealth > 0 and oppdist > 0 and opphealth > 0 and playener > 0 and oppener > 0:
  screen.fill((0, 0, 0))
  play()
  if playhealth <= 0:
    break
  if playdist <= 0:
    break
  if opphealth <= 0:
    break
  if oppdist <= 0:
    break
  opp(opptype)
  pygame.draw.rect(screen, (255, 255, 255), (0, 530, 240, 50), 5)
  pygame.draw.rect(screen, (255, 255, 255), (240, 530, 240, 50), 5)
  #Player health bar
  show_text('Player Health', 0, 480, (0, 255, 0))
  if playhealth > 50:
    playhealthcol = (0, 255, 0)
  elif playhealth > 25:
    playhealthcol = (255, 255, 0)
  else:
    playhealthcol = (255, 0, 0)
  playhealthbarlength = playhealth * 2.4
  playhealthbarlength = round(playhealthbarlength)
  if playhealthbarlength > 240:
    playhealthbarlength = 240
  pygame.draw.rect(screen, playhealthcol, (0, 530, playhealthbarlength, 50))
  #Opponent health bar
  show_text('Opponent Health', 240, 480, (255, 0, 0), 25)
  if opphealth > 50:
    opphealthcol = (0, 255, 0)
  elif opphealth > 25:
    opphealthcol = (255, 255, 0)
  else:
    opphealthcol = (255, 0, 0)
  opphealthbarlength = opphealth * 2.4
  opphealthbarlength = round(opphealthbarlength)
  if opphealthbarlength > 240:
    opphealthbarlength = 240
  pygame.draw.rect(screen, opphealthcol, (240, 530, opphealthbarlength, 50))
  #Dividers
  pygame.draw.line(screen, (255, 255, 255), (0, 480), (480, 480))
  pygame.draw.line(screen, (255, 255, 255), (240, 480), (240, 580), 5)
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
if playener <= 0:
  while playdist > 0 and playhealth > 0 and oppdist > 0 and opphealth > 0 and oppener > 0:
    screen.fill((0, 0, 0)) 
    opp(opptype)
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
if oppener <= 0:
  while playdist > 0 and playhealth > 0 and oppdist > 0 and opphealth > 0 and playener > 0:
    screen.fill((0, 0, 0)) 
    play()
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        exit()
points = 0
if playdist <= 0:
  print(Red + "Sad. You fell off the bed.")
  points -= 1
  animate('Dead_', '', playavatar.img, 'end')
  playhealth -= 10
if oppdist <= 0:
  print(Green + "Yay! The opponent fell off the bed!")
  points += 1
  animate('Jump_', '', playavatar.img, 'end')
  opphealth -= 10
if playhealth <= 0:
  print(Red + "Sad. You died.")
  points -= 2
  animate('Dead_', '', playavatar.img, 'end')
if opphealth <= 0:
  print(Green + "Yay! The opponent died!")
  points += 2
  animate('Jump_', '', playavatar.img, 'end')
if pyfigsupport == 'y':
  screen.fill((0, 0, 0))
  if points == 0:
    intro(Blue, 'DRAW')
  if points > 0:
    intro(Green, 'WIN!!!!')
  if points < 0:
    intro(Red, 'Loss')
while True:
  screen.fill((0, 0, 0))
  if points == 0:
    show_text('DRAW', 200, 255, (0, 0, 255), 50)
  if points > 0:
    show_text('YOU WIN!!!!', 155, 240, (0, 255, 0))
  if points < 0:
    show_text('You lose...', 155, 240, (255, 0, 0))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()