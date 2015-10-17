from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from donor.forms import DonorForm, StoreForm, FoodPictureForm
from donor.models import DonorProfile, FoodPicture


# Create your views here.
def index(request):
    return HttpResponse('OK')


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
        return render(request, 'donor/login.html', {})


@login_required()
def donor_logout(request):
    logout(request)
    return HttpResponse('LOGGED_OUT')


@login_required()
def upload_picture(request):
    if request.method == 'POST':
        form = FoodPictureForm(request.POST, request.FILES)
        if form.is_valid():
            FoodPicture(picture=request.FILES['picture']).save()
        else:
            print form.errors
    else:
        form = FoodPictureForm()

    return render(request, 'donor/picupload.html', {'form': form})
