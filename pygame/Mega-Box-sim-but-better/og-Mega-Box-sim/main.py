def remover(file, whattoremove):
  # code to delete a particular 
  # data from a file 

  # open file in read mode 
  f = open(file, "r")
	  # read data line by line 
  data = f.readlines() 	
  # open file in write mode 
  with open(file, "w") as f:	
	  for line in data:
		  # condition for data to be deleted 
		  if line.strip("\n") == whattoremove: 
			  f.write('')

def run():
  import random as r
  import time as t
  limit = 100
  score = 0
  name = input('WHats ur name?: ')
  while limit > 0:
    limit -= 1
    a = r.randint(1, 5)
    b = int(input('\033[0;0mChoose a number between 1 and 5: '))
    if a == b:
      print('You got a brawler!')
      t.sleep(0.5)
      c = r.randint(1, 15)
      if c <= 5:
        print('\033[0;32mYou got a rare.')
        suprrs = ['Rosa', 'El Primo', 'Barley', 'Poco']
        t.sleep(0.05)
        choiz = r.choice(suprrs)
        print('You got: ' + choiz)
        score += 2
        suprrs.remove(choiz)
      elif c > 5 and c <= 9:
        print('\033[0;34mYou got a super rare.')
        suprrs = ['Carl', 'Penny', 'Rico', 'Darryl', 'Jacky']
        t.sleep(0.05)
        choiz = r.choice(suprrs)
        print('You got: ' + choiz)
        score += 2
        suprrs.remove(choiz)
      elif c > 9 and c <= 12:
        print('\033[0;35mYou got an epic!')
        t.sleep(0.05)
        epics = ['Piper', 'Frank', 'Nani', 'Pam', 'Bea', 'Bibi', 'Gale']
        choiz = r.choice(epics)
        print('You got: ' + choiz)
        score += 3
        epics.remove(choiz)
      elif c > 12 and c <= 14:
        print('\033[0;31mYou got a mythic!')
        mythics = ['Max', 'Tara', 'Mortis', 'Gene', 'Mr. P', 'Sprout', 'Surge']
        t.sleep(0.05)
        choiz = r.choice(mythics)
        print('You got: ' + choiz)
        score += 5
        mythics.remove(choiz)
      elif c > 14:
        yellow = '\033[1;33m'
        print(yellow + '    _  _    _                _')
        print(yellow + '|  |_ | _  |_ |\\ | |\\  /_\\  |_| \/ |')
        print(yellow + '|_ |_ |__| |_ | \\| |/ /   \\ |\\   | .')
        legends = ['Crow', 'Spike', 'Sandy', 'Leon', 'Colette']
        t.sleep(0.05)
        choiz = r.choice(legends)
        print('You got: ' + choiz)
        score += 10
        legends.remove(choiz)
    else:
      print('YOU GOT NOTHING.')
  print('\033[0;0m Your score: ' + str(score))
  f = open('high score.txt')
  g = int(f.readline())
  if score > g:
    f = open('high score.txt', 'w')
    fi = open('high score name.txt', 'w')
    f.write(str(score))
    fi.write(name)
    f.close()
    fi.close()
  f = open('high score.txt')
  print('Highest Score: ' + f.readline())
  f.close()
  if name != 'None':
    openup = open('scores.txt', 'a')
    openup.write('{0}: {1}\n'.format(name, score))
run()