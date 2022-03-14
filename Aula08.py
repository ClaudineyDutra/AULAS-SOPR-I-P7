# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
class Carro():
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
    combustivel = 0
# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
    def __init__(self, consumo):
        self.consumo = consumo    

# Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    def andar(self, andar_km):
        km_rodados = andar_km
        while(km_rodados > 0):
            km_rodados -= self.consumo
            self.combustivel -= 1
            if(self.combustivel == 0):
                print(f'Você andou {km_rodados} e o seu combustivel acabou!')
            if(km_rodados <= 0):
                print(f'Você andou {andar_km}')

# Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    def obterGasolina(self):
        print(f'Quantidade de Gasolina restante é {self.combustivel}')

# Forneça um método adicionarGasolina( ), para abastecer o tanque.
    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade
# Executando o script
meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()
