from flask import Flask, request
from threading import Timer
from replit import db
import json
import os
import random as r
os.system('clear')
import idgen
app = Flask('mine rest apiiii')
workernames = ['Bob', 'George', 'Jeff', 'Nick', 'Randy', 'Matthew', 'Steve', 'Alex', 'Nicole', 'Grace', 'Carol', 'Oliver', 'Laurel', 'Sara', 'John', 'Harry', 'Marie', 'Stephanie', 'Gordon']
houses = {1:'Apartment', 2:'House', 3:'Mansion', 4:'Small Factory', 5:'Big Factory', 6:'Tower', 7:'City', 8:'County', 9:'State', 10:'Country', 11:'Continent', 12:'Earth', 13:'Solar System', 14:'Milky Way Galaxy', 15:'Universe'}
users = db['users']
for i in users:
  users[i]['timeout'] = False
db['users'] = users
def dbget(key):
  return json.loads(db.get_raw(key))
def getall(dict, prop):
  end = []
  for i in dict:
    end.append(dict[i][prop])
  return end
def grab(list, key, val):
  for j in range(len(list)):
    i = list[j]
    if i[key] == val:
      return [i, j]
@app.route('/')
def home():
  return {}

@app.route('/cr/<name>', methods=['POST'])
def cr(name):
  if name not in getall(db['users'], 'name'):
    idd = idgen.gen()
    while idd in db['ids']:
      idd = idgen.gen()
    baseworker = {'name':r.choice(workernames), 'level':1, 'xp':0}
    id2 = idgen.gen()
    while id2 in db['ids']:
      id2 = idgen.gen()
    baseworker['id'] = id2
    users[idd] = {'name':name, 'coins':0, 'workers':[baseworker], 'timeout':False, 'territory':(1, houses[1])}
    db['ids'].append(idd)
    db['ids'].append(id2)
    db['users'] = users
    return dict(users[idd], **{'id':idd})
  return {'error':'Name taken'}

@app.route('/my/account', methods=['GET'])
def myaccount():
  token = request.form['token']
  bfanc = dbget('users')[token].copy()
  users[token]['announcements'] = []
  return bfanc

@app.route('/work/<workerid>', methods=['POST'])
def work(workerid):
  token = request.form['token']
  workers = dbget('users')[token]['workers']
  worker = grab(workers, 'id', workerid)
  if users[token]['timeout']:
    return {'error':'On timeout'}
  else:
    def setToTimeout():
      users[token]['timeout'] = False
      db['users'] = users
    users[token]['timeout'] = True
    db['users'] = users
    thr = Timer(10.0, setToTimeout)
    thr.start()
  coinbonus = 0
  if worker[0]['level'] > 25:
    coinbonus = (len(workers)-1)*10
  users[token]['coins'] += worker[0]['level'] * 50 + coinbonus
  if users[token]['coins'] > users[token]['territory'][0] * 10000:
    users[token]['coins'] = users[token]['territory'][0] * 10000
    return {'error':'Not enough coin capacity'}
  xpbonus = 0
  if worker[0]['level'] > 25:
    foundgold = r.choice(list(map(int, '1000')))
    if foundgold:
      users[token]['gold'] += 1
      xpbonus = 30
  worker[0]['xp'] += 10 + xpbonus
  if worker[0]['xp'] >= 100:
    worker[0]['xp'] %= 100
    worker[0]['level'] += 1
  users[token]['workers'][worker[1]] = worker[0]
  db['users'] = users
  return dbget('users')[token]

