from django import forms

class CheckBoxForm(forms.Form):
    exec_summary = forms.BooleanField(required=False)
    scope = forms.BooleanField(required=False)
    isms = forms.BooleanField(required=False)
    methodology = forms.BooleanField(required=False)
    recommendation = forms.BooleanField(required=False)