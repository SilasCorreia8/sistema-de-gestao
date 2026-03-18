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