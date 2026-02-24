from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", ProdutoList.as_view(), name="lista-produtos"),
    path("novo/", ProdutoCreate.as_view(), name="criar-produtos"),
    path("editar/<int:pk>", ProdutoUpdate.as_view(), name="editar-produtos"),
    path("excluir/<int:pk>", ProdutoDelete.as_view(), name="excluir-produtos"),
    path("cli/", views.get_produtos, name="get-produtos"),
]