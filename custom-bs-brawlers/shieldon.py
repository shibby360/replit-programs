def sepper():
  print('-----------------')
class shieldon:
  pwrlvl = 1
  shieldHealth = 8000
  health = 4000
  totalHealth = shieldHealth + health
  speed = 'Normal'
  type = 'Fighter'
  rarity = 'Legendary'
  class attack:
    name = 'Slam'
    descrip = 'Shieldon swings his shield.'
    damage = 500
    range = 'Normal'
    reloadSpeed = 'Fast'
    def all():
      print('Name: ' + shieldon.attack.name)
      print('Description: ' + shieldon.attack.descrip)
      print('Damage: ' + str(shieldon.attack.damage))
      print('Range: ' + shieldon.attack.range)
      print('Reload Speed: ' + shieldon.attack.reloadSpeed)
  class super:
    name = 'Deflect'
    descrip = 'The next time Shieldon is hit, the damage is deflected to the brawler who attacked him!'
    damage = None
    range = None
    def all():
      print('Name: ' + shieldon.super.name)
      print('Description: ' + shieldon.super.descrip)
      print('Damage: ' + str(shieldon.super.damage))
      print('Range: ' + str(shieldon.super.range))
  class gadget1:
    name = 'Base'
    descrip = 'Shieldon creates a base where he is invisible and cannot be attacked the first time, the next three he teleports to it! He stays in the base for 5 seconds.'
    cpm = 4
    def all():
      print('Name: ' + shieldon.gadget1.name)
      print('Description: ' + shieldon.gadget1.descrip)
      print('Charges per match: ' + str(shieldon.gadget1.cpm))
  class gadget2:
    name = 'Shield Ram'
    descrip = 'Shieldon Runs straight dealing 1000 damage and knocking back anyone in his path!'
    cpm = 3
    def all():
      print('Name: ' + shieldon.gadget2.name)
      print('Description: ' + shieldon.gadget2.descrip)
      print('Charges per match: ' + str(shieldon.gadget2.cpm))
  class starpower1:
    name = 'Shield Crash'
    descrip = 'Whenever Shieldon attacks, he knockbacks the enemy!'
    def all():
      print('Name: ' + shieldon.starpower1.name)
      print('Description: ' + shieldon.starpower1.descrip)
  class starpower2:
    name = 'Shield Seeker'
    descrip = 'Whener Shieldon is defeated, he respawns where ever his shield was broken!'
    def all():
      print('Name: ' + shieldon.starpower2.name)
      print('Description: ' + shieldon.starpower2.descrip)
  def all():
    print('Stats')
    print('Shield Health: ' + str(shieldon.shieldHealth))
    print('Health: ' + str(shieldon.health))
    print('Total Health: ' + str(shieldon.totalHealth))
    print('Speed: ' + shieldon.speed)
    print('Type: ' + shieldon.type)
    print('Rarity: ' + shieldon.rarity)
    sepper()
    print('Attack')
    shieldon.attack.all()
    sepper()
    print('Super')
    shieldon.super.all()
    sepper()
    print('Gadgets')
    shieldon.gadget1.all()
    print('<---->')
    shieldon.gadget2.all()
    sepper()
    print('Star powers')
    shieldon.starpower1.all()
    shieldon.starpower2.all()
  def upgrade():
    shieldon.pwrlvl += 1
    shieldon.health += 1000
    shieldon.shieldHealth += 1000
    shieldon.attack.damage += 250
    shieldon.totalHealth = shieldon.shieldHealth + shieldon.health