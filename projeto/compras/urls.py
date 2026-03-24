from django.urls import path
from .views import CompraList, CompraCreate, CompraUpdate, CompraDelete
from . import views


urlpatterns = [
    path("", CompraList.as_view(), name="lista_compras"),
    path("novo/", CompraCreate.as_view(), name="criar_compras"),
    path("editar/<int:pk>/", CompraUpdate.as_view(), name="editar_compras"),
    path("excluir/<int:pk>/", CompraDelete.as_view(), name="excluir_compras"),
    path("cli/", views.get_compras, name="get_clientes"),
]