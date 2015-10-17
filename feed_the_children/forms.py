from django import forms

class CouponSubmitForm(forms.Form):
    coupon = forms.CharField(label = "Coupon Code")
