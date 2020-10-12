from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
	
	class Meta:
		model = Customer
		fields = ('firstname', 'lastname')
		
class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('category','brand')
