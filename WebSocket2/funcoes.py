import json
def menu():
    print('+--------------------------------------------------+')
    print('|{:^50s}|'.format('-> CONVERSOR DE MEDIDAS <-'))
    print('+--------------------------------------------------+')
    print('|{:50s}|'.format('1 - TEMPERATURA'))
    print('|{:50s}|'.format('2 - COMPRIMENTO'))
    print('|{:50s}|'.format('3 - ÁREA'))
    print('|{:50s}|'.format('4 - MASSA'))
    print('|{:50s}|'.format('5 - SAIR'))
    print('+--------------------------------------------------+')
    valor = int(input('ESCOLHA A MEDIDA: '))
    return valor

def opcao01():
    while True:
        try:
            print('+--------------------------------------------------+')
            print('|{:^50s}|'.format('-> CONVERSÕES PARA TEMPERATURA <-'))
            print('+--------------------------------------------------+')
            print('|{:50s}|'.format('1 - CELCIUS -> FAHRENHEIT'))
            print('|{:50s}|'.format('2 - CELCIUS -> KELVIN'))
            print('|{:50s}|'.format('3 - FAHRENHEIT -> CELCIUS'))
            print('|{:50s}|'.format('4 - FAHRENHEIT -> KELVIN'))
            print('|{:50s}|'.format('5 - KELVIN -> CELCIUS'))
            print('|{:50s}|'.format('6 - KELVIN -> FAHRENHEIT'))
            print('+--------------------------------------------------+')
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
            print('Valor Inválido, tente novamente!')

def opcao02():
    while True:
        try:
            print('+--------------------------------------------------+')
            print('|{:^50s}|'.format('-> CONVERSÕES PARA COMPRIMENTO <-'))
            print('+--------------------------------------------------+')
            print('|{:50s}|'.format('1 - METROS -> KILOMETROS'))
            print('|{:50s}|'.format('2 - METROS -> CENTÍMETROS'))
            print('|{:50s}|'.format('3 - KILOMETROS -> METROS'))
            print('|{:50s}|'.format('4 - KILOMETROS -> CENTÍMETROS'))
            print('|{:50s}|'.format('5 - CENTÍMETROS -> METROS'))
            print('|{:50s}|'.format('6 - CENTÍMETROS -> KILOMETROS'))
            print('+--------------------------------------------------+')
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
            print('Valor Inválido, tente novamente!')

def opcao03():
    while True:
        try:
            print('+--------------------------------------------------+')
            print('|{:^50s}|'.format('-> CONVERSÕES PARA ÁREA <-'))
            print('+--------------------------------------------------+')
            print('|{:50s}|'.format('1 - METROS -> KILOMETROS'))
            print('|{:50s}|'.format('2 - METROS -> CENTÍMETROS'))
            print('|{:50s}|'.format('3 - KILOMETROS -> METROS'))
            print('|{:50s}|'.format('4 - KILOMETROS -> CENTÍMETROS'))
            print('|{:50s}|'.format('5 - CENTÍMETROS -> METROS'))
            print('|{:50s}|'.format('6 - CENTÍMETROS -> KILOMETROS'))
            print('+--------------------------------------------------+')
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
         print('Valor Inválido, tente novamente!')

def opcao04():
    while True:
        try:
            print('+--------------------------------------------------+')
            print('|{:^50s}|'.format('-> CONVERSÕES PARA MASSA <-'))
            print('+--------------------------------------------------+')
            print('|{:50s}|'.format('1 - GRAMA -> QUILOGRAMA'))
            print('|{:50s}|'.format('2 - GRAMA -> MILIGRAMA'))
            print('|{:50s}|'.format('3 - QUILOGRAMA -> GRAMA'))
            print('|{:50s}|'.format('4 - QUILOGRAMA -> MILIGRAMA'))
            print('|{:50s}|'.format('5 - MILIGRAMA -> GRAMA'))
            print('|{:50s}|'.format('6 - MILIGRAMA -> QUILOGRAMA'))
            print('+--------------------------------------------------+')
            valor = int(input('ESCOLHA A CONVERSÃO: '))
            if valor!=1 and valor!=2 and valor!=3 and valor!=4 and valor!=5 and valor!=6:
                raise Exception
            return valor
            break
        except:
            print('Valor Inválido, tente novamente!')

def enviar(vetor, client):
    vetor = json.dumps(vetor).encode('utf-8')
    client.send(vetor)

    vetor = vetor.decode('utf-8')
    vetor = json.loads(vetor)
    vetor.clear()

def receber(client):
    msg = client.recv(1024)
    msg = msg.decode('utf-8')
    msg = json.loads(msg)
    return msg
