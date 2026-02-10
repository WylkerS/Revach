from django import forms
import datetime

class SelecaoMesForm(forms.Form):
    OPCOES_DATA = []
    ano_atual = datetime.date.today().year
    
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    for ano in range(ano_atual - 1, ano_atual + 2):
        for i, mes_nome in enumerate(meses, 1):
            valor = f"{ano}-{i:02d}-01"
            rotulo = f"{mes_nome}/{ano}"
            OPCOES_DATA.append((valor, rotulo))

    periodo = forms.ChoiceField(
        choices=OPCOES_DATA, 
        widget=forms.Select(attrs={'class': 'border border-gray-300 rounded p-2'})
    )