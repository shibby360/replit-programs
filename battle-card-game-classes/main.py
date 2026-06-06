red = '\x1b[1;31m'
cyan = '\x1b[1;36m'
black = '\x1b[1;30;47m'
yellow = '\x1b[1;33;44m'
purple = '\x1b[1;35m'
blapur = '\x1b[1;30;45m'
crystal = '\x1b[0;35;47m'
emerald = '\x1b[1;32m'
restore = '\x1b[0;0m'
gray = '\x1b[2;37m'
yelpur = '\x1b[0;33;45m'
nope = red + '⚠️ Invalid Input Given⚠️' + restore
#Evolove Adds All properties by 10 and the CP goes to the next level.
#https://docs.google.com/spreadsheets/d/1t_5Gll5l7Cjgrc-4c23Zx8DIw845Zc0bA88LYixqERU/edit#gid=0
class dudes:
  def everything():
    dudes.light.allofem()
    print(restore + '------------------')
    print('------------------')
    print('------------------')
    dudes.dark.allofem()
    print(restore + '------------------')
    print('------------------')
    print('------------------')
    dudes.neutral.allofem()
    print(restore + '------------------')
    print('------------------')
    print('------------------')
    dudes.double.allofem()
  class light:
    def allofem():
      dudes.light.firy.all()
      print('------------------')
      print('------------------')
      dudes.light.earth_boom.all()
      print('------------------')
      print('------------------')
      dudes.light.geek.all()
      print('------------------')
      print('------------------')
      dudes.light.boss.prall()
    class firy:
      def all():
        print(red + 'Firy')
        print(restore + 'Moves: ')
        dudes.light.firy.move1.all()
        dudes.light.firy.move2.all()
        dudes.light.firy.move3.all()
        print('------------------')
        print('Avatar: ')
        dudes.light.firy.avatar.show()
        print(restore + 'Health: ' + str(dudes.light.firy.health))
        print('Type: ' + dudes.light.firy.type)
        print('CP: ' + str(dudes.light.firy.cp))
      class move1:
        name = 'Ember'
        healing = emerald + str(10)
        intheal = 10
        damage = nope
        def all():
          print(dudes.light.firy.move1.name)
          print(emerald + '+' + str(dudes.light.firy.move1.healing), 'health')
      class move2:
        name = 'Match Attack'
        damage = 20
        def all():
          print(restore + dudes.light.firy.move2.name)
          print(str(dudes.light.firy.move2.damage) + ' damage')
      class move3:
        name = 'Fire Blast'
        damage = 30
        def all():
          print(dudes.light.firy.move3.name)
          print(str(dudes.light.firy.move3.damage) + ' damage')
      class avatar:
        name = red + 'Blazing Whip'
        damage = 60
        def show():
          print(red + '~~~~~~~~~~~~')
          print(dudes.light.firy.avatar.name)
          print(str(dudes.light.firy.avatar.damage) + ' damage')
          print(red + '~~~~~~~~~~~')
      health = 100
      cp = 3
      type = 'Damager'
    class earth_boom:
      def all():
        print(cyan + 'Earth Boom')
        print(restore + 'Moves: ')
        dudes.light.earth_boom.move1.all()
        dudes.light.earth_boom.move2.all()
        dudes.light.earth_boom.move3.all()
        print('------------------')
        print('Avatar: ')
        dudes.light.earth_boom.avatar.show()
        print(restore + 'Health:' + str(dudes.light.earth_boom.health))
        print('Type: ' + dudes.light.earth_boom.type)
        print('CP: ' + str(dudes.light.earth_boom.cp))
      class move1:
        name = 'Rocker'
        damage = 15
        def all():
          print(restore + dudes.light.earth_boom.move1.name)
          print(str(dudes.light.earth_boom.move1.damage), 'damage')
      class move2:
        name = 'Stone Shield'
        damage = nope
        sheildity = 25
        duration = 5
        def all():
          print(dudes.light.earth_boom.move2.name)
          print(str(dudes.light.earth_boom.move2.sheildity),'Sheildness')
          print(dudes.light.earth_boom.move2.duration, 'Turns')
      class move3:
        name = 'Quake'
        damage = 35
        def all():
          print(dudes.light.earth_boom.move3.name)
          print(str(dudes.light.earth_boom.move3.damage), 'damage')
      class avatar:
        name = cyan + 'Earth Blast'
        damage = 65
        def show():
          print(cyan + '>>>>>>>>>>>>')
          print(dudes.light.earth_boom.avatar.name)
          print(str(dudes.light.earth_boom.avatar.damage), 'damage')
          print(cyan + '>>>>>>>>>>>>')
      health = 150
      cp = 5
      type = 'Damager'
    class geek:
      def all():
        print(black + 'Geek')
        print(restore + 'Moves: ')
        dudes.light.geek.move1.all()
        dudes.light.geek.move2.all()
        dudes.light.geek.move3.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.light.geek.avatar.show()
        print(restore + 'Health:' + str(dudes.light.geek.health))
        print('Type: ' + dudes.light.geek.type)
        print('CP: ' + str(dudes.light.geek.cp))
      class move1:
        name = 'See the future'
        descrip = 'Wiew the top 5 cards of the draw pile.'
        def all():
          print(restore + dudes.light.geek.move1.name)
          print(dudes.light.geek.move1.descrip)
      class move2:
        name = 'Binarify'
        damage = 40
        descrip = nope
        def all():
          print(dudes.light.geek.move2.name)
          print(dudes.light.geek.move2.damage, 'damage')
      class move3:
        name = crystal + 'All change'
        descrip = crystal + 'Shuffle the draw pile.'
        def all():
          print(dudes.light.geek.move3.name)
          print(dudes.light.geek.move3.descrip)
      class avatar:
        name = 'Alter the Future'
        descrip = 'View and change the top 5 cards of the draw pile.'
        def show():
          print(black + '?-----?----?')
          print(dudes.light.geek.avatar.name)
          print(dudes.light.geek.avatar.descrip)
          print(black + '?-----?---?')
      health = 200
      cp = 8
      type = 'Descripped'
    class boss:
      def prall():
        print(yellow + 'Name: ' + dudes.light.boss.name)
        print(yellow + 'Moves: ')
        dudes.light.boss.move1.all()
        dudes.light.boss.move2.all()
        dudes.light.boss.move3.all()
        print('------------------')
        print('Special Attack: ')
        dudes.light.boss.spec_atk.show()
        print(yellow + 'Health:' + str(dudes.light.boss.health))
      name = yellow + 'Whiz'
      class move1:
        name = yellow + 'Sun blast'
        damage = 50
        def all():
          print(dudes.light.boss.move1.name)
          print(yellow + str(dudes.light.boss.move1.damage), 'damage')
      class move2:
        name = yellow + 'Electro'
        damage = 100
        def all():
          print(dudes.light.boss.move2.name)
          print(yellow + str(dudes.light.boss.move2.damage), 'damage')
      class move3:
        name = yellow + 'Spell Strike'
        damage = 150
        def all():
          print(dudes.light.boss.move3.name)
          print(yellow + str(dudes.light.boss.move3.damage), 'damage')
      class spec_atk:
        name = 'Wand of Light'
        damage = yellow + str(300)
        intdamage = 300
        def show():
          print(yellow + '~>-~>-~>-~>-~>-~>-')
          print(dudes.light.boss.spec_atk.name)
          print(yellow + dudes.light.boss.spec_atk.damage + ' damage')
          print(yellow + '~>-~>-~>-~>-~>-')
      health = yellow + str(500)
      inthealth = 500
  class dark:
    def allofem():
      dudes.dark.spyder.all()
      print('------------------')
      print('------------------')
      dudes.dark.snakes.all()
      print('------------------')
      print('------------------')
      dudes.dark.batty.all()
      print('------------------')
      print('------------------')
      dudes.dark.boss.prall()
    class spyder:
      def all():
        print(purple + 'Spyder')
        print(restore + 'Moves: ')
        dudes.dark.spyder.move1.all()
        dudes.dark.spyder.move2.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.dark.spyder.avatar.show()
        print(restore + 'Health:' + str(dudes.dark.spyder.health))
        print('Type: ' + dudes.dark.spyder.type)
        print('CP: ' + str(dudes.dark.spyder.cp))
      class move1:
        name = 'Web whip'
        damage = 30
        def all():
          print(restore + dudes.dark.spyder.move1.name)
          print(dudes.dark.spyder.move1.damage, 'damage')
      class move2:
        name = 'Flytrap'
        damage = nope
        healing = emerald + str(40)
        intheal = 40
        def all():
          print(dudes.dark.spyder.move2.name)
          print(emerald + '+' + dudes.dark.spyder.move2.healing, 'health')
      class move3:
        name = nope
        damage = nope
        def all():
            print(nope)
      class avatar:
        name = 'Web wrap'
        damage = 50
        def show():
          print(purple + ':::::::::::')
          print(dudes.dark.spyder.avatar.name)
          print(dudes.dark.spyder.avatar.damage, 'damage')
          print(purple + '::::::::::')
      health = 250
      cp = 3
      type = 'Damager'
    class snakes:
      def all():
        print(purple + 'Snakes')
        print(restore + 'Move: ')
        dudes.dark.snakes.move1.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.dark.snakes.avatar.show()
        print(restore + 'Health:' + str(dudes.dark.snakes.health))
        print('Type: ' + dudes.dark.snakes.type)
        print('CP: ' + str(dudes.dark.snakes.cp))
      class move1:
        name = 'Bite'
        damage = 50
        def all():
          print(restore + dudes.dark.snakes.move1.name)
          print(dudes.dark.snakes.move1.damage, 'damage')
      class move2:
        name = nope
        damage = nope
        def all():
          print(nope)
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class avatar:
        name = 'Rattler'
        damage = 60
        def show():
          print(purple + '////////////')
          print(dudes.dark.snakes.avatar.name)
          print(dudes.dark.snakes.avatar.damage, 'damage')
          print(purple + '///////////')
      health = 300
      cp = 5
      type = 'Damager'
    class batty:
      def all():
        print(purple + 'Batty')
        print(restore + 'Moves: ')
        dudes.dark.batty.move1.all()
        dudes.dark.batty.move2.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.dark.batty.avatar.show()
        print(restore + 'Health:' + str(dudes.dark.batty.health))
        print('Type: ' + dudes.dark.batty.type)
        print('CP: ' + str(dudes.dark.batty.cp))
      class move1:
        name = 'Raise the dead'
        descrip = 'Take 5 cards from the draw pile.'
        def all():
          print(restore + dudes.dark.batty.move1.name)
          print(dudes.dark.batty.move1.descrip)
      class move2:
        name = 'Moth chomp'
        descrip = nope
        healing = emerald + str(50)
        intheal = 50
        def all():
          print(dudes.dark.batty.move2.name)
          print(emerald + '+' + str(dudes.dark.batty.move2.healing), 'health')
      class move3:
        name = nope
        descrip = nope
        def all():
            print(nope)
      class avatar:
        name = purple + 'Swoop'
        damage = 70
        descrip = nope
        def show():
          print(purple + ';;;;;;;;;;;;;')
          print(dudes.dark.batty.avatar.name)
          print(purple + str(dudes.dark.batty.avatar.damage), 'damage')
          print(purple + ';;;;;;;;;;;;')
      health = 350
      cp = 8
      type = 'Descripped'
    class boss:
      def prall():
        print(blapur + 'Name: ' + dudes.dark.boss.name)
        print(blapur + 'Moves: ')
        dudes.dark.boss.move1.all()           
        dudes.dark.boss.move2.all()
        print('------------------')
        print('Special Attack: ')
        dudes.dark.boss.spec_atk.show()
        print(blapur + 'Health:' + str(dudes.dark.boss.health))
      name = blapur + 'Skulls'
      class move1:
        name = blapur + 'Acid pool'
        damage = 100
        def all():
          print(dudes.dark.boss.move1.name)
          print(blapur + str(dudes.dark.boss.move1.damage), 'damage')
      class move2:
        name = blapur + 'Tornado attack'
        damage = 150
        def all():
          print(dudes.dark.boss.move2.name)
          print(blapur + str(dudes.dark.boss.move2.damage), 'damage')
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class spec_atk:
        name = blapur + 'Dark Blast'
        damage = 350
        def show():
          print(blapur + ':/;:/;:/;:/;:/;:/;')
          print(dudes.dark.boss.spec_atk.name)
          print(blapur + str(dudes.dark.boss.spec_atk.damage), 'damage')
          print(blapur + ':/;:/;:/;:/;:/;')
      health = blapur + str(550)
      inthealth = 550
  class neutral:
    def allofem():
      dudes.neutral.primo.all()
      print('------------------')
      print('------------------')
      dudes.neutral.kicker.all()
      print('------------------')
      print('------------------')
      dudes.neutral.blocker.all()
      print('------------------')
      print('------------------')
      dudes.neutral.boss.prall()
    class primo:
      def all():
        print(gray + 'Primo')
        print(restore + 'Moves: ')
        dudes.neutral.primo.move1.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.neutral.primo.avatar.show()
        print(restore + 'Health:' + str(dudes.neutral.primo.health))
        print('Type: ' + dudes.neutral.primo.type)
        print('CP: ' + str(dudes.neutral.primo.cp))
      class move1:
        name = 'Punch'
        damage = 20
        def all():
          print(dudes.neutral.primo.move1.name)
          print(gray + str(dudes.neutral.primo.move1.damage), 'damage')
      class move2:
        name = nope
        damage = nope
        def all():
          print(nope)
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class avatar:
        name = 'Karate Punch'
        damage = 200
        def show():
          print(gray + '==)==)==)==)')
          print(dudes.neutral.primo.avatar.name)
          print(gray + str(dudes.neutral.primo.avatar.damage), 'damage')
          print(gray + '==)==)==)==)')
      health = 100
      type = 'Damager'
      cp = 3
    class kicker:
      def all():
        print(gray + 'Kicker')
        print(restore + 'Moves: ')
        dudes.neutral.kicker.move1.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.neutral.kicker.avatar.show()
        print(restore + 'Health:' + str(dudes.neutral.kicker.health))
        print('Type: ' + dudes.neutral.kicker.type)
        print('CP: ' + str(dudes.neutral.kicker.cp))
      class move1:
        name = 'Kick'
        damage = 30
        def all():
          print(dudes.neutral.kicker.move1.name)
          print(gray + str(dudes.neutral.kicker.move1.damage), 'damage')
      class move2:
        name = nope
        damage = nope
        def all():
          print(nope)
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class avatar:
        name = 'Karate Kick'
        damage = 300
        def show():
          print(gray + '==>==>==>==>')
          print(dudes.neutral.kicker.avatar.name)
          print(gray + str(dudes.neutral.kicker.avatar.damage), 'damage')
          print(gray + '==>==>==>==>')
      health = 100
      type = 'Damager'
      cp = 5
    class blocker:
      def all():
        print(gray + 'Blocker')
        print(restore + 'Moves: ')
        dudes.neutral.blocker.move1.all()
        dudes.neutral.blocker.move2.all()
        print(restore + '------------------')
        print('Avatar: ')
        dudes.neutral.blocker.avatar.show()
        print(restore + 'Health:' + str(dudes.neutral.blocker.health))
        print('Type: ' + dudes.neutral.blocker.type)
        print('CP: ' + str(dudes.neutral.blocker.cp))
      class move1:
        name = 'Hand Block'
        damage = nope
        sheildity = 70
        duration = 1
        def all():
          print(dudes.neutral.blocker.move1.name)
          print(str(dudes.neutral.blocker.move1.sheildity),'Sheildness')
          print(dudes.neutral.blocker.move1.duration, 'Turns')
      class move2:
        name = 'Leg Block'
        damage = nope
        sheildity = 80
        duration = 5
        def all():
          print(dudes.neutral.blocker.move2.name)
          print(str(dudes.neutral.blocker.move2.sheildity),'Sheildness')
          print(dudes.neutral.blocker.move2.duration, 'Turns')
      class move3:
        name = 'Block hit'
        damage = 50
        def all():
          print(dudes.neutral.blocker.move3.name)
          print(gray + str(dudes.neutral.blocker.move3.damage), 'damage')
      class avatar:
        name = 'Retaliate'
        damage = nope
        descrip = 'The next time Blocker is hit, he returns the damage.'
        def show():
          print(gray + '}}}}}}}}}}}}')
          print(dudes.neutral.blocker.avatar.name)
          print(gray + str(dudes.neutral.blocker.avatar.descrip))
          print(gray + '}}}}}}}}}}}}')
      health = 100
      type = 'Damager/Descripped'
      cp = 8
    class boss:
      def prall():
        print(gray + 'Name: ' + dudes.neutral.boss.name)
        print(gray + 'Moves: ')
        dudes.neutral.boss.move1.all()           
        dudes.neutral.boss.move2.all()
        print('------------------')
        print('Special Attack: ')
        dudes.neutral.boss.spec_atk.show()
        print(gray + 'Health:' + str(dudes.neutral.boss.health))
      name = gray + 'No Boss'
      class move1:
        name = gray + 'Ultra Punch'
        damage = 30
        def all():
          print(dudes.neutral.boss.move1.name)
          print(gray + str(dudes.neutral.boss.move1.damage), 'damage')
      class move2:
        name = gray + 'Ultra Kick'
        damage = 70
        def all():
          print(dudes.neutral.boss.move2.name)
          print(gray + str(dudes.neutral.boss.move2.damage), 'damage')
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class spec_atk:
        name = gray + 'Karate Fury'
        damage = 150
        def show():
          print(gray + '==)>}==)>}==)>}')
          print(dudes.neutral.boss.spec_atk.name)
          print(gray + str(dudes.neutral.boss.spec_atk.damage), 'damage')
          print(gray + '==)>}==)>}==)>}')
      health = gray + str(300)
      inthealth = 300
  class double:
    def allofem():
      dudes.double.boss.prall()
    class boss:
      def prall():
        print(yelpur + 'Name: ' + dudes.double.boss.name)
        print('------------------')
        print('Special Attack: ')
        dudes.double.boss.spec_atk.show()
        print(yelpur + 'Health:' + str(dudes.double.boss.health))
      name = yelpur + 'Double Boss'
      class move1:
        name = nope
        damage = nope
        def all():
          print(nope)
      class move2:
        name = nope
        damage = nope
        def all():
          print(nope)
      class move3:
        name = nope
        damage = nope
        def all():
          print(nope)
      class spec_atk:
        name = yelpur + 'Dark and light Fury'
        damage = 400
        def show():
          print(yelpur + '888888888888888')
          print(dudes.double.boss.spec_atk.name)
          print(yelpur + str(dudes.double.boss.spec_atk.damage), 'damage')
          print(yelpur + '888888888888888')
      health = yelpur + str(700)
      inthealth = 700

