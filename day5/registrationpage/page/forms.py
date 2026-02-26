from django import forms

class RegisterForm(forms.Form):
    full_name = forms.CharField(
        label="Full Name",
        min_length=5,
        max_length=50
    )

    email = forms.EmailField(
        label="Email"
    )

    password = forms.CharField(
        label="Password",
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )
