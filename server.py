import socket
import pickle

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as UDPServer:
    UDPServer.bind((HOST, PORT))
    UDPServer.listen()
    conn, addr = UDPServer.accept()
    
    with conn:
        print('Connected by', addr)
        
        while True:
            data = conn.recv(4096)
            if not data:
                break;
            data.decode('utf-8')
            data = eval(data)
            print(data)

# nome = ["Felipe", "Pedro"]
# sexo = ["masc", "masc"]
# idade = [21, 21]

# dados = [nome, sexo, idade]

# print(dados)
