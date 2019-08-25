# Python program to implement client side of chat room. 
import socket 
import select 
import sys 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 4: 
	print("Correct usage: script, Name, IP address, port number")
	exit() 
Name = str(sys.argv[1])
IP_address = str(sys.argv[2]) 
Port = int(sys.argv[3]) 
server.connect((IP_address, Port)) 

while True: 

	# maintains a list of possible input streams 
	sockets_list = [sys.stdin, server] 

	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print(str(message, "utf-8")) 
		else: 
			message = sys.stdin.readline() 
			server.send(bytes("<" + Name + ">: "+ message, "utf-8")) 
			print("<You>: " + message)
server.close() 