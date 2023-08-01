from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Cadastro(models.Model):

    nome = models.CharField(max_length=125, blank=False, null=False)
    email = models.EmailField(max_length=125, blank=False, null=False)
    senha = models.CharField(max_length=125, blank=False, null=False)


class Usuario(models.Model):

    OPCOES_CATEGORIA = [
        ("PESSOA", "pessoa"),
        ("CONSOLE", "console")
    ]

    OPCAO_USUARIO = [
        ("USUARIO", "usuario"),
    ]

    nome = models.CharField(max_length=125, blank=False, null=False)
    legenda = models.CharField(max_length=125, blank=False, null=False)
    categoria = models.CharField(
        max_length=125, choices=OPCOES_CATEGORIA, default='OPCOES_CATEGORIA')
    descrisao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%n/%d/', blank=True)
    eh_publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    Usuario = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
