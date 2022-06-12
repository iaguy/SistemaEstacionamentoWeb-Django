from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista,
)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('mov-rota-list/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas/', lista_mensalista, name='core_lista_mensalistas'),
    path('mov-mensalistas/', lista_movmensalista, name='core_lista_movmensalistas'),
]
