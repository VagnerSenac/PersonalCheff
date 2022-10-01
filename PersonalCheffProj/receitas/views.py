from django.shortcuts import render
from .models import Receitas

def index(request):
    receitas = Receitas.objects.all()
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