import UART
import camera
import compress

arduino=UART.connect()
pyboard=UART.connect()
arduino_data=[]
while True :
	if arduino.available():
		data=UART.raed(arduino)
		arduino_data.append(data)
		camera.take_image('image_1')
		compress.compress_image()
		UART.send_image_1(pyboard,"compressed_image_1")
		time.sleep(2)
		camera.take_image('image_2')
		compress.compress_image()
		UART.send_image_1(pyboard,"compressed_image_2")
		time.sleep(2)
