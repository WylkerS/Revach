from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Transacao

def transactions_create(request):
    
    tipos = Transacao.TipoTransacao.choices   
    categorias = Categoria.objects.all()
    
    context = {
        'categorias': categorias,
        'tipos': tipos
    }

    return render(request, 'partials/htmx_components/modal_create_transaction.html', context)

def transactions_tipo(request):
    
    tipo = request.GET.get('tipo')
    
    if tipo == 'Parcelada':
        return render(request, 'partials/htmx_components/parcelada_fields.html')
    
    return HttpResponse("")