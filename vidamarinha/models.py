from django.db import models
from datetime import datetime
# Create your models here.

class Curiosidade(models.Model):

    nome=models.CharField(max_length=100,null=False,blank=False)
    legenda=models.CharField(max_length=100,null=False,blank=False)
    categoria=models.CharField(max_length=100,null=False,blank=False)
    descrisao=models.TextField(null=False,blank=False)
    foto=models.ImageField(upload_to="imagem/%Y/%m/%d/")
    publicada=models.BooleanField(default=False)
    data=models.DateTimeField(default= datetime.now,blank=False)

