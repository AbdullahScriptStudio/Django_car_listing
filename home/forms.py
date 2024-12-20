from django import forms
from .models import Listing101


class Listings_Form(forms.ModelForm):
    class Meta:
        model = Listing101
        fields = {'brand', 'model', 'vin', 'color', 'description', 'milage', 'transmission', 'pic'}