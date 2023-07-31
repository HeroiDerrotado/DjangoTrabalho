from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):

    nome = models.CharField(max_length=100, null=True, blank=True)
    senha = models.CharField(max_length=100, null=True, blank=False)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)


class Cadastro(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    senha = models.CharField(max_length=100, null=True, blank=False)
