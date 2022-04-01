from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=32, required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
