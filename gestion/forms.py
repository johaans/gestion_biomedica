from django import forms

from betterforms.multiform import MultiModelForm

from .models import equipo, cronograma


class equipoModelForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = '__all__'

class cronogramaModelForm(forms.ModelForm):
    class Meta:
        model = cronograma
        fields = ['tipo', 'fecha']


class equipocronogramaModelForm(MultiModelForm):
    form_classes = {
        'equipo': equipoModelForm,
        'cronograma': cronogramaModelForm,
    }
