from django import forms
from orders.models import ShippingAddress


class CheckoutForm(forms.ModelForm):
    """
    Checkout form — captures shipping address at the time of order.
    Maps directly to ShippingAddress model fields.
    """
    class Meta:
        model = ShippingAddress
        exclude = ['order']   # 'order' is assigned in the view after Order is created
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
            'phone':     forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'address':   forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Street address'}),
            'city':      forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'country':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country'}),
            'zip_code':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ZIP / Postal code'}),
        }
