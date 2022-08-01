from django import forms
from django.core import validators


class ShortnerForm(forms.Form):
    link = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Give me your link',
        'class': 'form-control',
        'type': 'url',
        'aria-describedby': 'button-addon2',
        'aria-label': 'Recipients username',
        'name': 'link',
    }), required=True, validators=[validators.URLValidator(), ])
