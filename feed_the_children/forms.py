from django import forms
from django.contrib.auth.models import User

from feed_the_children import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
