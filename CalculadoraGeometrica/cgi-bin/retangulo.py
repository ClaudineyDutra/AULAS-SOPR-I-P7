#C:\Users\Lenovo\Desktop\aulas-sopr-I-p7\
import cgitb
import cgi
import geo_funcs
# habilita a visualizacao de erros
cgitb.enable(display=0, logdir="./")

# instancia um form para receber dados do navegador
form = cgi.FieldStorage()

def area(base, altura):
    area_ret = base * altura

    geo_funcs.print_header(title)
    print("<h1>Retângulo</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Área do Retângulo: {:.1f} </p>".format(area_ret))
    print("Clique <a href=\'../retangulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def perimetro(base, altura):
    per_ret = (base * 2) + (altura *2)

    geo_funcs.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Perímetro do Retângulo: {:.1f} </p>".format(per_ret))
    print("Clique <a href=\'../retangulo.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

def ambos(base, altura):
    per_ret = (base * 2) + (altura *2)
    area_ret = base * altura

    geo_funcs.print_header(title)
    print("<h1>Quadrado</h1>")
    print("<p>Base {}</p>".format(base))
    print("<p>Altura: {:.1f}".format(altura))
    print("<p>Perímetro do Retângulo: {:.1f} </p>".format(per_ret))
    print("<p>Área do Retângulo: {:.1f} </p>".format(area_ret))
    print("Clique <a href=\'../quadrado.html\'>aqui</a> para novo cálculo.")
    geo_funcs.print_footer()

# recebe o valor do lado do usuario
option = int(form.getvalue('escolha'))
base_ = float(form.getvalue('base'))
altura_ = float(form.getvalue('altura'))
title = "Retângulo"

if option == 0:
    perimetro(base_, altura_)
elif option == 1:
    area(base_, altura_)
elif option == 2:
    ambos(base_, altura_)


