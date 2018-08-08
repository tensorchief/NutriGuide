from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

from guide.models import TitleCard
from guide.forms import ProfileForm


def index(request):
    cards = [
        TitleCard('Weekly menu planning',
                  'Create personalized weekly menu plan based on your nutrition goals.',
                  'danger',
                  'fa-calendar-alt'),
        TitleCard('Shopping list',
                  'Add items from your menu plan to shopping list.',
                  'warning',
                  'fa-shopping-cart'),
        TitleCard('Personal settings',
                  'Edit personal settings and calculate nutrition goals.',
                  'info',
                  'fa-heartbeat'),

    ]
    return render(request, 'guide/index.html', {'cards': cards})


def logout(request):
    auth_logout(request)
    return redirect('index')


def login(request):
    return HttpResponseRedirect('/admin/login/?next=/')


def settings(request):
    form = ProfileForm()
    return render(request, 'guide/settings.html', {'form': form})
