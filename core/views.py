from django.shortcuts import render,redirect
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista,
)
from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm,
)


def home(request):
    context = {'mensagem': 'Olá Mundo e index'}
    return render(request, 'core/index.html', context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_pessoas')


def pessoa_update(request, id):
    data = {}
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)
    data['pessoa'] = pessoa
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_pessoas')
        else:
            return render(request, 'core/update_pessoa.html', data)


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_veiculos')


def lista_movrotativos(request):
    mov_rota = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rota': mov_rota, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movrotativos')


def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalista.html', data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_mensalistas')



def lista_movmensalista(request):
    mov_mensa = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensa': mov_mensa, 'form': form}
    return render(request, 'core/lista_movmensalista.html', data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movmensalistas')

