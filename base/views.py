from django.shortcuts import render
from .models import Transacao
from .forms import SelecaoMesForm
from .utils import get_data_navegacao

def home_page(request):
    transacoes = Transacao.objects.all()
    
    info_data = get_data_navegacao(request)
    data_ref = info_data['data_referencia']

    
    context = {
        **info_data['navegacao'],
        'data_referencia': data_ref,
        'transacoes': transacoes,
    }

    return render(request, 'pages/home_page.html', context)

def transactions_page(request):
    info_data = get_data_navegacao(request)
    data_ref = info_data['data_referencia']

    context = {
        **info_data['navegacao'],
        'data_referencia': data_ref,
    }

    return render(request, 'pages/transactions_page.html', context)

def categories_page(request):
    return render(request, 'pages/categories_page.html')