#C:\\Users\\Lenovo\\PycharmProjects\\aulas-sopr-I-p7\\CalculadoraGeometrica\\venv
import cgitb
import cgi
import math
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

def area(raio):
    area_circ = math.pi * math.pow(raio_, 2)

    geo_funcs.print_header(title)
    print("<h1>Círculo</h1><hr>")
    print("<p>Raio: {:.1f}</p>".format(raio))
    print("<p>Área do círculo: {:.1f}</p>".format(area_circ))
    print("<br><br>Clique <a href=\'../circulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def perimetro(raio):
    per_circ = 2 * math.pi * raio

    geo_funcs.print_header(title)
    print("<h1>Círculo</h1><hr>")
    print("<p>Raio: {:.1f}".format(raio))
    print("<p>Perímetro do círculo: {:.1f}".format(per_circ))
    print("<br><br>Clique <a href=\'../circulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def ambos(raio):
    per_circ = 2 * math.pi * raio
    area_circ = math.pi * math.pow(raio_, 2)

    geo_funcs.print_header(title)
    print("<h1>Círculo</h1><hr>")
    print("<p>Base {}</p>".format(raio))
    print("<p>Perímetro do Círculo: {:.1f} </p>".format(per_circ))
    print("<p>Área do Círculo: {:.1f} </p>".format(area_circ))
    print("<br><br>Clique <a href=\'../circulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()


# recebe o valor do lado do usuario
option = int(form.getvalue('escolha'))
raio_ = float(form.getvalue('raio'))
title = "Círculo"

if option == 0:
    perimetro(raio_)
elif option == 1:
    area(raio_)
elif option == 2:
    ambos(raio_)

