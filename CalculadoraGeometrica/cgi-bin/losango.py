#C:\Users\Alunos\PycharmProjects\aulas-sopr-I-p7\
import cgitb
import cgi
import geo_funcs
# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

def area(diagonal_maior, diagonal_menor):
    area_los = diagonal_maior * diagonal_menor

    geo_funcs.print_header(title)
    print("<h1>Losango</h1>")
    print("<p>Diagonal Maior {}</p>".format(diagonal_maior))
    print("<p>Diagonal Menor: {:.1f}".format(diagonal_menor))
    print("<p>Área do Losango: {:.1f} </p>".format(area_los))
    print("<a href=\'../losango.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

def perimetro(lado):
    per_los = lado * 4

    geo_funcs.print_header(title)
    print("<h1>Losango</h1>")
    print("<p>Lado: {}".format(lado))
    print("<p>Perímetro do Losango: {:.1f} </p>".format(per_los))
    print("<a href=\'../losango.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

def ambos(diagonal_maior, diagonal_menor, lado):
    per_los = lado * 4
    area_los = diagonal_maior * diagonal_menor

    geo_funcs.print_header(title)
    print("<h1>Losango</h1>")
    print("<p>Lado {}</p>".format(lado))
    print("<p>Diagonal Maior {}</p>".format(diagonal_maior))
    print("<p>Diagonal Menor: {}</p>".format(diagonal_menor))
    print("<p>Perímetro do Losango: {:.1f} </p>".format(per_los))
    print("<p>Área do Losango: {} </p>".format(area_los))
    print("<a href=\'../losango.html\'><button class='buttom'>Calcular novamente</button></a>")
    geo_funcs.print_footer()

# recebe o valor do lado do usuario
option = int(form.getvalue('escolha'))
lado_ = float(form.getvalue('lado'))
diaMaior_ = float(form.getvalue('diaMaior'))
diaMenor_ = float(form.getvalue('diaMenor'))
title = "Losango"

if option == 0:
    perimetro(lado_)
elif option == 1:
    area(diaMaior_, diaMenor_)
elif option == 2:
    ambos(diaMaior_, diaMenor_, lado_)