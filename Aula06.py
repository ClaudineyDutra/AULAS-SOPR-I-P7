# DEFINIÇÃO DE VARIÁVEIS GLOBAIS
tot = []

# FUNÇÃO PARA CRIAR UM CABEÇALHO
def Cabecalho():
  print('+-------------------------+---------------+---------------+---------------+---------------+---------------+')
  print('|{:^105s}|'.format('LISTA DE PRODUTOS'))
  print('+-------------------------+---------------+---------------+---------------+---------------+---------------+')
  print('|{:^25s}|{:^15s}|{:^15s}|{:^15s}|{:^15s}|{:^15s}|'.format('Lista de Produtos', 'QTD Entradas', 'QTD Saídas', 'Saldo Estoque', 'Preço Unitário', 'Subtotal'))

# FUNÇÃO PARA ESCREVER LINHA
def escreverLinha():
  print('+-------------------------+---------------+---------------+---------------+---------------+---------------+')

# FUNÇÃO PARA CADASTRAR UM PRODUTO
def cadastrarProduto(nome, qtdEntrada, qtdSaida, preco):
  qtdEstoque = qtdEntrada - qtdSaida
  Subtotal = preco * qtdEstoque
  tot.append(Subtotal)
  print('|{:<25s}|{:15d}|{:15d}|{:15d}|{:15.2f}|{:15.2f}|'.format(nome, qtdEntrada, qtdSaida, qtdEstoque, preco, Subtotal))

# FUNÇÃO PARA MOSTRAR OS PRODUTOS CADASTRADOS
def Produtos():
  cadastrarProduto('Azeite de Oliva', 100, 40, 21.90)
  cadastrarProduto('Castanha do Pará', 100, 5, 6)
  cadastrarProduto('Flocos de Aveia', 1000, 200, 10.90)
  cadastrarProduto('Paçoca de Amendoim', 100, 8, 1.50)
  cadastrarProduto('Panetone sem Gluten', 100, 60, 17.30)
  cadastrarProduto('Pão Sirio Integral', 100, 70, 5.90)
  cadastrarProduto('Polpa de Açai Natural', 100, 1, 7.10)
  cadastrarProduto('Queijo Vegano PCT', 100, 30, 25)

# FUNÇÃO PARA CALCULAR O VALOR TOTAL
def Total():
  print('|{0:<25s} {0:15s} {0:15s} {0:15s}|{1:^15s}|{2:15.2f}|'.format('', 'TOTAL', sum(tot)))


# MONTANDO A TABELA
Cabecalho()
escreverLinha()
Produtos()
escreverLinha()
Total()
escreverLinha()
