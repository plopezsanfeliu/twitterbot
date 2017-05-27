from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20, min_length=3)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=12, min_length=8)
    password2 = forms.CharField(label='Repite password', widget=forms.PasswordInput, max_length=12, min_length=8)
    email = forms.EmailField(label='Email', max_length=50)
