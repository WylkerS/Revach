from django.shortcuts import render
from .models import Transacao
from .utils import get_data_navegacao
from .forms import TransacaoForm

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
    
    if request.method == 'POST':
        print("Criando")
        
        form = TransacaoForm(request.POST)
        mes = request.GET.get('mes')
        ano = request.GET.get('ano')
        print(f"Ano: {ano}, Mês: {mes}")

        if form.is_valid():
            if form.cleaned_data['tipo'] == 'Fixa' or form.cleaned_data['tipo'] == "Única":
                form.cleaned_data['total_parcelas'] = 1
                print('Transação do tipo Fixa ou Única, definindo total_parcelas como 1.')
            else:
                print('Transação do tipo Parcelada')
                if not form.cleaned_data['total_parcelas']:
                     form.add_error('total_parcelas', 'Este campo é obrigatório para transações parceladas.')
                     print('Erro: total_parcelas é obrigatório para transações parceladas.')
                
            form.save(mes=mes, ano=ano)
        else:
            print("Erro ao salvar transação:", form.errors)

        
    info_data = get_data_navegacao(request)
    data_ref = info_data['data_referencia']
    
    transacoes = Transacao.objects.all()

    context = {
        **info_data['navegacao'],
        'data_referencia': data_ref,
        'transacoes': transacoes,
    }
    
    return render(request, 'pages/transactions_page.html', context)

def categories_page(request):
    return render(request, 'pages/categories_page.html')

    