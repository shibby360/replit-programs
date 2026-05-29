from flask import Flask, render_template, request
from wrpy import WordReference
wr = WordReference('en', 'fr')

app = Flask('app')

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
  try:
    translation = wr.translate(request.form['word'])
  except NameError:
    return 'no translation'
  return translation

app.run(host='0.0.0.0', port=8080)
