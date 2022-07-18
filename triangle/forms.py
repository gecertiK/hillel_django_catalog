from django import forms

from triangle.models import Person


class GetForm(forms.Form):
    leg1 = forms.IntegerField(label='Leg 1', required=True, min_value=1)
    leg2 = forms.IntegerField(label='Leg 2', required=True, min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
