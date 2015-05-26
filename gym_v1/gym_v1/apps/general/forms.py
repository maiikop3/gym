from django import forms
from gym_v1.apps.general.models import *


class addProductForm(forms.ModelForm):
	class Meta:
		model = producto
		exclude = {'status',}


"""
class addProductForm(forms.Form):
	nombre 		= forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.TextInput())
	imagen		= forms.ImageField(required=False)
	precio		= forms.DecimalField(required=True)
	stock		= forms.IntegerField(required=False)

	def clean(self):
		return self.cleaned_data #para que no se puedan meter datos vacios
"""