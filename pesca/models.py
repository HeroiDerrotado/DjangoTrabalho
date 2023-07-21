from django.db import models
from datetime import datetime

# Create your models here.

class Imagem(models.Model):

    OPCOES_CATAEGORIA = [
        ('MARINHO','marinho'),
        ('MAR','mar'),
    ]
    
    nome = models.CharField(max_length=100,null = False, blank = False )
    legenda = models.CharField(max_length=100,null =False,blank=False)
    categoria = models.CharField(max_length=100, choices= OPCOES_CATAEGORIA, default= "")
    descricao = models.TextField(null=False, blank=False)
    descrisao = models.TextField(null = False,blank= False)
    foto = models.ImageField(upload_to='imagem/%Y/%m/%d/',blank=True)
    publicada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.now, blank=False)


    def __str__(self):
        return self.nome