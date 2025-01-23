import os, time, requests
from flask import Response, request
import urllib
import inspect
os.environ['TZ'] = 'US/Pacific'
time.tzset()
page = 'https://small-talk.shivankchhaya.repl.co'
def dicttoclass(dict, addclass=None):
  class tret:
    pass
  if addclass != None:
    tret = addclass
  for i in dict:
    setattr(tret, i, dict[i])
  return tret
class Bot:
  def __init__(self, name, password, app, site=None, status=None, prefix=None):
    self.name = name + '[Bot]'
    self.app = app
    r = requests.get(f'{page}/loggedin?user={self.name}&pwd={password}')
    if r.text == 'Not found user.':
      syms = ['/', '-', '\\']
      for j in range(0, 5):
        for i in syms:
          os.system('clear')
          print('Creating bot...' + i)
          time.sleep(0.5)
      self.name = name
      r = requests.get(f'{page}/makeprof?name={self.name}&pwd={password}&status={status}&bot=[Bot]&botsite={site}&botfix={prefix}&dataurl=&ip=')
      self.name = name + '[Bot]'
      self.userdict = r.json()
    else:
      if status != None:
        requests.get(f'{page}/editprof/status/{status}/{self.name}')
    self.userdict = r.json()
    class comglos:
      pass
    self.comglos = comglos
    self.comglos.guildId = None
    self.comglos.initiator = None
  def command(self, name):
    def i(f):
      def name__():
        global guildId
        form = urllib.parse.parse_qs(request.query_string)
        for i in form.copy():
          form[str(i)[2:-1]] = str(form[i][0])[2:-1]
          del form[i]
        self.comglos.guildId = form['guildId']
        self.comglos.initiator = form['initiator']
        del form['guildId']
        del form['initiator']
        inspection = inspect.getfullargspec(f)
        argstoput = {}
        for l in range(len(inspection[0])):
          k = inspection[0][l]
          argstoput[k] = list(form.values())[l]
        returnval = f(**argstoput)
        returnval = returnval if returnval != None else ''
        return ACAO(returnval)
      name__.__name__ = name
      self.app.route('/command/'+name)(name__)
    return i
  def get_guild(self, id):
    r = requests.get(f'{page}/getAGuild/{id}').json()
    return Guild(self, r)
  def get_user(self, id):
    r = requests.get(f'{page}/users').json()
    for i in r:
      del r[i]['password']
    for i in r:
      if r[i]['id'] == id:
        return dicttoclass(dict({'name':i}, **r[i]))
class Messageable:
  def __init__(self):
    pass
  def update(self):
    requests.get(f'{page}/botmessage/{self.id}')
  def in_messageable(self):
    r = requests.get(f'{page}/getAGuild/{self.id}').json()
    return self.user.userdict in r['bots']
  def send(self, message):
    if not self.in_messageable():
      return
    r = requests.get(f'{page}/sendmessage?user={self.user.name}&message={message}&time={time.time()}&guildid={self.id}').text
    self.update()
    return r
  def delmsg(self, id):
    if not self.in_messageable():
      return
    requests.get(f'{page}/delmsg?id={id}&guildid={self.id}')
    self.update()
    return self
  def purge(self):
    if not self.in_messageable():
      return
    requests.get(f'{page}/delmsg?id=0&guildid={self.id}&purge=yes')
    self.update()
    return self
class Guild(Messageable):
  def __init__(self, user, json):
    super().__init__()
    self.user = user
    dicttoclass(json, self)
def ACAO(response):
  rr = Response(response)
  rr.headers['Access-Control-Allow-Origin'] = page
  return rr