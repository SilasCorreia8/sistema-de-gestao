from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Compra
from .forms import CompraForm

from rest_framework.decorators import api_view
from .serializers import CompraSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CompraCreate(LoginRequiredMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = "compras/form.html"
    success_url = reverse_lazy("lista_compras")

class CompraList(LoginRequiredMixin, ListView):
    model = Compra
    template_name = "compras/lista.html"
    context_object_name = "compras"


class CompraUpdate(LoginRequiredMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = "compras/form.html"
    success_url = reverse_lazy("lista_compras")

class CompraDelete(LoginRequiredMixin, DeleteView):
    model = Compra
    template_name = "compras/excluir.html"
    success_url = reverse_lazy("lista_compras")

@api_view(['GET'])
def get_compras(request):

    if request.method == 'GET': 
       compras = Compra.objects.all()
       serializer = CompraSerializer(compras, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)