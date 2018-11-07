import socket
import time

s = socket.socket()
s.connect(('Server's IP' , 12345))
while True:
	s.send('hello')
	time.sleep(2)
s.close() 
