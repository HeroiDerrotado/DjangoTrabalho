from django import forms
from usuario.models import Imagem,Usuario
from django.contrib.auth.models import User
from usuario.models import Imagem



class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'legenda', 'categoria', 'descricao', 'foto', 'eh_publicada', 'data_fotografia')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ('titulo', 'imagem')

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Digite seu nome"
            }
        )
    )

    senha_login = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):

    nome_cadastro = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Digite seu nome"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Digite seu email"
            }
        )
    )
    

    senha_cadastro1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Digite sua senha"
            }
        )
    )

    senha_cadastro2 = forms.CharField(
        label='Digite novamente',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Digite sua senha novamente"
            }
        )
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()

            if '' in nome:
                raise forms.ValidationError("Espaços não são permitidos!")
            else:
                return nome

    def clean(self):
        cleaned_data = super().clean()
        senha1 = cleaned_data.get("senha1")
        senha2 = cleaned_data.get("senha2")

        if senha1 != senha2:
            raise forms.ValidationError("As senhas não são iguais")

        return cleaned_data
