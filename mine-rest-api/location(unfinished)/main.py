from flask import Flask, url_for, request
from replit import db
import idgen
import time
import maps
import json
import random as r
def dbget(key):
  return json.loads(db.get_raw(key))
users = dbget('users')
# print(users)
maps = dbget('maps')
# print(maps)
def save():
  db['users'] = users
def getall(dict, prop):
  end = []
  for i in dict:
    end.append(dict[i][prop])
  return end
def addkeytoall(prop, key):
  for i in users:
    users[i][prop] = key
  save()
# addkeytoall('workers', [])
def remkeyfromall(prop):
  for i in users:
    del users[i][prop]
  save()
app = Flask('mine rest api - loc')
mapkey = {0:'nothing', 1:'player'}
shop = json.loads(open('shop.json').read())
workers = json.loads(open('workers.json').read())
@app.route('/')
def index():
  return {} 

@app.route('/create/<name>', methods=['POST'])
def create(name):
  if name in getall(users, 'name'):
    return '{} is a used name'.format(name)
  uid = idgen.gen()
  users[uid] = {
    'name':name,
    'x':0,
    'y':0,
    'coins':50,
    'silver':0,
    'gold':0,
    'xp':0,
    'level':1,
    'joined_at':time.time(),
    'workers':[],
    'inventory':[]
  }
  db['maps'][uid] = maps.default()
  save()
  return {'data':users[uid], 'id':uid}
  
@app.route('/getinfo/<token>')
def getinfo(token):
  return users[token]

@app.route('/getmap/<token>')
def getmap(token):
  return {}

@app.route('/shop', methods=['POST'])
def shopfunc():
  token = request.form['token']
  item = request.form['item']
  if item in shop:
    if workers[item]['cost'] <= users[token][workers[item]['currency']]:
      if workers[item]['type'] == 'worker':
        users[token]['workers'].append(item)
        users[token][shop[item]['currency']] -= shop[item]['cost']
      save()
      return 'Purchase success'
    else:
      return '{} is too expensive'.format(item)
  else:
    return '{} is not in the shop'.format(item)
  
@app.route('/work', methods=['POST'])
def work():
  token = request.form['token']
  result = 'Work success\n'
  for i in users[token]['workers']:
    if workers[i]['type'] == 'worker':
      users[token][workers[i]['data']['income_currency']] += workers[i]['data']['income']
      itemsavail = users[token][workers[i]['data']['items_can_find']]
      ifitem = r.choice([1, 0, 0])
      if ifitem:
        item = r.choice(itemsavail)
        users[token]['inventory'].append(item)
        result += 'You got a(n) ' + item + '!\n'
  save()
  return result

@app.route('/move', methods=['POST'])
def move():
  token = request.form['token']
  x = int(request.form['x'])
  y = int(request.form['y'])
  if x > 5 or x < 0 or y > 5 or y < 0:
    return 'You can\'t move that much'
  users[token][x] += x
  users[token][y] += y
  save()
  return users[token]

# @app.route('/')
app.run(host='0.0.0.0', port=8080)