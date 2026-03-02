from django.urls import path
from .views import *

urlpatterns = [
    path("", FornecedorList.as_view(), name="lista-fornecedores"),
    path("novo/", FornecedorCreate.as_view(), name="criar-fornecedores"),
    path("editar/<int:pk>", FornecedorUpdate.as_view(), name="editar-fornecedores"),
    path("excluir/<int:pk>", FornecedorDelete.as_view(), name="excluir-fornecedores"),
    #path("cli/", views.get_clientes, name="get-fornecedores"),
]