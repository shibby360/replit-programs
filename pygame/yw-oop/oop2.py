import shdw
import random as r
screen = shdw.init_pygame(500, 500, 'circles')
class Circle:
  def __init__(self, x, y, color):
    self.radius = 10
    self.x = x
    self.y = y
    self.color = color
    self.speed = r.randint(1, 10)
    self.lapcount = 0
    if self.color == clsr.red:
      self.spdx = 1
      self.spdy = 0
    else:
      self.spdx = 0
      self.spdy = 1
  def draw(self):
    shdw.GUI_out.circle(screen, self.color, (self.x, self.y), self.radius)
  def move(self):
    self.x += self.spdx * 1
    if self.x >= 450 or self.x <= 0:
      self.spdx *= -1
    self.y += self.spdy * 1
    if self.y >= 450 or self.y <= 0:
      self.spdy *= -1
    self.draw()
  def check(self, pos):
    if pos != None:
      print(self.x, pos[0])
      if self.x <= pos[0] <= self.x+self.radius and self.y <= pos[1] <= self.y+self.radius:
        print('test')
        self.color = clsr.blue if self.color == clsr.red else clsr.red
        self.spdx, self.spdy = self.spdy, self.spdx
circles = []
clsr = shdw.GUI_colors
cols = [clsr.red, clsr.green, clsr.blue, clsr.pink, clsr.cyan, clsr.yellow]
k = shdw.GUI_keys
for i in range(0, 30):
  circles.append(Circle(r.randint(10, 440), r.randint(10, 440), r.choice([clsr.red, clsr.blue])))
j = None
while True:
  screen.fill(clsr.black)
  for event in shdw.GUI_events.get():
    if event.type == k.MOUSEBUTTONDOWN:
      j = event.pos
  for i in circles:
    i.draw()
    i.move()
    i.check(j)
  j = None    
  shdw.GUI.time.delay(150)
  shdw.GUI.display.update()