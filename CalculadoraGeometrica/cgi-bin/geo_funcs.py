#C:\Users\Alunos\PycharmProjects\aulas-sopr-I-p7\
def print_header(title):
    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <title>{}</title>
                    <link rel="stylesheet" href=\'../css/resultado.css\'>
                </head>
                <body>""".format(title))


def print_footer():
    print("</body></html>")