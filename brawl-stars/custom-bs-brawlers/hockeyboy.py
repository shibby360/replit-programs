def sepper():
  print('--------------')
class hockeyboy:
  pwrlvl = 1
  health = 2000
  speed = 'Very Fast'
  type = 'Fighter'
  rarity = 'Legendary'
  class attack:
    name = 'Slice'
    descrip = 'Hockey Boy slices through the air, sending a shockwave. Anyone closer to him takes more damage!'
    stickDamage = 3000
    shockDamage = 2000
    range = 'Very Long'
    reloadSpeed = 'Fast'
    def all():
      print('Name: ' + hockeyboy.attack.name)
      print('Description: ' + hockeyboy.attack.descrip)
      print('Stick Damage: ' + str(hockeyboy.attack.stickDamage))
      print('Shock Damage: ' + str(hockeyboy.attack.shockDamage))
      print('Range: ' + hockeyboy.attack.range)
      print('Reload Speed: ' + hockeyboy.attack.reloadSpeed)
  class super:
    name = 'Super Stick'
    descrip = 'Hockey Boy swings his hockey stick, stunning anybody who he hits!'
    damage = 3000
    range = 'Normal'
    def all():
      print('Name: ' + hockeyboy.super.name)
      print('Description: ' + hockeyboy.super.descrip)
      print('Stick Damage: ' + str(hockeyboy.super.damage))
      print('Range: ' + hockeyboy.attack.range)
  class gadget:
    name = 'Mega Charge'
    descrip = 'Hockey boy waits for 1 second, then his super is fully charged!'
    cpm = 3
    def all():
      print('Name: ' + hockeyboy.gadget.name)
      print('Description: ' + hockeyboy.gadget.descrip)
      print('Charges per match: ' + str(hockeyboy.gadget.cpm))
  class starpower:
    name = 'Rush Blast'
    descrip = 'Whenever Hockey boy is attacked, he zooms at the closest enemy, dealing 1500 damage if he crashes, and then attacks!'
    def all():
      print('Name: ' + hockeyboy.starpower.name)
      print('Decription: ' + hockeyboy.starpower.descrip)
  def all():
    print('Stats')
    print('Health: ' + str(hockeyboy.health))
    print('Speed: ' + hockeyboy.speed)
    print('Type: ' + hockeyboy.type)
    print('Rarity: ' + hockeyboy.rarity)
    sepper()
    print('Attack')
    hockeyboy.attack.all()
    sepper()
    print('Super')
    hockeyboy.super.all()
    sepper()
    print('Gadgets')
    hockeyboy.gadget.all()
    sepper()
    print('Star powers')
    hockeyboy.starpower.all()
  def upgrade():
    hockeyboy.pwrlvl += 1
    hockeyboy.health += 250
    hockeyboy.attack.stickDamage += 1000
    hockeyboy.attack.shockDamage += 1000