from django.forms import ModelForm
from .models import Compra
from django import forms

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ["fornecedor", "produto", "preco", "quantidade", "data_compra"]
        widgets = {
            # Exibe dd/mm/aaaa e aceita esse formato
            'data_compra': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_compra'].input_formats = ['%d/%m/%Y', '%Y-%m-%d']