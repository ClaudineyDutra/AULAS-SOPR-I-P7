import socket
import threading
import pickle


def calculo_IMC(clientsocket, addr):
    print("Conectado a %s" % str(addr))
    dados = clientsocket.recv(1024)
    dados = pickle.loads(dados)

    imc = dados[1]/ (dados[0] * dados[0])

    imc = pickle.dumps(imc)
    clientsocket.send(imc)
    print("Resposta enviada!!")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()
print("Server rodando...")


while True:
    clientsocket, addr = server.accept()
    t = threading.Thread(target=calculo_IMC, args=(clientsocket, addr))
    t.start()