import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)


while True:
	print( "LEDs on")
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(1)
	print( "LED off")
	GPIO.output(16,GPIO.LOW)
	GPIO.output(12,GPIO.LOW)
	time.sleep(1)
