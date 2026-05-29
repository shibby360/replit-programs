from flask import Flask, render_template, request
from flask_socketio import emit, SocketIO, join_room, leave_room, rooms, send
import os
import random as r
def loggingoff():
  import logging
  log = logging.getLogger('werkzeug')
  log.setLevel(logging.ERROR)
loggingoff()
try:
  import ShdwDB
except ModuleNotFoundError:
  os.system('pip install ShdwDB')
  import ShdwDB
app = Flask('app')
suckit = SocketIO(app)
os.system('clear')
#Vars
chars = [
  {'name':'Shiv', 'punch':150, 'kick':200, 'specialty':'kick', 'hellblast':{'health':90, 'damage':90}},
  {'name':'Anish', 'punch':180, 'kick':150, 'specialty':'punch', 'hellblast':{'health':100, 'damage':120}},
  {'name':'Screwer', 'punch':270, 'kick':270, 'specialty':'punch', 'hellblast':{'health':300, 'damage':150}},
]
romno = 1
allrooms = {'Room 1':[]}
sidtoname = {}
#functions
def filrou(nm):
  exec(f"@app.route('/{nm}\')\ndef {nm}():\n  return render_template(\'{nm}.html\')\n")

#routes and events
@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/getchar/<sid>')
def getchar(sid):
  return sidtoname[sid]

filrou('start')
filrou('fail')
filrou('end')

#These two stay
@suckit.event
def Join(data):
  global romno, allrooms
  if len(allrooms[list(allrooms.keys())[-1]]) == 2:
    romno += 1
    allrooms['Room '+str(romno)] = [request.sid]
  else:
    allrooms['Room '+str(romno)] += [request.sid]
  join_room('Room '+str(romno))
  oppsid = 'No opponent yet'
  duplst = allrooms['Room '+str(romno)][:]
  duplst.remove(request.sid)
  if len(duplst) != 0:
    oppsid = duplst[0]
  emit('oppsid', oppsid, to=request.sid)
  emit('oppsid', request.sid, to=oppsid)
  if len(allrooms['Room '+str(romno)]) == 2:
    emit('whoturn', r.choice(allrooms['Room '+str(romno)]), to='Room '+str(romno))
  print(allrooms)
  
@suckit.event
def disconnect():
  global romno, allrooms
  roomtosend = None
  for i in rooms(request.sid):
    if 'Room ' in i:
      roomtosend = i
  if roomtosend != None:
    del allrooms[roomtosend]
    if roomtosend == 'Room 1':
      allrooms['Room 1'] = []
  else:
    pass
  emit('levv', 'someone left', to=roomtosend)

@suckit.event
def anatk(data):
  roomtosend = None
  for i in rooms(request.sid):
    if 'Room ' in i:
      roomtosend = i
  emit('atk', {'sid':request.sid, 'obj':sidtoname[request.sid]['char'], 'mode':data['mode']}, to=roomtosend)

@suckit.event
def hellblast(data):
  roomtosend = None
  for i in rooms(request.sid):
    if 'Room ' in i:
      roomtosend = i
  emit('helll', {'sid':request.sid, 'obj':sidtoname[request.sid]['char'], 'mode':data['mode']}, to=roomtosend)

@suckit.event
def speech(data):
  roomtosend = None
  for i in rooms(request.sid):
    if 'Room ' in i:
      roomtosend = i
  emit('atalk', {'sid':request.sid, 'dialog':data['dat'], 'obj':sidtoname[request.sid]},  to=roomtosend)

@suckit.event
def werein(data):
  char = ''
  for i in chars:
    if i['name'] == data['char']:
      char = i
  sidtoname[request.sid] = {'name':data['name'], 'char':char}
  emit('usersid', {'sid':request.sid})

suckit.run(app, host='0.0.0.0', port=8080)
