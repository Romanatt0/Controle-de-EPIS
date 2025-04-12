
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Colaborador


# Create your views here.

def home(request):
    return render(request, "index.html")

def menu(request):
    return render(request, "menu.html")

def colaborador(request):
    return render(request, "colaborador.html")

def cadastrar_colaborador(request):
    if request.method == 'POST':
        # Recebe os dados do formulário
        nome = request.POST.get('usuario')
        cpf = request.POST.get('senha')

        # Validação simples
        if not nome or not cpf:
            return HttpResponse("Nome e CPF são obrigatórios.", status=400)

        # Verificar se o CPF já está cadastrado
        if Colaborador.objects.filter(cpf=cpf).exists():
            return HttpResponse("CPF já cadastrado.", status=400)

        # Criar novo colaborador
        colaborador = Colaborador(nome=nome, cpf=cpf)
        colaborador.save()

        # Redireciona para uma página de sucesso ou página inicial
        return redirect('sucesso')  # Substitua 'sucesso' pelo nome de sua URL de sucesso

    return render(request, 'cadastrar_colaborador.html')

def sucesso(request):
    return render(request, 'sucesso.html')  # Uma página simples de suce