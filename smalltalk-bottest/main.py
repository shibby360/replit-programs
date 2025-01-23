import time
import requests
import os
os.system('clear')
from flask import Flask, render_template, request
import urllib
app = Flask('DaBot', template_folder='ts')
import bottest
bot = bottest.Bot('DaBot', os.environ['pwd'], app, status="hi")
me = bot.get_user(8)
myguild = bot.get_guild(570)
@app.route('/')
def home():
  return 'dis is dabot'
@app.route('/waiter')
def waiter():
  time.sleep(10)
  return 'done'
@bot.command('purge')
def purgecommand():
  bot.get_guild(bot.comglos.guildId).purge()

@bot.command('bnc')
def bnccommand(bncc):
  myguild.send('i bounced: ' + bncc)
  print(bncc)

@bot.command('count')
def countcommand(num, end):
  print('count')
  for i in range(1, int(num)+1):
    myguild.send(str(i))
  myguild.send(end)

@app.route('/event/message')
def onmessage():
  form = urllib.parse.parse_qs(request.query_string)
  for i in form.copy():
    form[str(i)[2:-1]] = str(form[i][0])[2:-1]
    del form[i]
  print(form)
  #keep logiggn form
  return bottest.ACAO('')
app.run(host='0.0.0.0', port=8080)