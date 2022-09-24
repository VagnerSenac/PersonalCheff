from django.shortcuts import render


def index(request):
    receitas={
        1:'Suco de Maçã',
        2:'Suco de Laranja',
        3:'Suco de Limão',
        4:'Suco de Abacaxi',
        5:'Suco de Melancia'
    }
    dados = {
        'lista_receitas': receitas
    }
    return render(request, 'index.html',dados)
    
def sucodelaranja(request):
    return render(request, 'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')

def sucodeabacaxi(request):
    return render(request, 'sucodeabacaxi.html')

def sucodemaca(request):
    return render(request, 'sucodemaca.html')

def sucodemelancia(request):
    return render(request, 'sucodemelancia.html')

def contato(request):
    return render(request, 'contato.html')