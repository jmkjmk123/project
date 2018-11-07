import socket

server_socket = socket.socket()
server_socket.bind(('localhost',12345))
server_socket.listen(0)
client_socket, addr = server_socket.accept()
while True:
	data = client_socket.recv(65535)
	print(data)
client_socket.close()
server_socket.close()
