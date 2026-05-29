def sepper():
  print('--------------')
class polar:
  pwrlvl = 1
  health = 5000
  speed = 'Very Fast'
  type = 'Fighter'
  rarity = 'Mythic'
  class attack:
    name = 'Pole Swipe'
    descrip = 'Polar swipes through the air.'
    damage = 1000
    range = 'Normal'
    reloadSpeed = 'Fast'
    def all():
      print('Name: ' + polar.attack.name)
      print('Description: ' + polar.attack.descrip)
      print('Damage: ' + str(polar.attack.damage))
      print('Range: ' + polar.attack.range)
      print('Reload Speed: ' + polar.attack.reloadSpeed)
  class super:
    name = 'Pole Slam'
    descrip = 'Polar slams his pole on the ground, creating 4 shockwaves around him and slowing down who they hit!'
    damage = 1750
    range = 'Normal'
    def all():
      print('Name: ' + polar.super.name)
      print('Description: ' + polar.super.descrip)
      print('Stick Damage: ' + str(polar.super.damage))
      print('Range: ' + polar.attack.range)
  class gadget:
    name = 'Pole Split'
    descrip = 'Polar splits his pole and gets double range and half damage for each stick! Lasts for 4 seconds.'
    cpm = 3
    def all():
      print('Name: ' + polar.gadget.name)
      print('Description: ' + polar.gadget.descrip)
      print('Charges per match: ' + str(polar.gadget.cpm))
  class starpower:
    name = '360 Poles'
    descrip = 'Polar now spins around for his attack and gadget.'
    def all():
      print('Name: ' + polar.starpower.name)
      print('Decription: ' + polar.starpower.descrip)
  def all():
    print('Stats')
    print('Health: ' + str(polar.health))
    print('Speed: ' + polar.speed)
    print('Type: ' + polar.type)
    print('Rarity: ' + polar.rarity)
    sepper()
    print('Attack')
    polar.attack.all()
    sepper()
    print('Super')
    polar.super.all()
    sepper()
    print('Gadgets')
    polar.gadget.all()
    sepper()
    print('Star powers')
    polar.starpower.all()
  def upgrade():
    polar.pwrlvl += 1
    polar.health += 250
    polar.attack.damage += 750