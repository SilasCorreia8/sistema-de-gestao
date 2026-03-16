from django.forms import ModelForm, TextInput, EmailInput
from .models import Fornecedor

class FornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome", "email", "telefone", "cidade", "estado", "cnpj"]

        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Nome da Empresa / Fornecedor'}),
            'cnpj': TextInput(attrs={'placeholder': 'CNPJ'}),
            'email': EmailInput(attrs={'placeholder': 'E-mail de Contato'}),
            'telefone': TextInput(attrs={'placeholder': 'Telefone'}),
            'cidade': TextInput(attrs={'placeholder': 'Cidade'}),
            'estado': TextInput(attrs={'placeholder': 'Estado'}),
        }