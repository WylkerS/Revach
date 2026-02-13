from django.shortcuts import render, redirect
from .models import Transacao, Categoria
from .utils import get_data_navegacao
from .forms import TransacaoForm

def home_page(request):
    
    info_data = get_data_navegacao(request)
    data_ref = info_data['data_referencia']
    
    transacoes = Transacao.objects.filter(data_lancamento=data_ref)[:5]
    
    valor_entrada = 0
    valor_despesa = 0
    for transacao in transacoes:
        
        if transacao.categoria.entrada:
            valor_entrada += transacao.valor
        else:
            valor_despesa += transacao.valor
            
    saldo = valor_entrada - valor_despesa    
    
    context = {
        **info_data['navegacao'],
        'data_referencia': data_ref,
        'transacoes': transacoes,
        'valor_entrada': valor_entrada,
        'valor_despesa': valor_despesa,
        'saldo': saldo,
    }

    return render(request, 'pages/home_page.html', context)

def transactions_page(request):
    info_data = get_data_navegacao(request)
    data_ref = info_data['data_referencia']
    
    form = TransacaoForm()
    categorias = Categoria.objects.all()
    tipos = Transacao.TipoTransacao.values
    
    transacoes = Transacao.objects.filter(data_lancamento=data_ref)[:5]
    
    context = {
        'transacoes': transacoes,
        
        **info_data['navegacao'],
        'data_referencia': data_ref,
        
        'form': form,
        'categorias': categorias,
        'tipos': tipos,
        
    }

    return render(request, 'pages/transactions_page.html', context)

def create_transaction(request):
    if request.method == 'POST':
        
        ano = request.GET.get('ano')
        mes = request.GET.get('mes')
        
        form = TransacaoForm(request.POST)
        
        if form.is_valid():
            transacao = form

            if transacao.cleaned_data['tipo'] == "Única" or transacao.cleaned_data['tipo'] == "Fixa":
                transacao.total_parcelas = 1

            elif transacao.cleaned_data['tipo'] == "Parcelada" and transacao.cleaned_data['total_parcelas'] is None:
                return render(request, 'pages/transactions_page.html', {'form': form})
            
            transacao.save(mes=mes, ano=ano)
            return redirect(f"/transactions/?mes={mes}&ano={ano}")
        
        categorias = Categoria.objects.all()
        tipos = Transacao.TipoTransacao.values
        info_data = get_data_navegacao(request)
        data_ref = info_data["data_referencia"]
        transacoes = Transacao.objects.filter(data_lancamento=data_ref)[:5]

        context = {
            **info_data["navegacao"],
            "data_referencia": data_ref,
            "transacoes": transacoes,
            "categorias": categorias,
            "tipos": tipos,
            "form": form,
            "open_modal": True,
            "mes": mes,
            "ano": ano,
        }
        return render(request, "pages/transactions_page.html", context)
                
def categories_page(request):
    return render(request, 'pages/categories_page.html')

    