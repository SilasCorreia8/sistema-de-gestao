from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Fornecedor
from .forms import FornecedorForm

from produtos.models import Produto

from django.db import transaction
from django.forms import inlineformset_factory

from rest_framework.decorators import api_view
from .serializers import FornecedorSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
ProdutoFormSet = inlineformset_factory(
    Fornecedor, Produto,
    fields=("nome", "preco", "quantidade", "validade"), # Quais campos mostrar no formset
    extra=1, # Começa mostrando 1 linha em branco para cadastrar produto
    can_delete=True # Permite excluir um produto pela tela do fornecedor
)

class FornecedorCreate(LoginRequiredMixin, CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista_fornecedores")

    # Injeta os formulários de produtos na tela
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['produtos'] = ProdutoFormSet(self.request.POST)
        else:
            data['produtos'] = ProdutoFormSet()
        return data

    # Salva o fornecedor e os produtos de uma vez só
    def form_valid(self, form):
        context = self.get_context_data()
        produtos = context['produtos']
        with transaction.atomic():
            self.object = form.save()
            if produtos.is_valid():
                produtos.instance = self.object
                produtos.save()
        return super().form_valid(form)

class FornecedorList(LoginRequiredMixin, ListView):
    model = Fornecedor
    template_name = "fornecedores/lista.html"
    context_object_name = "fornecedores"

class FornecedorUpdate(LoginRequiredMixin, UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = "fornecedores/form.html"
    success_url = reverse_lazy("lista_fornecedores")

    # Injeta os formulários de produtos na tela (carregando os que já existem)
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['produtos'] = ProdutoFormSet(self.request.POST, instance=self.object)
        else:
            data['produtos'] = ProdutoFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        produtos = context['produtos']
        with transaction.atomic():
            self.object = form.save()
            if produtos.is_valid():
                produtos.instance = self.object
                produtos.save()
        return super().form_valid(form)

class FornecedorDelete(LoginRequiredMixin, DeleteView):
    model = Fornecedor
    template_name = "fornecedores/excluir.html"
    success_url = reverse_lazy("lista_fornecedores")

@api_view(['GET'])
def get_fornecedores(request):

    if request.method == 'GET':
        forecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(forecedores, many=True)
        return Response(serializer.data)
    
    return Response(status.HTTP_404_NOT_FOUND)