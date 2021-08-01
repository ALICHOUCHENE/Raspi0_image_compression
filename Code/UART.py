import serial

def ports_availables() :
    
    p = serial.tools.list_ports.comports()
    for port, desc, hwid in sorted(p):
        if  desc == "Arduino Uno ("+str(port)+")" :
            ports.append(port)
        
    return(ports)



def connect(ports):
    global port
    baudrate=9600
    bytesize=8
    for port in ports :
        try:
            port = serial.Serial(port,baudrate,bytesize)
            print('connected sucsessefully')
        except:
            print('faile')



