from django.shortcuts import render, HttpResponse

from feed_the_children.forms import UserForm, UserProfileForm


# Create your views here.
def index(request):
    return HttpResponse('OK')


def register(request):
    if request.method == 'POST':
        pass