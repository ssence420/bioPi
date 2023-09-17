import RPi.GPIO as GPIO
import time

# Setze den GPIO-Modus auf BCM
GPIO.setmode(GPIO.BCM)

# Definiere den PWM-Pin (BCM-Pin 18)
pwm_pin = 12

# Konfiguriere den Pin als PWM-Ausgang
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 1000)  # 1000 Hz Frequenz

try:
    while True:
        # Lüftergeschwindigkeiten in Prozent und Pulsweiten in Sekunden
        speeds = [25, 50, 75]  # Geschwindigkeiten in Prozent
        for speed in speeds:
            # Berechnung der Pulsweiten basierend auf der Geschwindigkeit
            T_on = (speed / 100) * 0.01  # Pulsweite in Sekunden (1% = 0,01s)
            T_off = 0.01 - T_on  # Restliche Zeit

            # Starte das PWM-Signal mit der berechneten Pulsweite
            pwm.start(speed)
            print(f"Speed: {speed}%")
            time.sleep(5)  # Läuft für 5 Sekunden

            # Stoppe das PWM-Signal
            pwm.stop()

except KeyboardInterrupt:
    # Programm sauber beenden
    GPIO.cleanup()