@app.route('/purchase/<item>', methods=['POST'])
def purchase(item):
  token = request.form['token']
  if item == 'worker':
    if users[token]['coins'] >= 100:
      baseworker = {'name':r.choice(workernames), 'level':1, 'xp':0}
      id2 = idgen.gen()
      while id2 in db['ids']:
        id2 = idgen.gen()
      db['ids'].append(id2)
      baseworker['id'] = id2
      users[token]['workers'].append(baseworker)
      users[token]['coins'] -= 100
      db['users'] = users
      return dbget('users')[token]
    return {'error':'Insufficient coins'}
  if item == 'territory':
    if users[token]['coins'] >= users[token]['territory'][0] * 10000:
      try:
        users[token]['territory'] = (users[token]['territory'][0]+1, houses[users[token]['territory'][0]+1])
      except KeyError:
        return {'error':'Maximum territory reached'}, 304
      users[token]['coins'] -= users[token]['territory'][0] * 10000
      db['users'] = users
      return dbget('users')[token]
    return {'error':'Insufficient coins'}

@app.route('/charity', methods=['PUT'])
def charity():
  token = request.form['token']
  amount = request.form['amount']
  users[token]['coins'] -= int(amount)
  if users[token]['coins'] < 0:
    users[token]['coins'] = 0
  db['users'] = users
  return dbget('users')[token]

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
  cns = {}
  for i in users:
    cns[users[i]['name']] = users[i]['coins']
  cns = dict(sorted(cns.items(), key=lambda item: item[1], reverse=True))
  endstr = ''
  j = 1
  for i in cns:
    endstr += '' + str(j) + '. ' + i + ': ' + str(cns[i]) + '<br>\n'
    j += 1
  return 'Leaderboard(by coins):\n<br>' + endstr

@app.route('/trade/<other>/<type>', methods=['POST'])
def trade(other, type):
  trades = db['trades']
  token = request.form['token']
  if type == 'send':
    item = request.form['item']
    amount = str(request.form['amount'])
    id = idgen.gen()
    while id in db['ids']:
      id = idgen.gen()
    for i in users:
      if users[i]['name'] == other:
        recvr = dict({'id':i}, **users[i])
    trades[id] = {
      'from':token,
      'to':recvr['id'],
      'item':item,
      'amount':amount,
      'type':'offering'
    }
    users[recvr['id']]['announcements'].append(users[token]['name'] + ' has offered ' + amount + ' ' + item + '. Send a request to /trade/' + id + '/recieve, and send your body payload should have item=<the item you are giving>; amount=<the amount of the item you are giving>')
    db['trades'] = trades
    db['users'] = users
    return {'message':'Trade initiated successfully'}
  elif type == 'recieve':
    item = request.form['item']
    amount = str(request.form['amount'])
    for i in dict(trades):
      if i == other:
        trades[i]['new'] = {
          'item':item,
          'amount':amount
        }
        trades[i]['type'] = 'giving'
        users[trades[i]['from']]['announcements'].append(users[trades[i]['to']]['name'] + ' is giving back ' + item + ' ' + amount + '. Send a request to /trade/' + i + '/complete to finish the trade.')
    db['trades'] = trades
    return {'message':'Trade recieved successfully'}
  elif type == 'complete':
    sendr = trades[other]['from']
    recvr = trades[other]['to']
    item = trades[other]['item']
    amount = trades[other]['amount']
    nitem = trades[other]['new']['item']
    namount = trades[other]['new']['amount']
    users[recvr][item] += int(amount)
    users[recvr][nitem] -= int(namount)
    users[sendr][item] -= int(amount)
    users[sendr][nitem] += int(namount)
    del trades[other]
    return {'message':'Trade completed successfully'}
  elif type == 'reject':
    if trades[other]['type'] == 'offering':
      users[trades[other]['from']]['announcements'].append('Your trade was rejected.')
    elif trades[other]['type'] == 'giving':
      users[trades[other]['to']]['announcements'].append('Your trade was rejected.')
    del trades[other]
    return {'message':'Trade rejected successfully'}

for i in list(range(400, 419))+list(range(422, 430)):
  if i in [402, 407, 425, 426, 427]:
    continue
  @app.errorhandler(i)
  def handle_err(err):
    print(err)
    return "Oop! An error came up. It\'s your fault, so find some way to fix it."

for i in range(500, 506):
  @app.errorhandler(i)
  def handle_err_500(err):
    print(err)
    return 'Oop! An error came up. Sorry :(.'
app.run(host='0.0.0.0', port=8080)