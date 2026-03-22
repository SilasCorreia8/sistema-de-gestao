from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Produto
from .forms import ProdutoForm

from rest_framework.decorators import api_view
from .serializers import ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse

# Create your views here.
class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    form_class = ProdutoForm
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista_produtos")

class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = "produtos/lista.html"
    context_object_name = "produtos"

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm 
    template_name = "produtos/form.html"
    success_url = reverse_lazy("lista_produtos")

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = "produtos/excluir.html"
    success_url = reverse_lazy("lista_produtos")

@api_view(['GET'])
def get_produtos(request):

    if request.method == 'GET': 
       produtos = Produto.objects.all()
       serializer = ProdutoSerializer(produtos, many=True)
       return Response(serializer.data)

    return Response(status.HTTP_404_NOT_FOUND)

def produtos_por_fornecedor(request, fornecedor_id):
    # Busca apenas os produtos que têm a chave estrangeira igual ao fornecedor selecionado
    produtos = Produto.objects.filter(fornecedor_id=fornecedor_id).values('id', 'nome')
    # Converte para uma lista e retorna como JSON
    return JsonResponse(list(produtos), safe=False)