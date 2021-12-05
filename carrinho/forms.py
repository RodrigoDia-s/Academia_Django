from django import forms
from django.conf import settings

plano_QUANTITY_CHOICES = [
    (i, str(i)) for i in range(1, settings.CART_ITEM_MAX_QUANTITY + 1)
]


class CartAddplanoForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label="Quantidade", choices=plano_QUANTITY_CHOICES, coerce=int
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
