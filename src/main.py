import time
import datetime
import DATA
from flask import Flask, render_template

log_datei = 'log.txt'



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

# Funktion zum Schreiben der Messwerte in das Log
def schreibe_log(datei, messwert):
    with open(datei, 'r+') as file:
        # Lies den aktuellen Inhalt der Datei
        inhalt = file.read()
        
        # Erstelle einen Zeitstempel für das aktuelle Datum und die Uhrzeit
        jetzt = datetime.datetime.now()
        zeitstempel = jetzt.strftime('%Y-%m-%d %H:%M:%S')

        # Kombiniere den neuen Messwert mit dem Zeitstempel
        neuer_messwert = f"[{zeitstempel}] Temperatur: {messwert[0]}, Humidity: {messwert[1]}\n"

        # Setze den Dateizeiger an den Anfang der Datei
        file.seek(0, 0)

        # Schreibe den neuen Messwert in die erste Zeile
        file.write(neuer_messwert)

        # Füge den vorherigen Inhalt unterhalb des neuen Messwerts ein
        file.write(inhalt)


#GetDaten aus DATA.py

while True:
    data = DATA.GetMeasures()
    print("GetMeasures erfolgreich")

    schreibe_log(log_datei, data)
    print("Messwert protokolliert.")
    cTemp = data[0]
    humidity = data[1]

    print ("MAIN Temperature in Celsius : %.2f C" %cTemp)
    print ("MAIN Relative Humidity : %.2f %%" %humidity)
    time.sleep(10) 