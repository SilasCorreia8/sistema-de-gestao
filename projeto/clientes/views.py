from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm

from rest_framework.decorators import api_view
from .serializers import ClienteSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista_clientes")

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "clientes/lista.html"
    context_object_name = "clientes"

class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm 
    template_name = "clientes/form.html"
    success_url = reverse_lazy("lista_clientes")

class ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "clientes/excluir.html"
    success_url = reverse_lazy("lista_clientes")

@api_view(['GET'])
def get_clientes(request):

    if request.method == 'GET': 
       clientes = Cliente.objects.all()
       serializer = ClienteSerializer(clientes, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)