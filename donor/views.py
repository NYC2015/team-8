from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CouponSubmitForm
from models import Coupon

# Create your views here.

def sale(request):
    if request.session.get('store_login',False): #Might need to change store_login
        return HttpResponse("Please log in")
    else:
        if request.method == 'POST':
            form = CouponSubmitForm(request.POST)
            if form.is_valid():
                code = form.clean_data['Coupon Code']
                coupon = Coupon.objects.get(id=code)
                coupon.delete()
                return HttpResponseRedirect('/donor/sale')
        else:
            form = CouponSubmitForm()
        return render(request,"couponsubmit.html",{'form':form}) #Change couponsubmit to the right template

