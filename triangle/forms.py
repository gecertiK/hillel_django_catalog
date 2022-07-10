from django import forms


class GetForm(forms.Form):
    leg1 = forms.IntegerField(label='Leg 1', required=True, min_value=1)
    leg2 = forms.IntegerField(label='Leg 2', required=True, min_value=1)
