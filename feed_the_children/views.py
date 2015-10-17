from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from feed_the_children.forms import UserForm
from feed_the_children.models import UserProfile
import random

# Create your views here.
def index(request):
    return render(request, 'feed_the_children/login.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            UserProfile.objects.create(user=user,
                                       address='270 Avenue',
                                       state='NY',
                                       zip='10018',
                                       net_income=1000,
                                       household_size=3)
            return HttpResponse('Registered')
        else:
            print (user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'feed_the_children/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
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
def user_logout(request):
    logout(request)
    return HttpResponse('LOGGED_OUT')


@login_required()
def list_of_food(request):
    context_dict = {'items': [('bannnas', 'walgreens', 3), ('watermelon', 'walgreens', 1), ('milk', 'costco', 1)]}
    return render(request, 'feed_the_children/foodlist.html', context_dict)

def get_coupon(request):
    coupon_list = ['0000','0001','1000','1111']
    index = random.randrange(0,5)
    return render(request, 'feed_the_children/coupon.html',coupon_list[index])

