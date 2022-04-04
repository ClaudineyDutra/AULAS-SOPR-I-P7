from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import json

# --------------- CRIANDO CONEXÃO ---------------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('localhost', 9999))

    # --------------- FUNÇÕES ---------------
    def addConversao():
        unidade = vConversao.get()
        valores[1] = unidade


    def obterConversoes():
        valor = vMedida.get()
        valores[0] = valor

        if valor == 1:
            txt1 = "CELCIUS -> FAHRENHEIT"
            txt2 = "CELCIUS -> KELVIN"
            txt3 = "FAHRENHEIT -> CELCIUS"
            txt4 = "FAHRENHEIT -> KELVIN"
            txt5 = "KELVIN -> CELCIUS"
            txt6 = "KELVIN -> FAHRENHEIT"
        elif valor == 2:
            txt1 = "METROS -> KILOMETROS"
            txt2 = "METROS -> CENTÍMETROS"
            txt3 = "KILOMETROS -> METROS"
            txt4 = "KILOMETROS -> CENTÍMETROS"
            txt5 = "CENTÍMETROS -> METROS"
            txt6 = "CENTÍMETROS -> KILOMETROS"
        elif valor == 3:
            txt1 = "METROS² -> KILOMETROS²"
            txt2 = "METROS² -> CENTÍMETROS²"
            txt3 = "KILOMETROS² -> METROS²"
            txt4 = "KILOMETROS² -> CENTÍMETROS²"
            txt5 = "CENTÍMETROS² -> METROS²"
            txt6 = "CENTÍMETROS² -> KILOMETROS²"
        elif valor == 4:
            txt1 = "GRAMA -> QUILOGRAMA"
            txt2 = "GRAMA -> MILIGRAMA"
            txt3 = "QUILOGRAMA -> GRAMA"
            txt4 = "QUILOGRAMA -> MILIGRAMA"
            txt5 = "MILIGRAMA -> GRAMA"
            txt6 = "MILIGRAMA -> QUILOGRAMA"

        opc_1 = Radiobutton(fm_conversoes, text=txt1, value=1, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_1.place(x=50, y=80, width=300, height=40)

        opc_2 = Radiobutton(fm_conversoes, text=txt2, value=2, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_2.place(x=50, y=125, width=300, height=40)

        opc_3 = Radiobutton(fm_conversoes, text=txt3, value=3, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_3.place(x=50, y=170, width=300, height=40)

        opc_4 = Radiobutton(fm_conversoes, text=txt4, value=4, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_4.place(x=50, y=215, width=300, height=40)

        opc_5 = Radiobutton(fm_conversoes, text=txt5, value=5, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_5.place(x=50, y=260, width=300, height=40)

        opc_6 = Radiobutton(fm_conversoes, text=txt6, value=6, indicatoron=0, cursor="hand2", variable=vConversao,
                            command=addConversao, bg="#4973F2")
        opc_6.place(x=50, y=305, width=300, height=40)


    def receberDados():
        # Deserializando
        valorConvertido = client.recv(1024)
        valorConvertido = valorConvertido.decode('utf-8')
        valorConvertido = json.loads(valorConvertido)

        # Mostrando no terminal o valor recibido
        print('Resultado: ', valorConvertido[2])

        # Atualizando dados na label
        valor_convertido['text'] = f' {valorConvertido[2]} {valorConvertido[3]}'
        unidade_conversao['text'] = f'{valorConvertido[1]}'

        # Inserindo as informações no registro
        reg.insert("", "end", values=(valorConvertido[0], valorConvertido[1], valorConvertido[2], valorConvertido[3]))


    def enviarDados(valores):
        valores[2] = valor_conversao.get()
        if valores[2] == '':
            messagebox.showinfo(title="ERRO", message="Insira um valor para ser convertido")
        elif valores[0] == 0 or valores[1] == 0:
            messagebox.showinfo(title="ERRO", message="Escolha a conversão")
        else:
            valores = json.dumps(valores)
            valores = valores.encode('utf-8')
            client.send(valores)

            valores = json.loads(valores.decode('utf-8'))
            print("Você enviou: ", valores)
            receberDados()
            valores.pop()


    # --------------- INTERFACE ---------------
    interface = Tk()
    interface.title("Conversor de Medidas")
    interface.geometry("800x600")

    # --------------- VARIAVÉIS ---------------
    vMedida = IntVar()
    vConversao = IntVar()
    valores = [0, 0, 0]

    # Notebook
    nb = ttk.Notebook(interface)
    nb.place(x=0, y=0, width=800, height=600)

    # --------------- ABA DO CONVERSOR ---------------
    aba_conversor = Frame(nb)
    nb.add(aba_conversor, text="CONVERSOR")

    txt = Label(aba_conversor, text="CONVERSOR DE MEDIDAS", bg='#0634BF', font=('Impact', 40))
    txt.place(x=0, y=0, width=800, height=50)

    # -----> FRAME DAS OPÇÕES DE MEDIDA <-----
    fm_medidas = LabelFrame(aba_conversor, text="ESCOLHA A MEDIDA", borderwidth=1, relief="solid", bg='#0634BF', font=('Impact', 15))
    fm_medidas.place(x=0, y=50, width=400, height=400)

    # OPÇÕES
    opc_1 = Radiobutton(fm_medidas, text="TEMPERATURA", value=1, indicatoron=0, cursor="hand2", variable=vMedida,
                        command=obterConversoes, bg='#8F9AD9')
    opc_1.place(x=50, y=80, width=300, height=50)

    opc_2 = Radiobutton(fm_medidas, text="COMPRIMENTO", value=2, indicatoron=0, cursor="hand2", variable=vMedida,
                        command=obterConversoes, bg='#8F9AD9')
    opc_2.place(x=50, y=140, width=300, height=50)

    opc_3 = Radiobutton(fm_medidas, text="ÁREA", value=3, indicatoron=0, cursor="hand2", variable=vMedida,
                        command=obterConversoes, bg='#8F9AD9')
    opc_3.place(x=50, y=200, width=300, height=50)

    opc_4 = Radiobutton(fm_medidas, text="MASSA", value=4, indicatoron=0, cursor="hand2", variable=vMedida,
                        command=obterConversoes, bg='#8F9AD9')
    opc_4.place(x=50, y=260, width=300, height=50)

    # -----> FRAME DAS OPÇÕES DE CONVERSÃO <-----
    fm_conversoes = LabelFrame(aba_conversor, text="ESCOLHA A CONVERSÃO", borderwidth=1, relief="solid", bg='#0634BF', font=('Impact', 15))
    fm_conversoes.place(x=400, y=50, width=400, height=400)

    # ---------> FRAME DA CONVERSÃO <---------
    fm_conversao = Frame(aba_conversor, bg='#0634BF')
    fm_conversao.place(x=0, y=450, width=800, height=80)

    txt_valor_conversao = Label(fm_conversao, text="VALOR PARA CONVERSÃO", bg='#0634BF', fg='#FFFFFF')
    txt_valor_conversao.place(x=100, y=5, width=150, height=20)

    valor_conversao = Entry(fm_conversao, borderwidth=1, relief='solid', font=('Impact', 20))
    valor_conversao.place(x=100, y=25, width=150, height=40)

    unidade_conversao = Label(fm_conversao, bg='#0634BF', font=('Impact', 20))
    unidade_conversao['text'] = ''
    unidade_conversao.place(x=250, y=25, width=50, height=40)

    caixa_valor_convertido = LabelFrame(fm_conversao, text='VALOR CONVERTIDO', borderwidth=1, relief="solid", bg='#0634BF')
    caixa_valor_convertido.place(x=500, y=5, width=200, height=60)

    valor_convertido = Label(caixa_valor_convertido, font=('Impact', 20), bg='#0634BF')
    valor_convertido['text'] = ''
    valor_convertido.pack()

    # ---------> FRAME DOS BOTÕES <---------
    fm_botoes = Frame(aba_conversor, bg='#0634BF')
    fm_botoes.place(x=0, y=530, width=800, height=120)

    button_converter = Button(fm_botoes, text="CONVERTER", cursor="hand2", command=lambda: enviarDados(valores))
    button_converter.place(x=150, y=0, width=200, height=40)

    button_sair = Button(fm_botoes, text="SAIR", cursor="hand2", command=lambda: interface.quit())
    button_sair.place(x=450, y=0, width=200, height=40)

    # --------------- ABA DOS REGISTROS ---------------
    aba_registros = Frame(nb)
    nb.add(aba_registros, text="REGISTROS")

    # ---------> TREEVIEW <---------
    reg = ttk.Treeview(aba_registros, columns=('v_conversao', 'uni_conversao', 'v_convertido', 'uni_convertido'), show="headings",)
    reg.column('v_conversao', minwidth=0, width=200)
    reg.column('uni_conversao', minwidth=0, width=200)
    reg.column('v_convertido', minwidth=0, width=200)
    reg.column('uni_convertido', minwidth=0, width=200)

    reg.heading('v_conversao', text='VALOR PARA CONVERTER')
    reg.heading('uni_conversao', text='UNIDADE PARA CONVERTER')
    reg.heading('v_convertido', text='VALOR CONVERTIDO')
    reg.heading('uni_convertido', text='UNIDADE CONVERTIDA')

    sb = Scrollbar(aba_registros, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    reg.config(yscrollcommand=sb.set)
    sb.config(command=reg.yview)

    reg.pack(fill=Y, expand=True)

    # ---------> FRAME DO BOTÃO DE SAIR <---------
    fm_botoes_reg = Frame(aba_registros, bg="#0634BF")
    fm_botoes_reg.place(x=0, y=530, width=800, height=50)

    button_sair = Button(fm_botoes_reg, text="SAIR", cursor="hand2", command=lambda: interface.quit())
    button_sair.place(x=300, y=5, width=200, height=35)

    interface.mainloop()
except:
    print('Conexão não estabelecida')
