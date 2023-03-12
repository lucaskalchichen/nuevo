from django import forms
from AppCoder.models import Usuario,Automotor

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class FormAutomotor(forms.ModelForm):
    class Meta:
        model = Automotor
        fields = '__all__'

