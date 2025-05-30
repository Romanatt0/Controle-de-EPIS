
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Colaborador
from .models import Equipamento



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
    return render(request, 'sucesso.html')  # Uma página simples de sucesso

def cadastrar_equipamento(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        tipo = request.POST.get('tipo')
        modelo = request.POST.get('modelo')
        descricao = request.POST.get('descricao')
        quantidade = request.POST.get('quantidade')

        Equipamento.objects.create(
            nome=nome,
            tipo=tipo,
            modelo=modelo,
            descricao=descricao,
            quantidade=quantidade
        )

        return redirect('sucesso_equipamento')  # <- Aqui está a mudança

    return render(request, 'cadastrar_equipamento.html')

def sucesso_equipamento(request):
    return render(request, 'sucesso_equipamento.html')

    