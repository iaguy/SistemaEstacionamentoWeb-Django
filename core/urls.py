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
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensal_delete,
    Pdf,
    ExportarParaCSV,
)

urlpatterns = [
    path('', home, name='core_home'),

    path('pessoas/', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo/', pessoa_novo, name='core_pessoa_novo'),
    path('pessoa-update/<int:id>/', pessoa_update, name='core_pessoa_update'),
    path('pessoa-delete/<int:id>/', pessoa_delete, name='core_pessoa_delete'),

    path('veiculos/', lista_veiculos, name='core_lista_veiculos'),
    path('veiculos-novo/', veiculo_novo, name='core_veiculo_novo'),
    path('veiculo-update/<int:id>/', veiculo_update, name='core_veiculo_update'),
    path('veiculo-delete/<int:id>/', veiculo_delete, name='core_veiculo_delete'),

    path('mov-rota-list/', lista_movrotativos, name='core_lista_movrotativos'),
    path('mov-rota-novo/', movrotativos_novo, name='core_movrotativos_novo'),
    path('mov-rota-update/<int:id>/', movrotativo_update, name='core_movrotativos_update'),
    path('mov-rota-delete/<int:id>/', movrotativo_delete, name='core_movrotativos_delete'),

    path('mensalistas/', lista_mensalista, name='core_lista_mensalistas'),
    path('mensalistas-novo/', mensalista_novo, name='core_mensalistas_novo'),
    path('mensalistas-update/<int:id>/', mensalista_update, name='core_mensalistas_update'),
    path('mensalistas-delete/<int:id>/', mensalista_delete, name='core_mensalistas_delete'),

    path('mov-mensalistas/', lista_movmensalista, name='core_lista_movmensalistas'),
    path('mov-mensal-novo/', movmensalista_novo, name='core_movmensalista_novo'),
    path('mov-mensal-update/<int:id>/', movmensalista_update, name='core_movmensalistas_update'),
    path('mov-mensal-delete/<int:id>/', movmensal_delete, name='core_movmensal_delete'),

    path('relatorio/', Pdf.as_view(), name='relatorio_pdf'),
    path('relatorio-csv/', ExportarParaCSV.as_view(), name='relatorio_csv'),
]
