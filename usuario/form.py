from django import forms

class LoginForms(forms.Form):
    nome_login= forms.CharField(
        label='Nome de login',
        required= True,
        max_length= 100,
        widget= forms.TextInput(
            attrs = {
                'placeholder' : "digite seu nome"
            }
        )
    )
    
    senha_login = forms.CharField(
        label='Sua senha',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : "digite sua senha"
            }
        )
    )