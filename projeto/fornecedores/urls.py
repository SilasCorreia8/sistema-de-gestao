from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", FornecedorList.as_view(), name="lista-fornecedores"),
    path("novo/", FornecedorCreate.as_view(), name="criar-fornecedores"),
    path("editar/<int:pk>", FornecedorUpdate.as_view(), name="editar-fornecedores"),
    path("excluir/<int:pk>", FornecedorDelete.as_view(), name="excluir-fornecedores"),
    path("cli/", views.get_fornecedores, name="get-fornecedores"),
]