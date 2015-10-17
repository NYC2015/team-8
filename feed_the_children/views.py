from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

from feed_the_children.forms import UserForm, UserProfileForm
from feed_the_children.models import UserProfile


# Create your views here.
def index(request):
    return HttpResponse('OK')

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
            registered = True
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
