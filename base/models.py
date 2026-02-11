from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from datetime import date
from dateutil import relativedelta


class Categoria(models.Model):

    id = models.CharField(
        primary_key=True, max_length=36, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=50)
    entrada = models.BooleanField(default=False)
    cor = models.CharField(max_length=7, default="#FFFFFF")

    def __str__(self):
        return self.nome


class Transacao(models.Model):
    class TipoTransacao(models.TextChoices):
        UNICA = "Única", _("Única")
        FIXA = "Fixa", _("Fixa")
        PARCELADA = "Parcelada", _("Parcelada")

    class Situacao(models.TextChoices):
        PAGA = "PAGA", _("Paga")
        PENDENTE = "PENDENTE", _("Pendente")
        ATRASADA = "ATRASADA", _("Atrasada")

    id = models.CharField(
        primary_key=True, max_length=36, default=uuid.uuid4, editable=False
    )
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=100, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)

    valor = models.DecimalField(max_digits=10, decimal_places=2)
    
    data_vencimento = models.DateField("Data de Vencimento")
    data_lancamento = models.DateField("Data de Lançamento")

    tipo = models.CharField(
        max_length=10, choices=TipoTransacao.choices, default=TipoTransacao.UNICA
    )
    situacao = models.CharField(
        max_length=10, choices=Situacao.choices, default=Situacao.PENDENTE
    )

    parcela_atual = models.PositiveIntegerField(default=1, blank=True, null=True)
    total_parcelas = models.PositiveIntegerField(default=1, blank=True, null=True)

    identificador_transacao = models.UUIDField(default=uuid.uuid4, editable=False)
    
    data_criacao = models.DateField("Data de Criação")

    class Meta:
        ordering = ["-data_vencimento"]

    def __str__(self):
        return f"{self.nome} - {self.valor} - {self.data_vencimento}"

    @property
    def display_parcela(self):
        if self.tipo == self.TipoTransacao.PARCELADA:
            return f"{self.parcela_atual}/{self.total_parcelas}"
        return self.TipoTransacao(self.tipo).label

    @classmethod
    def create(cls, mes, ano, **kwargs):
        instance = cls(**kwargs)
        instance.data_lancamento = date(ano, mes, 1)
        instance.data_vencimento = date(ano, mes, 1)
        instance.data_criacao = date(ano, mes, 1)
        instance.parcela_atual = 1
        instance.identificador_transacao = uuid.uuid4()
        instance.save()
        
        if not instance.tipo in cls.TipoTransacao.UNICA:
            
            if instance.tipo == cls.TipoTransacao.PARCELADA:
                qtd = instance.total_parcelas
                
            elif instance.tipo == cls.TipoTransacao.FIXA:
                qtd = 12
                
            for parcela_num in range(2, qtd + 1):
                parcela = cls(
                    nome=instance.nome,
                    descricao=instance.descricao,
                    categoria=instance.categoria,
                    valor=instance.valor,
                    data_lancamento=instance.data_lancamento + relativedelta.relativedelta(months=parcela_num - 1),
                    data_vencimento=instance.data_vencimento + relativedelta.relativedelta(months=parcela_num - 1),
                    data_criacao=instance.data_criacao,
                    tipo=instance.tipo,
                    situacao=instance.situacao,
                    parcela_atual=parcela_num,
                    total_parcelas=instance.total_parcelas,
                    identificador_transacao=instance.identificador_transacao
                )
                
                parcela.save()
                
        return instance
