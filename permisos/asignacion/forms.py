from django import forms
from asignacion.models import Marcaaccount, Accounts
from django.forms import Widget
from django.utils.html import conditional_escape

from django.utils.safestring import mark_safe

from itertools import chain

#Creacion de FORM para Marcas por cuentas.
class MarcaCampForm(forms.ModelForm):
    class Meta:
        model = Marcaaccount
        fields = [
            'idmarca',
            'idaccountsid',
            'usrcreation',
            'datecreation',
        ]
        labels = {
            'idmarca': 'Marca',
            'idaccountsid': 'Account',
            'usrcreation' : 'Usuer',
            'datecreation': 'Fecha',
        }
        widgets = {
            'idmarca': forms.Select(attrs={'class': 'form-control'}),
            'idaccountsid': forms.CheckboxSelectMultiple(), 
            'usrcreation': forms.TextInput(attrs={'class': 'form-control'}),
            'datecreation': forms.TextInput(attrs={'class': 'form-control'}),
        }

