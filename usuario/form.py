from django import forms
from usuario.models import Usuario


class ImagemForm(forms.Form):
    class Meta:
        model = Usuario
        exclude = ['eh_publicada',]
        
        widgets = {
            
            'nome' :forms.TextInput(),
            'legenda' :forms.TextInput(),
            'categoria' :forms.Select(),
            'descriçao' :forms.Textarea(),
            'foto' :forms.FileInput(),
            'data_fotografia' :forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                   'type':'date',
                }
                
            ),
            'usuario':forms.Select(),
        }
        labels = {
            
            'descricao':'DESCRICAO',
            'data_fotografia':'Data da Foto',
            'usuario':'usuário'
        }

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': "digite seu nome"
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

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()

            if '' in nome:
                raise forms.ValidationError("Espaços não são permitidos!")
            else:
                return nome

    def clean_senha(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")

        if senha1 == senha2:
            raise forms.ValidationError("As senhas não são iguais")
        else:
            return senha2
