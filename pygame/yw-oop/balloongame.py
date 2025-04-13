import shdw
screen = shdw.init_pygame(600, 600, 'balon gam')
k = shdw.GUI_keys
c = shdw.GUI_colors
class Balon:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.image = shdw.GUI.image.load('blon.png')
    self.image = shdw.GUI.transform.scale(self.image, (40, 40))
    self.letter = chr(shdw.r.randint(97, 122))
  def draw(self):
    screen.blit(self.image, (self.x, self.y))
    shdw.show_text(screen, self.letter, self.x+20, self.y+20, (255, 255, 255), size=32)
balons = []
score = 0
while True:
  screen.fill((0, 0, 0))
  if score < 0:
    score = 0
  shdw.show_text(screen, str(score), 0, 0, (255, 255, 255), size=64)
  for i in balons:
    i.draw()
  shdw.GUI.display.update()
  for i in shdw.GUI.event.get():
    if i.type == k.KEYDOWN:
      noblon = True
      for j in balons[:]:
        if j.letter == chr(i.key):
          balons.remove(j)
          score += 1
          noblon = False
          break
      if noblon:
        score -= 1
        balons.append(Balon(shdw.r.randint(0, 580), shdw.r.randint(0, 580)))
      if i.key == k.K_PERIOD:
        balons.append(Balon(shdw.r.randint(0, 580), shdw.r.randint(0, 580)))
    if i.type == k.QUIT:
      shdw.GUI.quit()
      exit()