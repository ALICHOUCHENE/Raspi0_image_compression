from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.resolution = (1024, 768)

def take_image(name):
	camera.start_preview()
	# Camera warm-up time
	sleep(1)
	camera.capture(str(name)+'.jpg')
	camera.stop_preview()
	
