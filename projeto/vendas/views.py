from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Venda
from .forms import VendaForm

from rest_framework.decorators import api_view
from .serializers import VendaSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class VendaCreate(LoginRequiredMixin, CreateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/form.html"
    success_url = reverse_lazy("lista_vendas")

class VendaList(LoginRequiredMixin, ListView):
    model = Venda
    template_name = "vendas/lista.html"
    context_object_name = "vendas"

class VendaUpdate(LoginRequiredMixin, UpdateView):
    model = Venda
    form_class = VendaForm
    template_name = "vendas/form.html"
    success_url = reverse_lazy("lista_vendas")

class VendaDelete(LoginRequiredMixin, DeleteView):
    model = Venda
    template_name = "vendas/excluir.html"
    success_url = reverse_lazy("lista_vendas")

@api_view(['GET'])
def get_vendas(request):

    if request.method == 'GET': 
       vendas = Venda.objects.all()
       serializer = VendaSerializer(vendas, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)
    