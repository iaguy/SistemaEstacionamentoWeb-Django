from django.urls import path
from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalista,
    lista_movmensalista,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
)

urlpatterns = [
    path('', home, name='core_home'),

    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_veiculo_novo'),

    path('mov-rota-list/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rota-novo/', movrotativos_novo, name='core_movrotativos_novo'),

    path('mensalistas/', lista_mensalista, name='core_lista_mensalistas'),
    path('mensalistas-novo/', mensalista_novo, name='core_mensalistas_novo'),

    path('mov-mensalistas/', lista_movmensalista, name='core_lista_movmensalistas'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movmensalista_novo'),
]
