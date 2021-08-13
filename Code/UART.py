import serial
import os

def ports_availables() :
    
    ports = serial.tools.list_ports.comports()
    return(ports)



def connect(com):

	baudrate=9600
	bytesize=8
	try:
		port = serial.Serial(com,baudrate,bytesize,timeout=1)
	except:
		print('faile')

	return port 

def read(port):
	if (port.in_waiting) > 0 :
		line = (port.readline().decode('utf-8')).rstrip()
	return(line)


def send_image_1(port,image):
	os.system('base64 < image > pic.txt')
	CHUNK_SIZE = 55
	image_file ='pic.txt'
	with open(image_file, 'rb') as infile:	
		while True:
			chunk = infile.read(CHUNK_SIZE)
			if not chunk: break		
			port.write(chunk)
			port.write('\r')
		port.close()
		

 
def send_data_2(port,image):

	port.write(open(image).read)
	port.close()



