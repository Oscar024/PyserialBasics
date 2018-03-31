import serial


ser = serial.Serial('/dev/pts/19',baudrate=9600,timeout=None)  # open serial port
print(ser.name)         # check which port was really used
#ser.write(b'hellofrompycharm')     # write a string
#x = ser.read()          # read one byte
sx = ser.read(4)
#sx= ser.read_until('\r')
ser.close()             # close port





