import RPi.GPIO as GPIO
import time

import board,busio
import numpy as np
import adafruit_mlx90640

##################################
# MLX90640 Test with Raspberry Pi
##################################

# Set up GPIO general behavior
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up individual GPIO pins
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
# run the loop as long as you can
while True:
	try:
		print( "Prep for Read, slow blink")
		GPIO.output(16,GPIO.HIGH)
		#time.sleep(0.2)
		GPIO.output(16,GPIO.LOW)
		#time.sleep(0.2)
		mlx.getFrame(frame) # read MLX temperatures into frame var
		if 100 < frame.max():
			print('FIRE')
			GPIO.output(12,GPIO.HIGH)
			for ticker in range (0,60):
				print( "Valve on, fast blink")
				GPIO.output(16,GPIO.HIGH)
				#time.sleep(0.05)
				GPIO.output(16,GPIO.LOW)
				#time.sleep(0.05)
		else:
			GPIO.output(12,GPIO.LOW)
			GPIO.output(16,GPIO.LOW)
			print('no fire')
	except ValueError:
		continue # if error, just read again
