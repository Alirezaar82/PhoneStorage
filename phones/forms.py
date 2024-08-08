from django import forms

from .models import PhonesModel

class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhonesModel
        fields = [
            'brand_name',
            'model_name',
            'brand_nationality',
            'color',
            'screen_size',
            'status',
            'manufacturing_country',
            'price',
        ]
