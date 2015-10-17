from django.shortcuts import render
from form import CouponSubmitForm
# Create your views here.

def sale(request):
    if reguest.session.get('store_login',False):
        return HttpResponse("Please log in")
    else:
        if request.method == 'POST':
            form = CouponSubmitForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('/donor/submitOK')
        else:
            form = CouponSubmitForm()
        return render(request,"couponsubmit.html",{'form':form})

def submitOK(request):
    return HttpResponseRedirect('/donor/sale')
