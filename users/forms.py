from django import forms
from .models import Location



class Location_Form(forms.ModelForm):
    
    class Meta:
        model = Location
        fields = {
            'address_1', 'address_2', 'city', 'state', 'post_code',
        }