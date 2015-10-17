from django import forms
from django.contrib.auth.models import User

from donor import models

class FoodSearchForm(forms.Form):
    food = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class CouponSubmitForm(forms.Form):
    coupon = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class DonorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = models.DonorProfile
        fields = ('user', 'store',)


class StoreForm(forms.ModelForm):
    class Meta:
        model = models.Store
        fields = ('name', 'address', 'state', 'zip')


class FoodForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = ('name', 'quantity', 'weight', 'category')


class CouponForm(forms.ModelForm):
    class Meta:
        model = models.Coupon
        fields = ('food', 'code', 'quantity')
