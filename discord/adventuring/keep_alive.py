from flask import Flask, render_template, request
from threading import Thread
from replit import db

app = Flask('app')

@app.route('/', methods=['GET'])
def main():
  return ':)'

def run():
  app.run(host="0.0.0.0", port=8080)
    
def keep_alive():
  server = Thread(target=run)
  server.start()