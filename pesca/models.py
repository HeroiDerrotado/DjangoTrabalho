from django.db import models
from django.contrib.auth.models import User


OPCOES_CATEGORIA = [
    ('CATEGORIA','categoria'),
    ('CAT','cat')
    ]


class Pesca(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(
        max_length=100, choices=OPCOES_CATEGORIA, default='CATEGORIA')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/', blank=True)
    publicada = models.BooleanField(default=False)
  

    def __str__(self):
        return self.nome
