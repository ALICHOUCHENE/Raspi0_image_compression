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
   		 print('connected sucsessefully')
    except:
         print('faile')

    return port 



def read(port):
	if port.in_waiting > 0:
            line = port.readline().decode('utf-8').rstrip()
    return(line)


def send_image_1(port,image):            	    # image.jpg
	
	os.system('base64 < image > pic.txt')	    #Linux builtin to convert binary files to base64 txt
	CHUNK_SIZE = 55 					        # Maximum chunk size that can be sent
    image_file = 'pic.txt'					    # Image converted to b64 txt file
    with open(image_file, 'rb') as infile:			
    	while True:
		
			chunk = infile.read(CHUNK_SIZE)		
			if not chunk: break		
			port.write(chunk) 			    	# write data to Arduin0		
			port.write('\r')					# Write carriage return to tell arduino to send message
    port.close()
		

 
def send_data_2(port,image):

	port.write(open(image).read)
	port.close()



