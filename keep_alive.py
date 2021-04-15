from flask import Flask
from threading import Thread
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')

@app.route('/')
def home():
    return "<h1>-Dragonflyy is online!</h1><p1><a href='https://stats.uptimerobot.com/AWR8LS9Owx'>UptimeRobot Server Status</a>"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()