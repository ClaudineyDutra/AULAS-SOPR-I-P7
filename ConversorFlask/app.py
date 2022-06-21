from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/temperatura/", methods=['POST', 'GET'])
def conversor_temp():
    if request.method == 'POST':
        valor = float(request.form['valor'])
        conversao = request.form['conversao']

        if conversao == 'Kelvin_Celcius':
            resultado = valor - 273
        elif conversao == 'Kelvin_Fahrenheit':
            resultado = (valor - 273) * 1.8 + 32
        elif conversao == 'Celcius_Fahrenheit':
            resultado = 1.8 * valor + 32
        elif conversao == 'Celcius_Kelvin':
            resultado = valor + 273
        elif conversao == 'Fahrenheit_Celcius':
            resultado = (valor - 32) / 1.8
        elif conversao == 'Fahrenheit_Kelvin':
            resultado = (valor - 32) * 5 / 9 + 273
        return render_template('temperatura.html', resultado=resultado)
    return render_template('temperatura.html')


@app.route("/comprimento/", methods=['POST', 'GET'])
def comprimento():
    if request.method == 'POST':
        valor = float(request.form['valor'])
        conversao = request.form['conversao']

        if conversao == 'Metro_Kilometro':
            resultado = valor / 1000
        elif conversao == 'Metro_Hectometro':
            resultado = valor / 100
        elif conversao == 'Metro_Decametro':
            resultado = valor / 10
        elif conversao == 'Metro_Centimetro':
            resultado = valor * 100
        elif conversao == 'Metro_Decimetro':
            resultado = valor * 10
        elif conversao == 'Metro_Milimetro':
            resultado = valor * 1000
        return render_template('comprimento.html', resultado=resultado)
    return render_template('comprimento.html')



@app.route("/massa/", methods=['POST', 'GET'])
def conversor_massa():
    if request.method == 'POST':
        valor = float(request.form['valor'])
        conversao = request.form['conversao']

        if conversao == 'Grama_Kilograma':
            resultado = valor/1000
        elif conversao == 'Grama_Hectagrama':
            resultado = valor/100
        elif conversao == 'Grama_decagrama':
            resultado = valor/10
        elif conversao == 'Grama_decigrama':
            resultado = valor * 100
        elif conversao == 'Grama_Centigrama':
            resultado = valor * 10
        elif conversao == 'Grama_Miligrama':
            resultado = valor * 1000
        return render_template('massa.html', resultado=resultado)
    return render_template('massa.html')