from flask import Flask, render_template, request, redirect, flash, session
import os
from replit import db
import idgen
try:
  import ShdwDB
except ModuleNotFoundError:
  os.system('pip install shdwdb')
  import ShdwDB

shdb = ShdwDB.retrieve('data', 'data')
shdb.autosave = True
shdb.kts = 'data'
print(shdb)

app = Flask('app')
app.secret_key = 'hereisabunchofmumbojumbo12345689!@$%^&*('

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session.pop('_flashes', None)
    unms = list(shdb.get_row('username').values())
    # pwds = list(shdb.get_row('password').values())
    if request.form['username'] in unms:
      for id in shdb:
        if shdb.get_value(id, 'username') == request.form['username'] and shdb.get_value(id, 'password') == request.form['password']:
          return redirect('/profile/'+id)
      flash('Incorrect password', 'danger')
      return redirect('/login')
    flash('Username not found', 'warning')
    return redirect('/login')
  return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
    shdb.add_column(str(db['id']))
    shdb.set(str(db['id']), 'username', request.form['username'])
    shdb.set(str(db['id']), 'password', request.form['password'])
    allids = shdb.get_row('id')
    id = idgen.gen()
    while id in allids.values():
      id = idgen.gen()
    shdb.set(str(db['id']), 'id', id)
    db['id'] += 1
    return redirect('/profile/'+str(db['id']-1))
  return render_template('signup.html')

@app.route('/signup2', methods=['GET', 'POST'])
def signup2():
  return render_template('')

@app.route('/profile/<numid>')
def profile(numid):
  data = shdb.get_column(numid)
  newdata = {}
  for i in data:
    if i == 'password':
      continue
    if str(type(data[i])).startswith('Observed'):
      newdata[i] = data[i].value
      continue
    newdata[i] = data[i]
  newdata['column'] = numid
  username = data['username']
  return render_template('profile.html', username=username, userdata=newdata)

@app.route('/questions')
def questions():
  return render_template('questionnaire.html')

@app.route('/mealplan')
def mealplan():
  f = open('recipes.json')
  recipes = f.read()
  f.close()
  return render_template('mealplan.html', recipes=recipes)
  
app.run(host='0.0.0.0', port=8080)
