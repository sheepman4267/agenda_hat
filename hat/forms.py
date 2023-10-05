from django.forms import ModelForm
from .models import Item


class ItemForm(ModelForm):
    model = Item
    fields = [
        'text',
        'meeting',
        'major',
        'finished',
    ]