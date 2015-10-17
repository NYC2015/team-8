from django.shortcuts import render, HttpResponse

from feed_the_children.forms import UserForm, UserProfileForm


# Create your views here.
def index(request):
    return HttpResponse('OK')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile = UserProfileForm(request.POST)
        if user_form.is_valid() and profile.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile.save(commit=False)
            profile.user = request.user
            profile.address = '270 Avenue'
            profile.state = 'NY'
            profile.zip = '10000'
            profile.net_income = 10000
            profile.household_size = 2
            profile.save()

            registered = True
            return HttpResponse('Registered')
        else:
            print user_form.errors, profile.errors
    else:
        user_form = UserForm()

    return render(request, 'feed_the_children/register.html', {'user_form': user_form, 'registered': registered})
