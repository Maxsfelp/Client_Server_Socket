import socket

def readCommand(command):
	return command.split(':')

def sendCommand(data):
	UDPClient.sendall(data)

def recvData():
	return UDPClient.recv(1024)

HOST = '127.0.0.1'
PORT = 65432
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPClient.connect((HOST, PORT))
while True:
	inPut = input(">>> ")
	data = str(readCommand(inPut))
	sendCommand(data.encode())
	print(recvData())