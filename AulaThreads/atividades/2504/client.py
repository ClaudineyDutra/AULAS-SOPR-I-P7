import socket
import pickle


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('localhost', 9999))

dados = []

altura = float(input("Altura> "))
peso = float(input("Peso> "))

dados.append(altura)
dados.append(peso)

dados = pickle.dumps(dados)
cliente.send(dados)

imc = cliente.recv(1024)
imc = pickle.loads(imc)
print(f'Seu IMC é: {round(imc, 2)}')
