import socket

nome = []
sexo = []
idade = []
dados = []

def sendData(conn, dados):
    if len(dados) != 0:
        dados = str(dados)
        conn.sendall(dados.encode())

def saveData(data):
    nome.append(data[1])
    sexo.append(data[2])
    idade.append(data[3])
    dados = [nome, sexo, idade]
    return dados

def recvData(conn, dados):
    data = conn.recv(1024)
    if data:
        data.decode('utf-8')
        data = eval(data)
        if data[0] == 'SELECT*':
            sendData(conn, dados)
        elif data[0] == 'INSERT':
            dados = saveData(data)
    return dados

HOST = '127.0.0.1'
PORT = 65432
UDPServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
UDPServer.bind((HOST, PORT))
UDPServer.listen()
conn, addr = UDPServer.accept()
while 1:
    dados = recvData(conn, dados)
conn.close()
UDPServer.close()