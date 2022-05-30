#C:\Users\Alunos\PycharmProjects\aulas-sopr-I-p7\

import cgitb
import cgi
import geo_funcs

# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

def area(valor):
    area_quad = valor * valor

    geo_funcs.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Lado {}</p>".format(valor))
    print("<p>Área do Quadrado: {} </p>".format(area_quad))
    print("<a href=\'../quadrado.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

def perimetro(valor):
    per_quad = valor * 4

    geo_funcs.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Lado {}</p>".format(valor))
    print("<p>Perímetro do Quadrado: {} </p>".format(per_quad))
    print("<a href=\'../quadrado.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

def ambos(valor):
    per_quad = valor * 4
    area_quad = valor * valor

    geo_funcs.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Lado {}</p>".format(valor))
    print("<p>Perímetro do Quadrado: {} </p>".format(per_quad))
    print("<p>Área do Quadrado: {} </p>".format(area_quad))
    print("<a href=\'../quadrado.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

# recebe o valor do lado do usuario
option = int(form.getvalue('escolha'))
lado_ = float(form.getvalue('lado'))
title = "Quadrado"

if option == 0:
    perimetro(lado_)
elif option == 1:
    area(lado_)
elif option == 2:
    ambos(lado_)