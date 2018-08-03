from django.http import HttpResponse
from django.shortcuts import render

from guide.models import TitleCard


def index(request):
    cards = [
        TitleCard('Weekly planning',
                  'View weekly nutrition plan',
                  'danger',
                  'fa-calendar-alt'),
        TitleCard('Shopping list',
                  'Add items from nutrition plan to shopping list',
                  'warning',
                  'fa-shopping-cart'),
        TitleCard('Personal settings',
                  'Set nutrition goals',
                  'info',
                  'fa-heartbeat'),

    ]
    return render(request, 'guide/index.html', {'cards': cards})

