import RPi.GPIO as GPIO
import ipfshttpclient
import time

# GPIO setup
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# IPFS setup
client = ipfshttpclient.connect()

def control_led(message):
    if message == "ON":
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED is ON")
    elif message == "OFF":
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED is OFF")
    else:
        print("Unknown command")

try:
    print("Listening for pub-sub messages on topic 'led-control'...")
    for message in client.pubsub.subscribe('led-control'):
        control_led(message['data'].decode('utf-8'))
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()