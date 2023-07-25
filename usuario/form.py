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
                'placeholder' : "Digite sua senha"
            }
        )
    )

class CadastroForms(forms.Form):

    nome_completo = forms.CharField(
        label = 'Seu cadastro',
        required = True,
        max_length = 100,
        widget=forms.TextInput(
            attrs={
                'placeholder' : "Digite seu nome"
            }
        )
    )

    email = forms.EmailField(
        label = "email",
        required = True,
        max_length = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder' : "Digite seu nome"
            }
        )
    )

    senha_cadastro1 = forms.CharField(
        label='senha1',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : "Digite sua senha"
            }
        )
    )


    senha_cadastro2 = forms.CharField(
        label='senha2',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs = {
                'placeholder' : "Digite sua senha novamente"
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome=nome.strip()

            if ' ' in nome:
                raise forms.ValidationError("Espaços não são permitidos!")
            else:
                return nome



