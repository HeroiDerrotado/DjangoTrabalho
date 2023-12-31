from django.db import models
from datetime import datetime


# Create your models here.

from django import forms

class Busca(models.Model):
    buscando = forms.CharField(max_length=100, required=False)




class Menu(models.Model):

    OPCOES_CATEGORIA = [
        ('CATEGORIA','categoria'),
        ('CAT','cat'),
    ]
    nome = models.CharField(max_length=100,null = False, blank = False )
    legenda = models.CharField(max_length=100,null =False,blank=False)
    categoria = models.CharField(max_length=100, choices= OPCOES_CATEGORIA, default= "")
    descricao = models.TextField(null=False, blank=False)
    descrisao = models.TextField(null = False,blank= False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/',blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)
   
    
    def __str__(self):
        return self.nome