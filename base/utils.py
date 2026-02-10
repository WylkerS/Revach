from datetime import date, timedelta

def get_data_navegacao(request):
    hoje = date.today()
    
    try:
        mes_atual = int(request.GET.get('mes', hoje.month))
        ano_atual = int(request.GET.get('ano', hoje.year))
        data_referencia = date(ano_atual, mes_atual, 1)
    except (ValueError, TypeError):
        data_referencia = date(hoje.year, hoje.month, 1)

    # 2. Calcula Mês Anterior (Lógica de virada de ano)
    if data_referencia.month == 1:
        mes_ant = 12
        ano_ant = data_referencia.year - 1
    else:
        mes_ant = data_referencia.month - 1
        ano_ant = data_referencia.year

    # 3. Calcula Próximo Mês
    if data_referencia.month == 12:
        mes_prox = 1
        ano_prox = data_referencia.year + 1
    else:
        mes_prox = data_referencia.month + 1
        ano_prox = data_referencia.year

    return {
        'data_referencia': data_referencia,
        'navegacao': {                      
            'mes_ant': mes_ant,
            'ano_ant': ano_ant,
            'mes_prox': mes_prox,
            'ano_prox': ano_prox,
            'mes_atual': data_referencia.month,
            'ano_atual': data_referencia.year,
        }
    }