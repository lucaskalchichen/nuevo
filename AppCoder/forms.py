from django import forms

class FormUsuario(forms.Form):
    nombre =forms.CharField(max_length=30)
    apellido =forms.CharField(max_length=30)
    dni = forms.IntegerField()
    user =forms.CharField(max_length=16)


class FormAutomotor(forms.Form):
    user =forms.CharField(max_length=16)
    nchasis =forms.CharField(max_length=10)
    nmotor =forms.CharField(max_length=10)
    npatente =forms.CharField(max_length=7)
    ano =forms.IntegerField()