from django import forms
from django.forms.models import inlineformset_factory

from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderForm
        fields = (
            'name',
            'status_order',
            'amount',
            'price',
            'price_free_VAT',
            'VAT',
            'price_with_VAT',
            'total',
            'total_price_with_VAT',
            'total_price_ALL',
        )
#         labels = {
#             'name': "Product"
#         }


OrderFormSet = inlineformset_factory(
    Order,
    OrderForm,
    form=OrderForm,
    min_num=2,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=False  # show a checkbox in each form to delete the row
)
