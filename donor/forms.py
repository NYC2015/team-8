from django import forms
from django.contrib.auth.models import User
from donor import models

class CouponSubmitForm(forms.Form):
    coupon = forms.CharField(label = "Coupon Code")

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = models.DonorProfile
    fields = ('user',)


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
