import json
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 7777))
server.listen()
print('Server Rodando...')

try:
    client, addr = server.accept()
    print(f'Servidor conetado a {addr}')
except:
    print('Servidor não conectado!')

while True:
    try:
        vetor = client.recv(1024)
        vetor = vetor.decode('utf-8')
        vetor = json.loads(vetor)

        imc = vetor[0] / vetor[1] ** vetor[1]

        res = json.dumps(imc)
        res = res.encode('utf-8')
        client.send(res)
    except:
        client.close()
        print('Conexão Finalizada')
        client, addr = server.accept()
        print(f'Servidor conetado a {addr}')

