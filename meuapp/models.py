from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f'{self.nome} - {self.cpf}'


class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    descricao = models.TextField(blank=True, null=True)
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.nome} ({self.modelo})'
