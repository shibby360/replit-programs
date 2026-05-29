import shieldon
import hockeyboy
import polar
import pyfiglet
def greet(what):
  var = pyfiglet.Figlet(font='standard')
  print(var.renderText(what))
def forloop(cmd, howmany):
  for i in range(1, howmany + 1):
    eval(cmd)
def whileloop(cmd, condition):    
  while condition:
    eval(cmd)
def getgadget(who):
  forloop(who + '.' + who + '.upgrade()', 7)
def maxout(who):
  forloop(who + '.' + who + '.upgrade()', 9)

# maxout('hockeyboy')
# maxout('shieldon')
# maxout('polar')
greet('Shieldon')
shieldon.shieldon.all()
greet('Hockey boy')
hockeyboy.hockeyboy.all()
greet('Polar')
polar.polar.all()