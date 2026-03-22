from django.forms import ModelForm
from .models import Venda
from django import forms

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ["produto", "cliente", "preco", "quantidade", "data_venda"]
        widgets = {
            # Exibe dd/mm/aaaa e aceita esse formato
            'data_venda': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_venda'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']

    def clean(self):
        # Pega os dados que digitados
        cleaned_data = super().clean()
        produto = cleaned_data.get("produto")
        quantidade_solicitada = cleaned_data.get("quantidade")

        # Se o usuário preencheu o produto e a quantidade corretamente
        if produto and quantidade_solicitada:
            estoque_disponivel = produto.quantidade

            # Se for uma edição (a venda já tem ID), o produto continuar sendo o mesmo,
            # nós precisamos somar a quantidade da venda antiga de volta ao estoque
            # para saber o real valor disponível para essa edição.
            if self.instance.pk and self.instance.produto == produto:
                estoque_disponivel += self.instance.quantidade

            # A Validação: A quantidade pedida é maior que a disponível?
            if quantidade_solicitada > estoque_disponivel:
                self.add_error(
                    'quantidade', 
                    f"Estoque insuficiente! O produto '{produto.nome}' tem apenas {estoque_disponivel} unidades disponíveis."
                )

        return cleaned_data