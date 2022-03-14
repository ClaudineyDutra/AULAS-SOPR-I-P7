import pickle
Arquivo = {}

def Cabecalho():
    print('+--------------------+----------+--------------------+')
    print('+{:^20s}+{:^10s}+{:^20s}+'.format('NOME', 'TELEFONE', 'EMAIL'))
    print('+--------------------+----------+--------------------+')

def mostrarTabela(nome, telefone, email):
    print('|{:20s}|{:10s}|{:20s}|'.format(nome, telefone, email))
    print('+--------------------+----------+--------------------+')

print('Para se cadastrar digite:')
nome = input('Nome:')
telefone = input('Telefone:')
email = input('Email:')

Arquivo = {'nome':nome ,'telefone': telefone, 'email': email}

with open ('Arquivo.pickle', 'ab') as f:
    pickle.dump(Arquivo, f)

with open ('Arquivo.pickle', 'rb') as f:
    array = []
    i = 0
    try:
        while(i != 1):
            array.append(pickle.load(f))
    except EOFError:
        Cabecalho()
        for n in range(0, len(array)):
            mostrarTabela(
                array[n]['nome'],
                array[n]['telefone'],
                array[n]['email']
                )
        print('Você viu toda a lista cadastrada!')
    except FileNotFoundError:
        print('Arquivo não existi!')
       