class othrcrds:
  def allcrds():
    pass
  class dudetype:
    def all():
      othrcrds.dudetype.move.all()
      print('------------------')
      othrcrds.dudetype.avatar.all()
      print('------------------')
      othrcrds.dudetype.combine.all()
      print('------------------')
      othrcrds.dudetype.evolve.all()
    class move:
      def all():
        print('Name: Move')
        print('Description: ' + othrcrds.dudetype.move.descrip)
      descrip = 'Use a move of the current dude in your set.'
    class avatar:
      def all():
        print('Name: Avatar')
        print('Description: ' + othrcrds.dudetype.avatar.descrip)
      descrip = 'Use the avatar of the current dude in your set.'
    class combine:
      def all():
        print('Name: Combine')
        print('Description: ' + othrcrds.dudetype.combine.descrip)
      descrip = 'Combine all your dudes of a single type. Add the health and move damages together.'
    class evolve:
      def all():
        print('Name: Evolve')
        print('Description: ' + othrcrds.dudetype.evolve.descrip)
      descrip = 'Evolve the current dude in your set.'
  class events:
    def all():
      print('      Personals      ')
      print('---------------------')
      othrcrds.events.personals.light_overload.all()
      print('---------------------')
      othrcrds.events.personals.dark_magic_infection.all()
      print('---------------------')
      print('      Globals        ')
      print('---------------------')
      othrcrds.events.globals.double_spinner.all()
      print('---------------------')
      othrcrds.events.globals.ultimate_giveaway.all()
      print('---------------------')
      othrcrds.events.globals.tornado.all()
    class personals:
      def all():
        othrcrds.events.personals.light_overload.all()
        print('---------------------')
        othrcrds.events.personals.dark_magic_infection.all()
      class light_overload:
        def all():
          print('Name: Light Overload')
          print('Type: ' + othrcrds.events.personals.light_overload.type)
          print('Description: ' + othrcrds.events.personals.light_overload.descrip)
        type = 'light'
        descrip = 'Discard all your dark cards. If you draw a dark card, immediately discard it.'
      class dark_magic_infection:
        def all():
          print('Name: Dark magic infection')
          print('Type: ' + othrcrds.events.personals.dark_magic_infection.type)
          print('Description: ' + othrcrds.events.personals.dark_magic_infection.descrip)
        type = 'dark'
        descrip = 'Discard all your light dark cards. If you draw a light card, immediately discard it.'
    class globals:
      def all():
        print('---------------------')
        othrcrds.events.globals.double_spinner.all()
        print('---------------------')
        othrcrds.events.globals.ultimate_giveaway.all()
        print('---------------------')
        othrcrds.events.globals.tornado.all()
      class double_spinner:
        def all():
          print('Name: Double spinner')
          print('Type: ' + othrcrds.events.globals.double_spinner.type)
          print('Description: ' + othrcrds.events.globals.double_spinner.descrip)
        type = 'double'
        descrip = 'Everyone except for you chooses a card in their deck.'
      class ultimate_giveaway:
        def all():
          print('Name: Ultimate giveaway')
          print('Type: ' + othrcrds.events.globals.ultimate_giveaway.type)
          print('Description: ' + othrcrds.events.globals.ultimate_giveaway.descrip)
        type = 'double'
        descrip = 'This is just like double spinner, except the cards discarded in double spinner go to the person who had this card.'
      class tornado:
        def all():
          print('Name: Tornado')
          print('Type: ' + othrcrds.events.globals.tornado.type)
          print('Description: ' + othrcrds.events.globals.tornado.descrip)
        type = 'neutral'
        descrip = 'Everyone gives their cards to the player after them.'
  class lights:
    def all():
      ''
  class darks:
    def all():
      ''
''''othrcrds.events.all()'''
#Dudes: everything(), Type: allofem(), Specif dudes: all(), Boss: prall(), Moves: all(), Ultras: show()

def asker():
  one = input('Which thing?: ')
  two = input('What in that thing?: ')
  three = input('What in that thing?: ')
  four = input('What in that thing?: ')
  five = input('What in that thing?: ')

  alls = [one, two, three, four, five]
  evl = []
  for i in alls:
    if i != '':
      evl.append(i)

  if len(evl) == 1:
    elu = eval(evl[0])
  elif len(evl) == 2:
    elu = eval(evl[0] + '.' + evl[1])
  elif len(evl) == 3:
    elu = eval(evl[0] + '.' + evl[1] + '.' + evl[2])
  elif len(evl) == 4:
    elu = eval(evl[0] + '.' + evl[1] + '.' + evl[2] + '.' + evl[3])
  elif len(evl) == 5:
    elu = eval(evl[0] + '.' + evl[1] + '.' + evl[2] + '.' + evl[3] + '.' + evl[4])

  print(elu)

asker()