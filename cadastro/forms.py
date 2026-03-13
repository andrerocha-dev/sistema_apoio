from django import forms
from .models import Faltas, Pessoa, Prestador, CustoParceiros, Ferias, Atrasos


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'data_admissao', 'funcao',
                  'endereco', 'documento', 'prestador']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'data_admissao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control',
                       'type': 'date', 'placeholder': ' '}
            ),
            'funcao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'prestador': forms.Select(attrs={'class': 'form-select'}),
        }


class FaltasForm(forms.ModelForm):
    class Meta:
        model = Faltas
        fields = ['nome', 'data_falta', 'justificada']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'data_falta': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'justificada': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
        }


class AtrasosForm(forms.ModelForm):
    class Meta:
        model = Atrasos
        fields = ['nome', 'data_atraso', 'horario', 'justificado']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'data_atraso': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'horario': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'justificado': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}
            ),
        }


class FeriasForm(forms.ModelForm):
    class Meta:
        model = Ferias
        fields = ['nome', 'data_admissao', 'data_limite', 'periodo_aquisitivo',
                  'fim_aquisitivo', 'limite_gozo', 'inicio_gozo', 'fim_gozo']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'data_admissao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'data_limite': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'periodo_aquisitivo': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'fim_aquisitivo': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'limite_gozo': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'inicio_gozo': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'fim_gozo': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),

        }


class CustoParceirosForm(forms.ModelForm):
    class Meta:
        model = CustoParceiros
        fields = '__all__'
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'hora_tecnica': forms.NumberInput(attrs={'class': 'form-control'}),
            'hora_adcional': forms.NumberInput(attrs={'class': 'form-control'}),
            'Remanejamento': forms.NumberInput(attrs={'class': 'form-control'}),
            'desmobilizacao': forms.NumberInput(attrs={'class': 'form-control'}),
            'instalacao_1_catraca': forms.NumberInput(attrs={'class': 'form-control'}),
            'instalacao_2_catracas': forms.NumberInput(attrs={'class': 'form-control'}),
        }
