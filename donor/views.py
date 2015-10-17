from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from donor.forms import DonorForm, StoreForm, FoodPictureForm, FoodForm
from donor.models import DonorProfile, FoodPicture, Food


# Create your views here.
def index(request):
    food_list = Food.objects.filter(store=DonorProfile.objects.get(user=request.user.id).store)
    return render(request, 'donor/index.html', {'food_list': food_list})


def register(request):
    """
    Allows registration for a donor profile.
    :param request:
    :return: render response
    """
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
    """
    Allows donors to login.
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect('/donor/')
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


@login_required()
def add_food(request):
    if request.method == 'POST':
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food = food_form.save(commit=False)
            food.store = DonorProfile.objects.get(user=request.user).store
            food.save()
            return HttpResponseRedirect('/donor/')
        else:
            print food_form.errors
    else:
        food_form = FoodForm()

    return render(request, 'donor/add.html', {'add_form': food_form})


@login_required()
def scan_coupon(request):
    pass
