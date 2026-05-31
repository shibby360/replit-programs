import requests
import time
import keep_alive
import os
os.system('clear')
os.environ['TZ'] = 'US/Pacific'
time.tzset()

keep_alive.keep_alive()
while True:
  if '00:00:00' in time.ctime(time.time()):
    requests.get('https://moi-bot.shivankchhaya.repl.co', params={'dailies':''}, allow_redirects=True)
    print('Request sent!')
  if ':30 ' in time.ctime(time.time()):
    pass