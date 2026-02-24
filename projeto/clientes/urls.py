from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", ClienteList.as_view(), name="lista-clientes"),
    path("novo/", ClienteCreate.as_view(), name="criar-clientes"),
    path("editar/<int:pk>", ClienteUpdate.as_view(), name="editar-clientes"),
    path("excluir/<int:pk>", ClienteDelete.as_view(), name="excluir-clientes"),
    path("cli/", views.get_clientes, name="get-clientes"),
]