import RPi.GPIO as GPIO

# Setze den GPIO-Modus auf BCM
GPIO.setmode(GPIO.BCM)

# Definiere den PWM-Pin (BCM-Pin 18)
pwm_pin = 18

# Konfiguriere den Pin als PWM-Ausgang
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 1000)  # 1000 Hz Frequenz

try:
    while True:
        # Benutzereingabe für die gewünschte Geschwindigkeit (0-100%)
        speed = float(input("Geben Sie die Geschwindigkeit (0-100%) ein: "))
        
        if 0 <= speed <= 100:
            # Berechnung der Pulsweiten basierend auf der Geschwindigkeit
            duty_cycle = speed
            # Starte das PWM-Signal mit der berechneten Pulsweite
            pwm.start(duty_cycle)
            print(f"Geschwindigkeit: {speed}%")
        else:
            print("Ungültige Eingabe. Bitte geben Sie einen Wert zwischen 0 und 100 ein.")

except KeyboardInterrupt:
    # Programm sauber beenden
    pwm.stop()
    GPIO.cleanup()
