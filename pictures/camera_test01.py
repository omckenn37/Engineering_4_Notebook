import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768) # sets resolution
	camera.start_preview() # prepares camera
	print("Running")
	time.sleep(2)
	camera.capture('camera_test.jpg') # takes picture
	print("Done")
