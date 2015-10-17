from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CouponSubmitForm

# Create your views here.

def sale(request):
    if request.session.get('store_login',False):
        return HttpResponse("Please log in")
    else:
        if request.method == 'POST':
            form = CouponSubmitForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/donor/submitOK')
        else:
            form = CouponSubmitForm()
        return render(request,"couponsubmit.html",{'form':form}) #Change couponsubmit to the right template

def submitOK(request):
    return HttpResponseRedirect('/donor/sale')
    # Do some database stuff here
