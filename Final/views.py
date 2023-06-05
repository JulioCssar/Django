from django.http import HttpResponse
from django.template import Template, Context
#importação para manipulação de arquivos internos


def login(request):
    documentoExterno = open("C:/Users/Admin/Desktop/projetof/Final/pages/login.html")
    pagina = Template(documentoExterno.read())
    documentoExterno.close()
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)

def pagina(request):
    nome = "Matheus"
    sobrenome = "Sacramento"
    #0-masculino 1-femino 2-neutro 
    genero = 0
    documentoExterno = open("C:/Users/Admin/Desktop/projetof/Final/pages/page.html")
    pagi = Template(documentoExterno.read())
    documentoExterno.close()
    ctx = Context({"nomeUsuario": nome, "sobrenome": sobrenome, "genero": genero})
    documento = pagi.render(ctx)
    return HttpResponse(documento)

def cadastro(request):
    documentoExterno = open("C:/Users/Admin/Desktop/projetof/Final/pages/cadastro.html")
    pagina = Template(documentoExterno.read())
    documentoExterno.close()
    ctx = Context()
    documento = pagina.render(ctx)
    return HttpResponse(documento)