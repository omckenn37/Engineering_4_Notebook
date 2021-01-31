import time
import picamera
frame = 1

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768) # sets resolution
	while True:
		i = str(input("Entee to take a frame, x to exit: ")) # gets user input
		try:
			if i == "":
				camera.capture('/home/pi/Documents/Engineering_4_Notebook/pictures/animation/frame%03d.jpg' % frame) # captures frame
				frame += 1
			else:
				camera.stop_preview()
				break
		except KeyboardInterrupt: # checks for keyboard interrupt
			camera.stop_preview()
			break
