from django import forms
from django.contrib.auth.models import User

from donor import models


class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = models.DonorProfile


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
