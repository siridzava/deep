from django import forms
from django.contrib.auth.models import User
from dive_in.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('character_name', 'gold', 'silver')
