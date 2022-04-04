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

def enviar(var, resultado):
    # PARA TEMPERATURA
    if menu[0] == 1:
        if menu[1] == 1:
            # Celsius para Fahrenheit
            resultado.append(menu[2])
            resultado.append('ºC')
            resultado.append(var)
            resultado.append('ºF')
        elif menu[1] == 2:
            # Celsius para Kelvin
            resultado.append(menu[2])
            resultado.append('ºC')
            resultado.append(var)
            resultado.append('K')
        elif menu[1] == 3:
            # Fahrenheit para Celcius
            resultado.append(menu[2])
            resultado.append('ºF')
            resultado.append(var)
            resultado.append('ºC')
        elif menu[1] == 4:
            # Fahrenheit para Kelvin
            resultado.append(menu[2])
            resultado.append('ºF')
            resultado.append(var)
            resultado.append('K')
        elif menu[1] == 5:
            # Kelvin para Celcius
            resultado.append(menu[2])
            resultado.append('K')
            resultado.append(var)
            resultado.append('ºC')
        elif menu[1] == 6:
            # Kelvin para Fahrenheit
            resultado.append(menu[2])
            resultado.append('K')
            resultado.append(var)
            resultado.append('ºF')
    # PARA COMPRIMENTO
    elif menu[0] == 2:
        if menu[1] == 1:
            # Metros para Kilometros
            resultado.append(menu[2])
            resultado.append('m')
            resultado.append(var)
            resultado.append('Km')
        elif menu[1] == 2:
            # Metros para Centímetros
            resultado.append(menu[2])
            resultado.append('m')
            resultado.append(var)
            resultado.append('cm')
        elif menu[1] == 3:
            # Kilometros para Metros
            resultado.append(menu[2])
            resultado.append('Km')
            resultado.append(var)
            resultado.append('m')
        elif menu[1] == 4:
            # Kilometros para Centímetros
            resultado.append(menu[2])
            resultado.append('Km')
            resultado.append(var)
            resultado.append('cm')
        elif menu[1] == 5:
            # Centímetros para Metros
            resultado.append(menu[2])
            resultado.append('cm')
            resultado.append(var)
            resultado.append('m')
        elif menu[1] == 6:
            # Centímetros para Kilometros
            resultado.append(menu[2])
            resultado.append('cm')
            resultado.append(var)
            resultado.append('Km')
    # PARA ÁREA
    elif menu[0] == 3:
        if menu[1] == 1:
            # Metros Quadrados para Kilometros Quadrados
            resultado.append(menu[2])
            resultado.append('m²')
            resultado.append(var)
            resultado.append('Km²')
        elif menu[1] == 2:
            # Metros Quadrados para Centímetros Quadrados
            resultado.append(menu[2])
            resultado.append('m²')
            resultado.append(var)
            resultado.append('cm²')
        elif menu[1] == 3:
            # Kilometros Quadrados para Metros Quadrados
            resultado.append(menu[2])
            resultado.append('Km²')
            resultado.append(var)
            resultado.append('m²')
        elif menu[1] == 4:
            # Kilometros Quadrados para Centímetros Quadrados
            resultado.append(menu[2])
            resultado.append('Km²')
            resultado.append(var)
            resultado.append('cm²')
        elif menu[1] == 5:
            # Centímetros Quadrados para Metros Quadrados
            resultado.append(menu[2])
            resultado.append('cm²')
            resultado.append(var)
            resultado.append('m²')
        elif menu[1] == 6:
            # Centímetros Quadrados para Kilometros Quadrados
            resultado.append(menu[2])
            resultado.append('cm²')
            resultado.append(var)
            resultado.append('Km²')
    # PARA MASSA
    elif menu[0] == 4:
        if menu[1] == 1:
            # Grama para Quilograma
            resultado.append(menu[2])
            resultado.append('g')
            resultado.append(var)
            resultado.append('Kg')
        elif menu[1] == 2:
            # Grama para Miligrama
            resultado.append(menu[2])
            resultado.append('g')
            resultado.append(var)
            resultado.append('mg')
        elif menu[1] == 3:
            # Quilograma para Grama
            resultado.append(menu[2])
            resultado.append('Kg')
            resultado.append(var)
            resultado.append('g')
        elif menu[1] == 4:
            # Quilograma para Miligrama
            resultado.append(menu[2])
            resultado.append('Kg')
            resultado.append(var)
            resultado.append('mg')
        elif menu[1] == 5:
            # Miligrama para Grama
            resultado.append(menu[2])
            resultado.append('mg')
            resultado.append(var)
            resultado.append('g')
        elif menu[1] == 6:
            # Miligrama para Quilograma
            resultado.append(menu[2])
            resultado.append('mg')
            resultado.append(var)
            resultado.append('Kg')
    if (menu[0] == 1 and menu[1] == 3) or (menu[0] == 1 and menu[1] == 4):
        resultado[2] = round(resultado[2], 1)

    resultado = json.dumps(resultado).encode('utf-8')
    client.send(resultado)

