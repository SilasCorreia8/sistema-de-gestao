from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm

# Create your views here.
class ProdutoCreate(CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista-produtos")

class ProdutoList(ListView):
    model = Produto
    template_name = "produtos/lista.html"
    context_object_name = "produtos"

class ProdutoUpdate(UpdateView):
    model = Produto
    form_class = ProdutoForm 
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista-produtos")

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = "produtos/excluir.html"
    success_url = reverse_lazy("lista-produtos")