# from asyncio.timeouts import timeout
# from curses import baudrate
import os
import serial
import serial.tools.list_ports_windows

def get_ports():

    ports = serial.tools.list_ports_windows.comports()

    return ports

def find_arduino(portsFound):
    commPort = 'None'
    numConnection = len(portsFound)

    for i in range(0,numConnection):
        port = foundPorts[i]
        strPort = str(port)

        if 'CH340' in strPort:
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
    
    return commPort

foundPorts = get_ports()
print(foundPorts)

connectPort = find_arduino(foundPorts)

if connectPort != 'None':
    ser = serial.Serial(connectPort, baudrate = 9600 , timeout = 15)
    print("Connected to:",connectPort)
    while True:
        data = ser.readline(1000)
        with open("file.txt", "a", newline='\n') as thefile:
            # thefile.write(data.encode("utf-8").replace("\n", os.linesep))
            thefile.write(str(data))
        # str(data, 'UTF8')
        # data.decode('UTF-8')
            print(data) 
    
else:
    print("Connection issue")

print("Done")


import serial.tools.list_ports

def get_ports():
    return serial.tools.list_ports.comports()

foundPorts = get_ports()

for port in foundPorts:
    print(f"Name: {port.name} - Description: {port.description} - Device: {port.device}")