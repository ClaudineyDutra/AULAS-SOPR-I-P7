#C:\\Users\\Alunos\\PycharmProjects\\aulas-sopr-I-p7\\CalculadoraGeometrica\\venv
import cgitb
import cgi
import geo_funcs
# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

def area(base, altura):
    area_tri = (base * altura) / 2

    geo_funcs.print_header(title)
    print("<h1>Triângulo</h1><hr>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Área do Triângulo: {:.1f} </p>".format(area_tri))
    print("<br><br>Clique <a href=\'../triangulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def perimetro(base, lado1,lado2):
    per_tri = base + lado1 + lado2

    geo_funcs.print_header(title)
    print("<h1>Triângulo</h1><hr>")
    print("<p>Base {}</p>".format(base))
    print("<p>Lado: {:.1f}".format(lado1))
    print("<p>Lado: {:.1f}".format(lado2))
    print("<p>Perímetro do Triângulo: {:.1f} </p>".format(per_tri))
    print("<br><br>Clique <a href=\'../triangulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def ambos(base, altura, lado1, lado2):
    per_tri = base + lado1 + lado2
    area_tri = (base * altura) / 2

    geo_funcs.print_header(title)
    print("<h1>Triângulo</h1><hr>")
    print("<p>Base {}</p>".format(base))
    print("<p>Lado {}</p>".format(lado1))
    print("<p>Lado {}</p>".format(lado2))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Perímetro do Triângulo: {:.1f} </p>".format(per_tri))
    print("<p>Área do Triângulo: {:.1f} </p>".format(area_tri))
    print("<br><br>Clique <a href=\'../triangulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

# recebe o valor do lado do usuario
option = int(form.getvalue('escolha'))
base_ = float(form.getvalue('base'))
altura_ = float(form.getvalue('altura'))
lado1_ = float(form.getvalue('lado1'))
lado2_ = float(form.getvalue('lado2'))
title = "Triângulo"

if option == 0:
    perimetro(base_, altura_)
elif option == 1:
    area(base_, lado1_, lado2_)
elif option == 2:
    ambos(base_, altura_, lado1_, lado2_)