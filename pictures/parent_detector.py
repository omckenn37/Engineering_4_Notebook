from gpiozero import MotionSensor
from picamera import PiCamera
import datetime

pir = MotionSensor(4) # creates motion sensor on gpio 4
camera = PiCamera()
now = datetime.datetime.now() # gets current date and time
filename = "intruder_" + str(now).replace(" ", "_") + ".mp4" # creates filename that changes based on date and time

while True:
	pir.wait_for_motion() # waits for motion sensor to be triggered
	print("Motion detected")
	camera.start_recording(filename) # starts new recording with filename
	pir.wait_for_no_motion() # waits for motion to stop
	camera.stop_preview() # stops recording

