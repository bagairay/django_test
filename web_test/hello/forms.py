from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    gender = forms.BooleanField(label='gender', required=False)
    age = forms.IntegerField(label='age')
    birthday = forms.DateField(label='birth')