from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Lesen Sie den Inhalt der log.txt Datei
    with open('log.txt', 'r') as file:
        log_inhalt = file.read()

    # Rendern Sie eine einfache HTML-Seite mit dem Inhalt
    return f'<html><body><pre>{log_inhalt}</pre></body></html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)