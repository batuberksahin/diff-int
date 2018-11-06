from django import forms
from .models import question

class questionForms(forms.Form):
    value = forms.CharField(label='Denklem', required=False)
    variable = forms.CharField(label='Degişken', required=False)

    variable.clean('x')
    """class Meta:
        model = question
        fields = [
            'value',
            'variable',
        ]"""