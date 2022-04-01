import json
import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    cliente.connect(('localhost', 7777))
except:
    print('Conexão não estabelecida')

valores = []
menu = 1

while menu != 0:
    try:
        menu = int(input("'1' para continuar e '0' para sair"))
        if menu == 1:
            peso = float(input('Peso> '))
            valores.append(peso)
            alt = float(input('Altura> '))
            valores.append(alt)

            env = json.dumps(valores).encode('utf-8')
            cliente.send(env)

            imc = cliente.recv(1024)
            seuIMC = imc.decode('utf-8')
            seuIMC = json.loads(seuIMC)

            print(f'Seu IMC é {seuIMC}')
            valores.clear()
    except:
        print('Tente de novo')
    
    if menu == 0:
        print('Você saiu')
        cliente.close()