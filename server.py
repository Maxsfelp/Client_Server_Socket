import socket

nome = []
sexo = []
idade = []
dados = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as UDPServer:
    UDPServer.bind((HOST, PORT))
    UDPServer.listen()
    conn, addr = UDPServer.accept()
    
    with conn:
        
        while True:
            data = conn.recv(4096)
            if not data:
                break;
            data.decode('utf-8')
            data = eval(data)
            if data[0] == 'SELECT*':
                if len(dados) != 0:
                    conn.sendall(dados.encode())
            else:
                nome.append(data[1])
                sexo.append(data[2])
                idade.append(data[3])
                dados = [nome, sexo, idade]
                dados = str(dados)
                conn.sendall(dados.encode())