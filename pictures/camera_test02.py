import time
import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)

	for i in range(5):
		time.sleep(2)
		
		if i == 0:
			camera.image_effect = 'colorswap'
			camera.capture('camera_test_colorswap.jpg')
		elif i == 1:
			camera.image_effect = 'sketch'
			camera.capture('camera_test_colorswap.jpg')
		elif i == 2:
			camera.image_effect = 'cartoon'
			camera.capture('camera_test_colorswap.jpg')
		elif i == 3:
			camera.image_effect = 'washedout'
			camera.capture('camera_test_colorswap.jpg')
		else:
			camera.image_effect = 'none'
			camera.capture('camera_test_colorswap.jpg')
		
		time.sleep(2)
		print("Took picture # " + str(i))

camera.stop_preview()
print("Done")

