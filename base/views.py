from django.shortcuts import render
from .models import Transacao

def home_page(request):
    
    transacoes = Transacao.objects.all()
    
    for transacao in transacoes:
        print(transacao.nome)
    
    context = {
        'transacoes': transacoes
    }

    return render(request, 'pages/home_page.html', context)

def transactions_page(request):
    return render(request, 'pages/transactions_page.html')

def categories_page(request):
    return render(request, 'pages/categories_page.html')