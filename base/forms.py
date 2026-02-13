from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
  
    class Meta:
        model = Transacao
        fields = ['nome', 'valor', 'categoria', 'tipo', 'total_parcelas', 'descricao']
        
    def save(self, commit=True, mes=None, ano=None):
        data = self.cleaned_data
        
        if commit:
            instance = Transacao.create(
                mes=int(mes),
                ano=int(ano),
                **data
            )
            return instance
        
        return super().save(commit=False)