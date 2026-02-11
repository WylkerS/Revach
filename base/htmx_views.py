from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria, Transacao
from .utils import get_data_navegacao
from .forms import TransacaoForm

def transactions_create(request):
    
    if request.method == 'GET':
        form = TransacaoForm()
        tipos = Transacao.TipoTransacao.choices   
        categorias = Categoria.objects.all()
        
        info_data = get_data_navegacao(request)
        
        context = {
            'form': form,
            'categorias': categorias,
            'tipos': tipos,
            **info_data['navegacao']
        }

        print(f"Retornar modal de criação de transação.")
        return render(request, 'partials/htmx_components/modal_create_transaction.html', context)

def transactions_tipo(request):

    tipo = request.GET.get('tipo')
    
    if tipo == 'Parcelada':
        form = TransacaoForm()
        
        context = {
            'form': form,
            
        }
        
        print(f"Retornar campos para transação parcelada.")
        return render(request, 'partials/htmx_components/parcelada_fields.html', context)

    print(f"Tipo selecionado: {tipo}")
    return HttpResponse("")
    
    
        
        