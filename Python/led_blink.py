import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # sets weird warnings to false
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT) # sets board pin 40 to output

for i in range(0, 10): # blinks the LED's 10 times
	GPIO.output(pin, 1)
	time.sleep(0.5)
	GPIO.output(pin, 0)
	time.sleep(0.5)

