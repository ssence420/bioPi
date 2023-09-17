import Adafruit_BME280
import RPi.GPIO as GPIO
import time

# GPIO-Pin für den Lüfter (PWM)
FAN_PIN = 18

# BME280-Sensor Initialisierung
bme280 = Adafruit_BME280.Adafruit_BME280()

# Schwellenwerte für die Lüftersteuerung (anpassbar)
TEMP_THRESHOLD_HIGH = 28.0
TEMP_THRESHOLD_LOW = 25.0

# Initialisiere PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)
fan_pwm = GPIO.PWM(FAN_PIN, 1000)  # 1000 Hz PWM

def read_temperature():
    temperature = bme280.read_temperature()
    return temperature

try:
    fan_pwm.start(0)  # Starte den Lüfter mit 0% PWM

    while True:
        temperature = read_temperature()
        print(f"Aktuelle Temperatur: {temperature}°C")

        if temperature > TEMP_THRESHOLD_HIGH:
            fan_pwm.ChangeDutyCycle(100)  # 100% PWM (voller Lüfter)
        elif temperature < TEMP_THRESHOLD_LOW:
            fan_pwm.ChangeDutyCycle(0)    # 0% PWM (Lüfter aus)
        else:
            # PWM-Wert entsprechend der Temperatur anpassen
            fan_pwm.ChangeDutyCycle((temperature - TEMP_THRESHOLD_LOW) * 10)

        time.sleep(60)  # Messung alle 60 Sekunden

except KeyboardInterrupt:
    fan_pwm.stop()
    GPIO.cleanup()
