from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CouponSubmitForm
from .models import Coupon


# Create your views here.
def sale(request):
    #if request.user.username != 'donor login':              Check if donor login
    #    return HttpResponse("Please log in")
    #else:
        if request.method == 'POST':
            form = CouponSubmitForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data['coupon']
                # coupon = Coupon.objects.get(id=code)
                # coupon.delete()
                return HttpResponseRedirect('/donor/sale')
        else:
            form = CouponSubmitForm()
        return render(request,"donor/couponsubmit.html",{'form':form}) #Change couponsubmit to the right template

def register(request):
    registered = False
    if request.method == 'POST':
        pass

def donor_ui(request):
    return render(request,"donor/donorui.html",{})
