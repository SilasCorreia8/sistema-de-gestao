from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fornecedor
from .forms import FornecedorForm

# Create your views here.
class FornecedorCreate(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista-fornecedores")

class FornecedorList(ListView):
    model = Fornecedor
    template_name = "fornecedores/lista.html"
    context_object_name = "fornecedores"

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista-fornecedores")

class FornecedorDelete(DeleteView):
    model = Fornecedor
    template_name = "fornecedores/excluir.html"
    success_url = reverse_lazy("lista-fornecedores")