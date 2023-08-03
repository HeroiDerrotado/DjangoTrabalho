from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Usuario(models.Model):
    OPCOES_CATEGORIA = [
        ("PESSOA", "pessoa"),
        ("CONSOLE", "console")
    ]

    other_field1 = models.CharField(max_length=100, default='USUARIO')
    other_field2 = models.CharField(max_length=100, default='USUARIO')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1, related_name='usuario_profile')
    nome = models.CharField(max_length=125, blank=False, null=False)
    legenda = models.CharField(max_length=125, blank=False, null=False)
    categoria = models.CharField(
        max_length=125, choices=OPCOES_CATEGORIA, default='PESSOA'
    )
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%n/%d/', blank=True)
    eh_publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome

class Imagem(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    
    
