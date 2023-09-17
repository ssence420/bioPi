import RPi.GPIO as GPIO
import time

# Import library and create instance of REST client.
from Adafruit_IO import Client, Feed



aio = Client('flofi96', 'aio_zKLN00waUPiFUTKKQGHLsSlVy49L')

feed = Feed(name='FanSpeed')

result = aio.create_feed(feed)

# Send the value 100 to a feed called 'Foo'.
#aio.send('LüfterSpeed', 100)

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.

data = aio.feeds('FanSpeed')
print('Received value: {0}'.format(data.value))


# Setze den GPIO-Modus auf BCM
GPIO.setmode(GPIO.BCM)

# Definiere den PWM-Pin (BCM-Pin 18)
pwm_pin = 12

# Konfiguriere den Pin als PWM-Ausgang
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 1000)  # 1000 Hz Frequenz

try:
    while True:
        # Benutzereingabe für die gewünschte Geschwindigkeit (0-100%)
        # speed = float(input("Geben Sie die Geschwindigkeit (0-100%) ein: "))
        speed = aio.receive('FanSpeed')
        print('Received value: {0}'.format(data.value))


        if 0 <= speed <= 100:
            # Berechnung der Pulsweiten basierend auf der Geschwindigkeit
            duty_cycle = speed
            # Starte das PWM-Signal mit der berechneten Pulsweite
            pwm.start(duty_cycle)
            print(f"Geschwindigkeit: {speed}%")
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen Wert zwischen 0 und 100 ein.")
        time.sleep(10)


except KeyboardInterrupt:
    # Programm sauber beenden
    pwm.stop()
    GPIO.cleanup()
