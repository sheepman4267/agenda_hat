from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView

import random

from .models import Item


def get_remaining_items():
    return Item.objects.filter(pulled=False).count()

def index(request):
    return render(request, 'hat/hat.html', {
        'hat_class': 'index',  # todo: make timedelta in line 12 configurable
        'past_items': Item.objects.filter(pulled=True, pulled_at__range=(timezone.now() - timezone.timedelta(hours=6), timezone.now())),
        'remaining_items': Item.objects.filter(pulled=False).count(),
    })


def pull_item(request):
    item = ''
    hat_class = ''
    try:
        item = random.choice(Item.objects.filter(pulled=False))
        item.pulled = True
        item.pulled_at = timezone.now()
        item.save()
    except IndexError:
        hat_class = 'finished'

    return render(request, 'hat/hat.html', {
        'item': item,
        'hat_class': hat_class,
        'past_items': Item.objects.filter(pulled=True, pulled_at__range=(timezone.now() - timezone.timedelta(hours=6), timezone.now())),
        'remaining_items': Item.objects.filter(pulled=False).count(),
    })


class CreateItemView(CreateView):
    model = Item
    template_name = "hat/new_item.html"
    fields = [
        'text',
    ]
    success_url = reverse_lazy('new-item')
    print(Item.objects.filter(pulled=False))
    extra_context = {
        'remaining_items': get_remaining_items
    }


