from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput()
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email.endswith('@gmail.com'):
            raise ValidationError("Gmail emails are not allowed")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 6:
            raise ValidationError("Password must be at least 6 characters")

        return password
