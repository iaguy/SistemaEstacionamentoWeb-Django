from django.shortcuts import render
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)


def home(request):
    context = {'mensagem': 'Olá Mundo e index'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    data = {'pessoas': pessoas}
    return render(request, 'core/lista_pessoas.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    data = {'veiculos': veiculos}
    return render(request, 'core/lista_veiculos.html', data)


def lista_movrotativos(request):
    mov_rota = MovRotativo.objects.all()
    data = {'mov_rota': mov_rota}
    return render(request, 'core/lista_movrotativos.html', data)


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    data = {'mensalistas': mensalistas}
    return render(request, 'core/lista_mensalista.html', data)


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    data = {'mensalistas': mensalistas}
    return render(request, 'core/lista_mensalista.html', data)


def lista_movmensalista(request):
    mov_mensa = MovMensalista.objects.all()
    data = {'mov_mensa': mov_mensa}
    return render(request, 'core/lista_movmensalista.html', data)

