from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

# Create your views here.
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista-clientes")

class ClienteList(ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm 
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista-clientes")

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "clientes/excluir.html"
    success_url = reverse_lazy("lista-clientes")