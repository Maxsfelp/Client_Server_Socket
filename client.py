import socket

HOST = '127.0.0.1'
PORT = 65432

def readCommand(command):
	return command.split(':')

def sendCommand(data):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as UDPClient:
		UDPClient.connect((HOST, PORT))
		UDPClient.sendall(data)
		return UDPClient.recv(4096)

if __name__ == '__main__':
	inPut = input(">>> ")
	data = str(readCommand(inPut))
	print(sendCommand(data.encode()))