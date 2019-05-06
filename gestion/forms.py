from django import forms

from betterforms.multiform import MultiModelForm

from .models import equipo


class equipoModelForm(forms.ModelForm):
    class Meta:
        model = equipo
        fields = '__all__'



