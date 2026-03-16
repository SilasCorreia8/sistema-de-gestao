from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Compra
from .forms import CompraForm

# Create your views here.
class CompraCreate(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = "compras/form.html"
    success_url = reverse_lazy("lista_compras")

class CompraList(ListView):
    model = Compra
    template_name = "compras/lista.html"
    context_object_name = "compras"


class CompraUpdate(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = "compras/form.html"
    success_url = reverse_lazy("lista_compras")

class CompraDelete(DeleteView):
    model = Compra
    template_name = "compras/excluir.html"
    success_url = reverse_lazy("lista_compras")