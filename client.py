import socket

def readCommand(command):
	return command.split(':')

def sendCommand(data):
	UDPClient.sendall(data)

def recvData():
	data = UDPClient.recv(1024).decode()
	data = eval(data)
	for i in range(0, (len(data[0]))):
		print("Nome: "+data[0][i]+" Sexo: "+data[1][i]+" Idade: "+data[2][i])

HOST = '127.0.0.1'
PORT = 65432
UDPClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPClient.connect((HOST, PORT))
while True:
	inPut = input(">>> ")
	split = readCommand(inPut)
	data = str(split).encode()
	if split[0] == 'SELECT*':
		sendCommand(data)
		recvData()
	elif split[0] == 'INSERT':
		sendCommand(data)
	elif split[0] == 'EXIT':
		sendCommand(data)
		break
	else:
		print("Comando errado")
UDPClient.close()
	