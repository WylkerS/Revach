from django.shortcuts import render, get_object_or_404
from .models import Transacao
from django.http import HttpResponse
from .utils import get_data_navegacao
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_transaction(request, pk):
    
    transacao = get_object_or_404(Transacao, id=pk)
    transacoes_parcelas = Transacao.objects.filter(identificador_transacao=transacao.identificador_transacao)
    
    if request.method == 'POST':
        try:
            for t in transacoes_parcelas:
                t.delete()
        except Exception as e:
            return HttpResponse(f"Erro ao deletar a transação: {str(e)}", status=500)
        
        info_data = get_data_navegacao(request)
        data_ref = info_data["data_referencia"]
        transacoes = Transacao.objects.filter(data_lancamento=data_ref)[:5]
        
        lista = render(request, "partials/htmx_components/list_transactions.html", {"transacoes": transacoes}).content.decode('utf-8')

        fechar_modal = '<div id="modal_delete" hx-swap-oob="innerHTML"></div>'
        
        return HttpResponse(lista + fechar_modal)


    return render(request, 'partials/htmx_components/modal_confirm_delete_transaction.html', {'transacao': transacao})