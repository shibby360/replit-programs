import shdw
import sys
screen = shdw.init_pygame(600, 600, 'space invaders')
alien = shdw.GUI.image.load('al.png')
ship = shdw.GUI.image.load('OIP.png')
class Char:
  def __init__(self, x, y, width, height, img):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.img = shdw.GUI.transform.scale(img, (width, height))
  def draw(self):
    self.rect = screen.blit(self.img, (self.x, self.y))
class Alien(Char):
  def move_alien(self, spd):
    self.x += spd
  def alien_down(self, by):
    self.y -= by
class Ship(Char):
  pass
class Bullet:
  def __init__(self, x, y, if_shot):
    self.x = x
    self.y = y
    self.if_shot = if_shot
  def draw(self):
    self.rect = shdw.GUI.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)
  def move(self):
    if self.if_shot:
      self.y -= 10
    if self.y <= 5:
      self.if_shot = False
      self.reset_x_y()
    for i in aliens[:]:
      for j in i[:]:
        if self.rect.colliderect(j.rect):
          i.remove(j)
          if i == []:
            aliens.remove(i)
          self.if_shot = False
          self.reset_x_y()
  def reset_x_y(self):
    if not self.if_shot:
      self.x = player.x+20
      self.y = player.y-5
aliens = []
for i in range(0, 2):
  alist = []
  for j in range(0, 2):
    a = Alien(i*30+i*10, j*30+j*10, 30, 30, alien)
    alist.append(a)
  aliens.append(alist)
right = True
godown = False
player = Ship(280, 560, 40, 40, ship)
bullet = Bullet(300, 555, False)
k = shdw.GUI_keys
while True:
  screen.fill((0, 0, 0))
  player.draw()
  bullet.draw()
  for i in aliens:
    for j in i:
      if godown:
        j.alien_down(-5)
      if right:
        j.move_alien(5)
      else:
        j.move_alien(-5)
      j.draw()
  bullet.move()
  if aliens == []:
    screen.fill((0, 0, 0))
    shdw.show_text(screen, 'GAME OVER', 0, 0, (255, 0, 0), size=50)
    shdw.GUI.delay.update()
    shdw.GUI.time.delay(5000)
    exit()
  if godown:
    godown = False
  if aliens[-1][0].x >= 570:
    right = False
    godown = True
  elif aliens[0][0].x <= 0:
    right = True
    godown = True
  for event in shdw.GUI.event.get():
    if event.type == k.KEYDOWN:
      if event.key == k.K_LEFT:
        player.x -= 20
        if player.x >= 560:
          player.x = 560
        bullet.update_x_y()
      if event.key == k.K_RIGHT:
        player.x += 20
        if player.x <= 0:
          player.x = 0
        bullet.update_x_y()
      if event.key == k.K_SPACE:
        bullet.if_shot = True
  shdw.GUI.time.delay(50)
  shdw.GUI.display.update()