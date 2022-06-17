from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import io
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

@login_required
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = {'pessoas': pessoas, 'form': form}
    return render(request, 'core/lista_pessoas.html', data)

@login_required
def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_pessoas')

@login_required
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

@login_required
def pessoa_delete(request, id):
    pessoa = Pessoa.objects.get(id=id)
    data = {'obj': pessoa}
    if request.method == 'POST':
        pessoa.delete()
        return redirect('core_lista_pessoas')
    else:
        return render(request, 'core/delete_confirm.html', data)

@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = {'veiculos': veiculos, 'form': form}
    return render(request, 'core/lista_veiculos.html', data)

@login_required
def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_veiculos')

@login_required
def veiculo_update(request, id):
    data = {}
    veiculo = Veiculo.objects.get(id=id)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    data['veiculo'] = veiculo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/update_veiculo.html', data)

@login_required
def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)
    data = {'obj': veiculo}
    if request.method == 'POST':
        veiculo.delete()
        return redirect('core_lista_veiculos')
    else:
        return render(request, 'core/delete_confirm.html', data)

@login_required
def lista_movrotativos(request):
    mov_rota = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {'mov_rota': mov_rota, 'form': form}
    return render(request, 'core/lista_movrotativos.html', data)

@login_required
def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movrotativos')

@login_required
def movrotativo_update(request, id):
    data = {}
    mov_rotativo = MovRotativo.objects.get(id=id)
    form = MovRotativoForm(request.POST or None, instance=mov_rotativo)
    data['mov_rotativo'] = mov_rotativo
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/update_movrotativo.html', data)

@login_required
def movrotativo_delete(request, id):
    mov_rotativo = MovRotativo.objects.get(id=id)
    data = {'obj': mov_rotativo}
    if request.method == 'POST':
        mov_rotativo.delete()
        return redirect('core_lista_movrotativos')
    else:
        return render(request, 'core/delete_confirm.html', data)

@login_required
def lista_mensalista(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm
    data = {'mensalistas': mensalistas, 'form': form}
    return render(request, 'core/lista_mensalista.html', data)

@login_required
def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_mensalistas')

@login_required
def mensalista_update(request, id):
    data = {}
    mensalistas = Mensalista.objects.get(id=id)
    form = MensalistaForm(request.POST or None, instance=mensalistas)
    data['mensalistas'] = mensalistas
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/update_mensalistas.html', data)

@login_required
def mensalista_delete(request, id):
    mensalistas = Mensalista.objects.get(id=id)
    data = {'obj': mensalistas}
    if request.method == 'POST':
        mensalistas.delete()
        return redirect('core_lista_mensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)

@login_required
def lista_movmensalista(request):
    mov_mensalista = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = {'mov_mensalista': mov_mensalista, 'form': form}
    return render(request, 'core/lista_movmensalista.html', data)

@login_required
def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('core_lista_movmensalistas')

@login_required
def movmensalista_update(request, id):
    data = {}
    mov_mensalistas = MovMensalista.objects.get(id=id)
    form = MovMensalistaForm(request.POST or None, instance=mov_mensalistas)
    data['mov_mensalistas'] = mov_mensalistas
    data['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/update_movmensalistas.html', data)

@login_required
def movmensal_delete(request, id):
    mov_mensalistas = MovMensalista.objects.get(id=id)
    data = {'obj': mov_mensalistas}
    if request.method == 'POST':
        mov_mensalistas.delete()
        return redirect('core_lista_movmensalistas')
    else:
        return render(request, 'core/delete_confirm.html', data)


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)


class Pdf(View):

    def get(self, request):
        veiculos = Veiculo.objects.all()
        params = {
            'veiculos': veiculos,
            'request': request,
        }
        return Render.render('core/relatorio.html', params, 'Relatorio_Veiculos')