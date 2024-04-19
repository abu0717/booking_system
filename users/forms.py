from django import forms
from .models import UserModel
from django.core.exceptions import ValidationError
import re


class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = '__all__'

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Passwords do not match')
        elif len(self.cleaned_data['password']) < 6:
            raise ValidationError('Password length must be at least 6 characters')
        elif not re.match('.*[A-Z]', self.cleaned_data['password']):
            raise ValidationError('Password must contain at least 1 upper case character')
        elif not re.match('.*[a-z]', self.cleaned_data['password']):
            raise ValidationError("Your password must contain at least 1 lower case character.")
