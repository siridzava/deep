from django import forms
from django.contrib.auth.models import User
from dive_in.models import Character


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ('character_name', 'action_points', 'hit_points',
                  'crit_hit_points', 'gold', 'silver')

