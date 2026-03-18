from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("", VendaList.as_view(), name="lista_vendas"),
    path("nova/", VendaCreate.as_view(), name="criar_vendas"),
    path("editar/<int:pk>/", VendaUpdate.as_view(), name="editar_vendas"),
    path("excluir/<int:pk>/", VendaDelete.as_view(), name="excluir_vendas"),
    path("cli/", views.get_vendas, name="get_vendas"),
]