from django.db import models
from datetime import datetime
from vidamarinha.models import Curiosidade
# from vidamarinha.models import  Curiosidade
# Create your models here.


class EspecieGeral(models.Model):
    OPCOES_CATEGORIA = [
        ('MARINHO', 'marinho'),
        ('TERRA', 'terra')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.CharField(max_length=100, null=False, blank=False)
    descrisao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/')
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome
