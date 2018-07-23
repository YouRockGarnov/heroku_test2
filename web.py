from flask import Flask

app = Flask(__name__)

confirmation_token = '6d75c23e'

@app.route('/', methods=['POST'])
def processing():
      return confirmation_token

@app.route('/')
def index():
  return 'hello'
