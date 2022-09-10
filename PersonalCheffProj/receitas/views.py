from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    
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