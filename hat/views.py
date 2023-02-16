from django.shortcuts import render

import random

from .models import Item


def pull_item(request):
    item = ''
    hat_class = ''
    try:
        item = random.choice(Item.objects.filter(pulled=False))
        item.pulled = True
        item.save()
    except IndexError:
        hat_class = 'finished'

    return render(request, 'hat/hat.html', {
        'item': item,
        'hat_class': hat_class,
    })