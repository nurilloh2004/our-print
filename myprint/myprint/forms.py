from dataclasses import fields
from django import forms
from django.forms import ModelForm

from .models import *

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer

		fields = [
			'id_name_order',
			'client',
			'client_phone_number',
            'manager_name',
            'date_order',
            'ready_product_date_order',
		]

class OrdersForm(forms.ModelForm):
	class Meta:
		model = OrderForm

		fields = [
			'name',
			'status_order',
            'amount',
            'price',
            'price_free_VAT',
            'VAT',
            'price_with_VAT',
            'total',
		]

		widgets = {
			'name': forms.TextInput(attrs={'class': 'formset-field'}),
			'status_order': forms.TextInput(attrs={'class': 'formset-field'}),
			'price': forms.NumberInput(attrs={'class': 'formset-field'}),
            'price_free_VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'price_with_VAT': forms.NumberInput(attrs={'class': 'formset-field'}),
            'total': forms.NumberInput(attrs={'class': 'formset-field'}),
		}


