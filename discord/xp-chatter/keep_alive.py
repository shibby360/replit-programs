from flask import Flask, render_template, request
from threading import Thread
from replit import db

app = Flask('app')

@app.route('/', methods=['GET'])
def main():
  if request.method == 'GET':
    if 'dailies' in str(request.query_string):
      for i in db['user_stats']:
        print(db['user_stats'][i]['Daily Collected'])
        DB = db['user_stats']
        DB[i]['Daily Collected'] = False
        db['user_stats'] = DB
        print(i + 's daily reset')
        print(db['user_stats'][i]['Daily Collected'])
  return render_template('index.html')

def run():
  app.run(host="0.0.0.0", port=8080)
    
def keep_alive():
  server = Thread(target=run)
  server.start()