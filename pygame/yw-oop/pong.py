import shdw
screen = shdw.init_pygame(600, 600, 'pongg')
k = shdw.GUI_keys
c = shdw.GUI_colors
class Ball:     
  def __init__(self):        
    self.x = 300    
    self.y = 300         
    self.color = c.red
    self.radius = 20
    self.xmove = 0     
    self.ymove = -10
    self.rect = None
  def draw(self):
    self.rect = shdw.GUI_out.circle(screen, self.color, (self.x, self.y), self.radius)
ball = Ball()
class Paddle:     
  def __init__(self, color, x, y):         
    self.color = color         
    self.x = x
    self.y = y    
    self.width = 20     
    self.height = 200
    self.up = False
    self.down = False   
    self.score = 0         
    self.speed = 10
    self.rect = None
  def draw(self):
    self.rect = shdw.GUI_out.rect(screen, self.color, (self.x, self.y, self.width, self.height))
  def ShowScore(self, x, y):         
    font= shdw.GUI.font.SysFont('freesans', 32)         
    msg = font.render(str(self.score), True, self.color)         
    screen.blit(msg, (x,y)) 
p1 = Paddle(c.blue, 10, 200)
p2 = Paddle(c.green, 570, 200)
st = True
while True:
  screen.fill(c.black)
  ball.draw()
  p1.draw()
  p1.ShowScore(50, 50)
  p2.draw()
  p2.ShowScore(550, 50)
  ball.y += ball.ymove
  ball.x += ball.xmove
  #boundaris
  if ball.y < ball.radius:
    ball.ymove = 10
    if st:
      blmv = shdw.r.choice('rl')
      if blmv == 'r':
        ball.xmove = -8
      else:
        ball.xmove = 8
      st = False
  if ball.y > 600-ball.radius:
    ball.ymove = -10
  if ball.x < ball.radius:
    p2.score += 1
    ball.x = 300
    ball.xmove = 0
    ball.y = 300
    ball.ymove = -10
    shdw.GUI.time.delay(1000)
  if ball.x > 600-ball.radius:
    p1.score += 1
    ball.x = 300
    ball.xmove = 0
    ball.ymove = -10
    ball.y = 300
    shdw.GUI.time.delay(1000)
  if ball.rect.colliderect(p1.rect):
    ball.xmove = 8
  if ball.rect.colliderect(p2.rect):
    ball.xmove = -8
  shdw.GUI.display.update()
  shdw.GUI.time.delay(50)
  for i in shdw.GUI_events.get():
    if i.type == k.KEYDOWN:
      if i.key == k.K_UP:
        p2.y -= p2.speed
      elif i.key == k.K_DOWN:
        p2.y += p2.speed
      if i.key == k.K_w:
        p1.y -= p1.speed
      elif i.key == k.K_s:
        p1.y += p1.speed
    if i.type == k.QUIT:
      shdw.GUI.quit()
      exit()