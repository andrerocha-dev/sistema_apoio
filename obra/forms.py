from django import forms
from django.forms import ModelForm
from .models import Obra, PorEstado, Implantacao, ObrasAtivas, ObrasDesativadas


class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['nome', 'construtora']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
            'construtora': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' '}),
        }


class PorEstadoForm(ModelForm):
    class Meta:
        model = PorEstado
        fields = ['nome', 'modelo', 'ticket', 'base',
                  'facial', 'webcam', 'ativacao', 'nfe']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'ticket': forms.NumberInput(attrs={'class': 'form-control'}),
            'base': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'facial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'webcam': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ativacao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),

            'nfe': forms.NumberInput(attrs={'class': 'form-control'})
        }


class ImplantacaoForm(ModelForm):
    class Meta:
        model = Implantacao
        fields = ['nome', 'modelo', 'ticket', 'base', 'webcam',
                  'ativacao', 'nfe', 'status', 'informacao']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.Select(attrs={'class': 'form-control'}),
            'ticket': forms.NumberInput(attrs={'class': 'form-control'}),
            'base': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'webcam': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ativacao': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'nfe': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'informacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),

        }


class ObrasAtivasForm(ModelForm):
    class Meta:
        model = ObrasAtivas
        fields = ['nome', 'modelo']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'modelo': forms.Select(attrs={'class': 'form-control'})
        }


class ObrasDesativadasForm(ModelForm):
    class Meta:
        model = ObrasDesativadas
        fields = ['nome', 'desativacao']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-select'}),
            'desativacao': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})
        }