while True:
    try:
        menu = receber()
        menu[2] = int(menu[2])
        result = []
        print('Vetor recebeu: ', menu)
        # TEMPERATURA
        if menu[0] == 1:
            if menu[1] == 1:
                # Celsius para Fahrenheit
                valorFar = 1.8 * menu[2] + 32
                enviar(valorFar, result)
            elif menu[1] == 2:
                # Celsius para Kelvin
                valorKel = menu[2] + 273
                enviar(valorKel, result)
            elif menu[1] == 3:
                # Fahrenheit para Celcius
                valorC = (menu[2]-32)/1.8
                enviar(valorC, result)
            elif menu[1] == 4:
                # Fahrenheit para Kelvin
                valorKel = (menu[2]-32) * 5/9 + 273
                enviar(valorKel, result)
            elif menu[1] == 5:
                # Kelvin para Celcius
                valorC = menu[2] - 273
                enviar(valorC, result)
            elif menu[1] == 6:
                # Kelvin para Fahrenheit
                valorFar = (menu[2]-273) * 1.8 + 32
                enviar(valorFar, result)
        # COMPRIMENTO
        elif menu[0] == 2:
            if menu[1] == 1:
                # Metros para Kilometros
                valorKM = menu[2]/1000
                enviar(valorKM, result)
            elif menu[1] == 2:
                # Metros para Centímetros
                valorCM = menu[2] * 100
                enviar(valorCM, result)
            elif menu[1] == 3:
                # Kilometros para Metros
                valorM = menu[2] * 1000
                enviar(valorM, result)
            elif menu[1] == 4:
                # Kilometros para Centímetros
                valorCM = menu[2] * 100000
                enviar(valorCM, result)
            elif menu[1] == 5:
                # Centímetros para Metros
                valorM = menu[2] / 100
                enviar(valorM, result)
            elif menu[1] == 6:
                # Centímetros para Kilometros
                valorM = menu[2] / 100000
                enviar(valorM, result)
        # ÁREA
        elif menu[0] == 3:
            if menu[1] == 1:
                # Metros Quadrados para Kilometros Quadrados
                valorKM = menu[2]/1000000
                enviar(valorKM, result)
            elif menu[1] == 2:
                # Metros Quadrados para Centímetros Quadrados
                valorCM = menu[2] * 10000
                enviar(valorCM, result)
            elif menu[1] == 3:
                # Kilometros Quadrados para Metros Quadrados
                valorM = menu[2] * 1000000
                enviar(valorM, result)
            elif menu[1] == 4:
                # Kilometros Quadrados para Centímetros Quadrados
                valorcm = menu[2] * 10000000000
                enviar(valorcm, result)
            elif menu[1] == 5:
                # Centímetros Quadrados para Metros Quadrados
                valorm = menu[2] / 10000
                enviar(valorm, result)
            elif menu[1] == 6:
                # Centímetros Quadrados para Kilometros Quadrados
                valorkm = menu[2] / 10000000000
                enviar(valorkm, result)
        # GRAMA
        elif menu[0] == 4:
            if menu[1] == 1:
                # Grama para Quilograma
                valorQM = menu[2] / 1000
                enviar(valorQM, result)
            elif menu[1] == 2:
                # Grama para Miligrama
                valorMG = menu[2] * 100
                enviar(valorMG, result)
            elif menu[1] == 3:
                # Quilograma para Grama
                valorG = menu[2] * 1000
                enviar(valorG, result)
            elif menu[1] == 4:
                # Quilograma para Miligrama
                valormg = menu[2] * 1000000
                enviar(valormg, result)
            elif menu[1] == 5:
                # Miligrama para Grama
                valorg = menu[2] / 1000
                enviar(valorg, result)
            elif menu[1] == 6:
                # Miligrama para Quilograma
                valorqm = menu[2] / 1000000
                enviar(valorqm, result)
        result.clear()
    except:
        print('Conexão encerrada!')
        client.close()
        print('Aguardando conexão...')
        client, addr = server.accept()
        print(f'Servidor conectado a {addr}')