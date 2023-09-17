from flask import Flask, render_template, Response

import time
import DATA


app = Flask(__name__)





@app.route('/')
def index():
    # Lesen Sie den Inhalt der log.txt Datei
    # with open('log.txt', 'r') as file:
    #     log_inhalt = file.read()
     
    data = DATA.GetMeasures()
    cTemp = data[0]
    humidity = data[1]

    yield f"data: Temperature: {cTemp}, Humidity: {humidity}\n\n"
    time.sleep(10)


    # Rendern Sie eine einfache HTML-Seite mit dem Inhalt
    return f'<html><body><pre>{log_inhalt}</pre></body></html>'





