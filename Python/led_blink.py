import RPi.GPIO as GPIO
import time
#GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

while True:
	GPIO.output(3, 1)
	time.sleep(1)
	GPIO.output(3, 0)
	time.sleep(1)
