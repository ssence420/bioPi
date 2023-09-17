import time
import datetime
import DATA

log_datei = 'log.txt'

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
    time.sleep(120) 