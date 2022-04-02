import socket
import funcoes

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('localhost', 9999))
except:
    print('Conexão não estabelecida')

menu = 0
comando = []

while menu != 5:
    try:
        menu = funcoes.menu()
        # QUANDO TEMPERATURA FOR SELECIONADO
        if menu == 1:
            comando.append(menu)
            valor = funcoes.opcao01()
            comando.append(valor)
            if valor == 1:
                # Celsius para Fahrenheit
                num = float(input('VALOR EM CELSIUS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorFar = funcoes.receber(client)
                print(f'VALOR EM FAHRENHEIT: {round(valorFar, 1)} ºF')
                comando.clear()
            elif valor == 2:
                # Celsius para Kelvin
                num = float(input('VALOR EM CELCIUS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKel = funcoes.receber(client)
                print(f'VALOR EM KELVIN: {round(valorKel, 1)} K')
                comando.clear()
            elif valor == 3:
                # Fahrenheit para Celcius
                num = float(input('VALOR EM FAHRENHEIT: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorC = funcoes.receber(client)
                print(f'VALOR EM CELCIUS: {round(valorC, 1)} ºC')
                comando.clear()
            elif valor == 4:
                # Fahrenheit para Kelvin
                num = float(input('VALOR EM FAHRENHEIT: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKel = funcoes.receber(client)
                print(f'VALOR EM KELVIN: {round(valorKel, 1)} K')
                comando.clear()
            elif valor == 5:
                # Kelvin para Celcius
                num = float(input('VALOR EM KELVIN: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorC = funcoes.receber(client)
                print(f'VALOR EM CELCIUS: {round(valorC, 1)} ºC')
                comando.clear()
            elif valor == 6:
                # Kelvin para Fahrenheit
                num = float(input('VALOR EM KELVIN: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorFar = funcoes.receber(client)
                print(f'VALOR EM FAHRENHEIT: {round(valorFar, 1)} ºC')
                comando.clear()
        # QUANDO COMPRIMENTO FOR SELECIONADO
        elif menu == 2:
            comando.append(menu)
            valor = funcoes.opcao02()
            comando.append(valor)
            if valor == 1:
                # Metros para Kilometros
                num = float(input('VALOR EM METROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKM = funcoes.receber(client)
                print(f'VALOR EM KILOMETROS: {valorKM} Km')
                comando.clear()
            elif valor == 2:
                # Metros para Centímetros
                num = float(input('VALOR EM METROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorCM = funcoes.receber(client)
                print(f'VALOR EM CENTÍMETROS: {round(valorCM, 1)} cm')
                comando.clear()
            elif valor == 3:
                # Kilometros para Metros
                num = float(input('VALOR EM KILOMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorM = funcoes.receber(client)
                print(f'VALOR EM METROS: {round(valorM, 1)} m')
                comando.clear()
            elif valor == 4:
                # Kilometros para Centímetros
                num = float(input('VALOR EM KILOMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorCM = funcoes.receber(client)
                print(f'VALOR EM CENTÍMETROS: {round(valorCM, 1)} cm')
                comando.clear()
            elif valor == 5:
                # Centímetros para Metros
                num = float(input('VALOR EM CENTÍMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorM = funcoes.receber(client)
                print(f'VALOR EM METROS: {valorM} m')
                comando.clear()
            elif valor == 6:
                # Centímetros para Kilometros
                num = float(input('VALOR EM KILOMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKM = funcoes.receber(client)
                print(f'VALOR EM KILOMETROS: {valorKM} Km')
                comando.clear()
        # QUANDO ÁREA FOR SELECIONADO
        elif menu == 3:
            # Quando área for selecionado
            comando.append(menu)
            valor = funcoes.opcao03()
            comando.append(valor)
            if valor == 1:
                # Metros Quadrados para Kilometros Quadrados
                num = float(input('VALOR EM METROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKM = funcoes.receber(client)
                print(f'VALOR EM KILOMETROS QUADRADOS: {valorKM} Km²')
                comando.clear()
            elif valor == 2:
                # Metros Quadrados para Centímetros Quadrados
                num = float(input('VALOR EM METROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorCM = funcoes.receber(client)
                print(f'VALOR EM CENTÍMETROS QUADRADOS: {round(valorCM, 1)} cm²')
                comando.clear()
            elif valor == 3:
                # Kilometros Quadrados para Metros Quadrados
                num = float(input('VALOR EM KILOMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorM = funcoes.receber(client)
                print(f'VALOR EM METROS QUADRADOS: {round(valorM, 1)} m²')
                comando.clear()
            elif valor == 4:
                # Kilometros Quadrados para Centímetros Quadrados
                num = float(input('VALOR EM KILOMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorCM = funcoes.receber(client)
                print(f'VALOR EM CENTÍMETROS QUADRADOS: {round(valorCM, 1)} cm²')
                comando.clear()
            elif valor == 5:
                # Centímetros Quadrados para Metros Quadrados
                num = float(input('VALOR EM CENTÍMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorM = funcoes.receber(client)
                print(f'VALOR EM METROS QUADRADOS: {valorM} m²')
                comando.clear()
            elif valor == 6:
                # Centímetros Quadrados para Kilometros Quadrados
                num = float(input('VALOR EM CENTÍMETROS: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKM = funcoes.receber(client)
                print(f'VALOR EM KILOMETROS QUADRADOS: {valorKM} Km²')
                comando.clear()
        # QUANDO MASSA FOR SELECIONADO
        elif menu == 4:
            # QUANDO MASSA FOR SELECIONADO
            comando.append(menu)
            valor = funcoes.opcao04()
            comando.append(valor)
            if valor == 1:
                # Grama para Quilograma
                num = float(input('VALOR EM GRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKG = funcoes.receber(client)
                print(f'VALOR EM QUILOGRAMA: {valorKG} Kg')
                comando.clear()
            elif valor == 2:
                # Grama para Miligrama
                num = float(input('VALOR EM GRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorMG = funcoes.receber(client)
                print(f'VALOR EM MILIGRAMA: {round(valorMG, 1)} mg')
                comando.clear()
            elif valor == 3:
                # Quilograma para Grama
                num = float(input('VALOR EM QUILOGRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorG = funcoes.receber(client)
                print(f'VALOR EM GRAMA: {round(valorG, 1)} g')
                comando.clear()
            elif valor == 4:
                # Quilograma para Miligrama
                num = float(input('VALOR EM QUILOGRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorMG = funcoes.receber(client)
                print(f'VALOR EM MILIGRAMA: {round(valorMG, 1)} mg')
                comando.clear()
            elif valor == 5:
                # Miligrama para Grama
                num = float(input('VALOR EM MILIGRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorG = funcoes.receber(client)
                print(f'VALOR EM GRAMA: {valorG} g')
                comando.clear()
            elif valor == 6:
                # Miligrama para Quilograma
                num = float(input('VALOR EM MILIGRAMA: '))
                comando.append(num)
                funcoes.enviar(comando, client)

                valorKM = funcoes.receber(client)
                print(f'VALOR EM QUILOGRAMA: {valorKM} Kg')
                comando.clear()
        # SAIR
        elif menu == 5:
            print('Até mais!')
            comando.append(5)
            funcoes.enviar(comando, client)
        else:
            print('Por favor, escolher uma opção válida!')
    except:
        print('Tente novamente!')


