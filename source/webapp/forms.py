from django import forms
from django.forms import widgets

from webapp.models import CATEGORY_CHOISES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=False, label='Description',
                                       widget=widgets.Textarea)
    category = forms.ChoiceField(choices=CATEGORY_CHOISES, required=True, label='Category')
    balance = forms.IntegerField(required=True, min_value=0, label='Balance')
    price = forms.DecimalField(required=True, max_digits=7, decimal_places=2, label='Price')