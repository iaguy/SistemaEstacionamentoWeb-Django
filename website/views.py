from django.shortcuts import render
from .models import (
    Contato
)


def home(request):
    return render(request, 'website/index.html')


def contato(request):
    mensagem = ''
    if request.method == "POST":
        try:
            contato = {}
            contato['nome'] = request.POST.get('nome')
            contato['sobrenome'] = request.POST.get('sobrenome')
            contato['email'] = request.POST.get('email')
            contato['endereco'] = request.POST.get('endereco')
            contato['faleconosco'] = request.POST.get('faleconosco')
            contato['cidade'] = request.POST.get('cidade')
            contato['estado'] = request.POST.get('estado')
            contato['cep'] = request.POST.get('cep')


            Contato.objects.create(**contato)
        except Exception as e:
            pass
        else:
            mensagem = 'Contato Realizado com Sucesso'
    return render(request, 'website/contato.html', {'mensagem': mensagem})


def planos(request):
    return render(request, 'website/planos.html')


def sobre(request):
    return render(request, 'website/sobre.html')


def servicos(request):
    return render(request, 'website/servicos.html')