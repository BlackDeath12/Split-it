from django import forms
from .models import Product


class CheckBoxForm(forms.Form):
    choices = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    ##exec_summary = forms.BooleanField(required=False)
    ##scope = forms.BooleanField(required=False)
    ##isms = forms.BooleanField(required=False)
    ##methodology = forms.BooleanField(required=False)
    ##recommendation = forms.BooleanField(required=False)