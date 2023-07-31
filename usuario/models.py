from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone

class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Cadastro(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    email = models.EmailField()
    senha = models.CharField(max_length=125,null=True,blank=True)

    def __str__(self):
        return self.usuario.username
