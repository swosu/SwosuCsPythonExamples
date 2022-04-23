##################################
# MLX90640 Test with Raspberry Pi
##################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640

# set up GPIO Pins
import RPi.GPIO as GPIO
import time

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ # set refresh rate

# Add GPIO Stuff
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)

frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
while True:
    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var
        if 100 < frame.max():
                print('f', end = '')
                GPIO.output(16, 1)
                time.sleep(5)
                #GPIO.output(16, False)
                time.sleep(1)
        break
    except ValueError:
        continue # if error, just read again

# print out the average temperature from the MLX90640
print('Average MLX90640 Temperature: {0:2.1f}C ({1:2.1f}F)'.\
      format(np.mean(frame),(((9.0/5.0)*np.mean(frame))+32.0)))

if 100 < np.mean(frame):
	print('\n\nWE HAVE FIRE!!!!')

if 100 < frame.max():
	print('\n\n\nWE HAVE A BABY FIRE <3')
	print('f', end = '')
	GPIO.output(16, 1)
	time.sleep(5)
	#GPIO.output(16, False)
	time.sleep(1)
