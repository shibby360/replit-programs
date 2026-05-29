import requests
import os
try:
  import shdw
except ModuleNotFoundError:
  os.system('pip install Shdw')
  import shdw
true = True
false = False
null = None
u = requests.get('https://api.brawlapi.com/v1/brawlers')
alls = eval(u.text)
size = 300
screen = shdw.init_pygame(size, size, 'brawlers')
sqs = int(size/5)
for i in alls['list']:
  i['imageUrl2'] = 'brawlers/{0}_Skin-Default.png'.format(i['name'].replace(' ', '_'))
def getBrawlerDict(verif):
  if type(verif) == int:
    for i in alls['list']:
      if i['id'] == verif:
        return i
        break
  elif type(verif) == str:
    for i in alls['list']:
      if i['name'] == verif:
        return i
        break
  return __import__('random').choice(alls['list'])

def getGorSP(brawlername, name, type):
  brawler = getBrawlerDict(brawlername)
  for i in brawler[type]:
    if i['name'] == name:
      return i
      break

def addBrawler(dict):
  alls['list'].append(dict)

name = input('Which brawler?: ')
attr = input('What attribute?: ').lower()
if attr == 'rand':
  attr = __import__('random').choice(['profile', 'body', 'pin'])
brawler = getBrawlerDict(name)
if attr == 'profile':
  img = shdw.GUI.image.url_load(brawler['imageUrl'])
  while True:
    img = shdw.GUI_change.scale(img, (size, size))
    screen.blit(img, (size*0/5, size*0/5))
    shdw.GUI.display.update()
elif attr == 'body':
  img = shdw.GUI.image.load(brawler['imageUrl2'])
  while True:
    img = shdw.GUI_change.scale(img, (size, size))
    screen.blit(img, (size*0/5, size*0/5))
    shdw.GUI.display.update()
elif attr == 'pin':
  img = shdw.GUI.image.url_load(brawler['imageUrl3'])
  while True:
    img = shdw.GUI_change.scale(img, (size, size))
    screen.blit(img, (size*0/5, size*0/5))
    shdw.GUI.display.update()
elif attr == 'gadget':
  gadget = input('Which one?: ')
  attr = input('What attribute from the gadget?: ')
  print(getGorSP(name, gadget, 'gadgets')[attr])
elif attr == 'star powers':
  starpow = input('Which one?: ')
  attr = input('What attribute from the star power?: ')
  print(getGorSP(name, starpow, 'starPowers')[attr])
else:
  print(brawler[attr])