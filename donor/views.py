from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from donor.forms import DonorForm, StoreForm, CouponSubmitForm, FoodSearchForm
from donor.models import DonorProfile, Food

# Create your views here.

def search(request):
    results = None
    if request.method == 'POST':
        form = FoodSearchForm(request.POST)
        if form.is_valid():
            food = form.cleaned_data['food']
            results =  Food.objects.all().filter(name = food) #Might not work.
            for result in results:
                print(result)
        return render(request,"donor/search.html",{'results':results,'form':form})
    else:
        form = FoodSearchForm()
        return render(request,"donor/search.html",{'results':results,'form':form})

def sale(request):
    if request.session.get('store_login',False): #Might need to change store_login
        return HttpResponse("Please log in")
    else:
        if request.method == 'POST':
            form = CouponSubmitForm(request.POST)
            if form.is_valid():
                code = form.cleaned_data['coupon']
                # coupon = Coupon.objects.get(id=code)
                # coupon.delete()
                return HttpResponseRedirect('/donor/sale/')
        else:
            form = CouponSubmitForm()
        return render(request,"donor/couponsubmit.html",{'form':form})

def register(request):
    if request.method == 'POST':
        donor_form = DonorForm(data=request.POST)
        store_form = StoreForm(data=request.POST)
        if donor_form.is_valid() and store_form.is_valid():
            store = store_form.save()
            donor = donor_form.save()
            donor.set_password(donor.password)
            donor.is_active = False
            donor.save()
            DonorProfile.objects.create(user=donor, store=store)
            return HttpResponse('REQUEST SENT')
        else:
            print (donor_form.errors)
    else:
        donor_form = DonorForm()
        store_form = StoreForm()

    return render(request, 'donor/register.html', {'donor_form': donor_form, 'store_form': store_form})


def donor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('LOGGED_IN')
        else:
            return HttpResponse('WRONG AUTH DETAILS')
    else:
        return render(request, 'feed_the_children/login.html', {})


@login_required()
def donor_logout(request):
    logout(request)
    return HttpResponse('LOGGED_OUT')
