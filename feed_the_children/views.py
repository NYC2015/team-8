from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from feed_the_children.forms import UserForm
from feed_the_children.models import UserProfile

from donor.models import Coupon
import random
from donor.models import Food, Store

# Create your views here.
def index(request):
    return render(request, 'feed_the_children/login.html')


def register(request):
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

    return render(request, 'feed_the_children/register.html', {'user_form': user_form})


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
    if request.GET.get('zip', ''):
        stores = Store.objects.filter(zip=request.GET['zip'])
    else:
        stores = Store.objects.filter(zip=10018)
    nearby_foods = []
    for store in stores:
        foods = Food.objects.filter(store=store.pk)
        for food in foods:
            nearby_foods.append((store.name, food.name, food.quantity, food.weight))
    context_dict = {'items': [v for v in nearby_foods]}
    return render(request, 'feed_the_children/foodlist.html', context_dict)


@login_required()
def get_food(request):
    return render(request, 'feed_the_children/food.html', {'name': request.GET['name'],
                                                           'store': request.GET['store'],
                                                           'quantity': request.GET['qty']})

def get_coupon(request):
    index = random.randrange(1,4)
    coupon = Coupon.objects.get(pk=1)
    return render(request, 'feed_the_children/coupon.html',coupon)

