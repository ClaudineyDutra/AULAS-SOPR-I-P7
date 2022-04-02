import json
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()
print('Server Rodando...')
print('Aguardando conexão...')

try:
    client, addr = server.accept()
    print(f'Servidor conectado a {addr}')
except:
    print('Servidor não conectado!')

def receber():
    vetor = client.recv(1024)
    vetor = vetor.decode('utf-8')
    vetor = json.loads(vetor)
    return vetor

def enviar(var):
    var = json.dumps(var).encode('utf-8')
    client.send(var)

while True:
    try:
        menu = receber()
        print('Vetor recebeu: ', menu)
        # TEMPERATURA
        if menu[0] == 1:
            if menu[1] == 1:
                # Celsius para Fahrenheit
                valorFar = 1.8 * menu[2] + 32
                enviar(valorFar)
            elif menu[1] == 2:
                # Celsius para Kelvin
                valorKel = menu[2] + 273
                enviar(valorKel)
            elif menu[1] == 3:
                # Fahrenheit para Celcius
                valorC = (menu[2]-32)/1.8
                enviar(valorC)
            elif menu[1] == 4:
                # Fahrenheit para Kelvin
                valorKel = (menu[2]-32) * 5/9 + 273
                enviar(valorKel)
            elif menu[1] == 5:
                # Kelvin para Celcius
                valorC = menu[2] - 273
                enviar(valorC)
            elif menu[1] == 6:
                # Kelvin para Fahrenheit
                valorFar = (menu[2]-273) * 1.8 + 32
                enviar(valorFar)
        # COMPRIMENTO
        elif menu[0] == 2:
            if menu[1] == 1:
                # Metros para Kilometros
                valorKM = menu[2]/1000
                enviar(valorKM)
            elif menu[1] == 2:
                # Metros para Centímetros
                valorCM = menu[2] * 100
                enviar(valorCM)
            elif menu[1] == 3:
                # Kilometros para Metros
                valorM = menu[2] * 1000
                enviar(valorM)
            elif menu[1] == 4:
                # Kilometros para Centímetros
                valorCM = menu[2] * 100000
                enviar(valorCM)
            elif menu[1] == 5:
                # Centímetros para Metros
                valorM = menu[2] / 100
                enviar(valorM)
            elif menu[1] == 6:
                # Centímetros para Kilometros
                valorM = menu[2] / 100000
                enviar(valorM)
        # ÁREA
        elif menu[0] == 3:
            if menu[1] == 1:
                # Metros Quadrados para Kilometros Quadrados
                valorKM = menu[2]/1000000
                enviar(valorKM)
            elif menu[1] == 2:
                # Metros Quadrados para Centímetros Quadrados
                valorCM = menu[2] * 10000
                enviar(valorCM)
            elif menu[1] == 3:
                # Kilometros Quadrados para Metros Quadrados
                valorM = menu[2] * 1000000
                enviar(valorM)
            elif menu[1] == 4:
                # Kilometros Quadrados para Centímetros Quadrados
                valorcm = menu[2] * 10000000000
                enviar(valorcm)
            elif menu[1] == 5:
                # Centímetros Quadrados para Metros Quadrados
                valorm = menu[2] / 10000
                enviar(valorm)
            elif menu[1] == 6:
                # Centímetros Quadrados para Kilometros Quadrados
                valorkm = menu[2] / 10000000000
                enviar(valorkm)
        # GRAMA
        elif menu[0] == 4:
            if menu[1] == 1:
                # Grama para Quilograma
                valorQM = menu[2] / 1000
                enviar(valorQM)
            elif menu[1] == 2:
                # Grama para Miligrama
                valorMG = menu[2] * 100
                enviar(valorMG)
            elif menu[1] == 3:
                # Quilograma para Grama
                valorG = menu[2] * 1000
                enviar(valorG)
            elif menu[1] == 4:
                # Quilograma para Miligrama
                valormg = menu[2] * 1000000
                enviar(valormg)
            elif menu[1] == 5:
                # Miligrama para Grama
                valorg = menu[2] / 1000
                enviar(valorg)
            elif menu[1] == 6:
                # Miligrama para Quilograma
                valorqm = menu[2] / 1000000
                enviar(valorqm)
        # SAIR
        elif menu[0] == 5:
            raise Exception
    except:
        print('Conexão encerrada!')
        client.close()
        print('Aguardando conexão...')
        client, addr = server.accept()
        print(f'Servidor conectado a {addr}')