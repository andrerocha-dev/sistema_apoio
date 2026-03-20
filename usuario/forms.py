from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'login']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ' '}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")
        return email

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError(
                "O nome deve ter pelo menos 3 caracteres.")
        return nome

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if login == Usuario.objects.filter(login=login).exists():
            raise forms.ValidationError("Este login já está em uso.")
        return login

    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        if len(senha) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return senha


class UsuarioUpdate(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'login']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ' '}),
        }

        def clean_senha(self):
            senha = self.cleaned_data.get('senha')
            if len(senha) < 8:
                raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres.")
            return senha

        def clean_nome(self):
            nome = self.cleaned_data.get('nome')
            if len(nome) < 3:
                raise forms.ValidationError(
                    "O nome deve ter pelo menos 3 caracteres.")
            return nome

    
