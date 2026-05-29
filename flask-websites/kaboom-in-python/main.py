import kablooey as k
import random as rand
import markdown
import os
os.system('pip install pygments')
os.system('clear')
#Inserting stuff to docs.html
os.system('pygmentize -S vim -f html -a .codehilite  > codehilite.css')
extrastyles = '''h1, h3, h5, p { font-family: sans-serif; color: white; }
h3 code { color: rgb(228, 123, 0); background-color: rgb(169, 169, 169, 0.5); border-radius: 15px; padding: 5px; }
body { background-color: black; }
'''
mdd = markdown.markdown(open('README.md').read(), extensions=['extra', 'fenced_code', 'codehilite'])
open('codehilite.css', 'a').write(extrastyles)
@k.app.route('/docs')
def doccs():
  return k.render_template('docs.html', doccies=mdd)
@k.app.route('/site')
def sitte():
  return k.render_template('docs.html', doccies=mdd)
#Packaging
def pkg(dell):
  if dell:
    import shutil
    shutil.rmtree('build')
    shutil.rmtree('dist')
  os.system('python setup.py sdist bdist_wheel')
  os.system('twine upload dist/*')
# pkg(1)
def tst():
  import test
tst()
#This is where the code really starts
k.kablooey('Kaboom... in python!')
k.add(k.Text('KABOOOOOOOOOOOOOOOOM.PY!', size=70, font='papyrus', color=(255, 0, 0)), 0, 0)
kab = k.add(k.Sprite('kablooey.png', 300, 300), 0, 100, comps=[k.ArrowMove()])
class Colorss:
  def __init__(self, ScreenObj=None):
    self.objattr = 'coloring'
    self.iss = 'colorer'
    self.screenobj = ScreenObj
  def color(self, colors):
    self.screenobj.add_styles_string(f"background-color:{colors};")
r = k.Rect(50, 50)
a = k.add(r, 0, 0, comps=[Colorss()])
print('')
@k.action()
def actionn():
  a.coloring.color(f'rgb({rand.randint(0, 255)}, {rand.randint(0, 255)}, {rand.randint(0, 255)})')
k.run()
while True:
  for action in k.actions:
    action()