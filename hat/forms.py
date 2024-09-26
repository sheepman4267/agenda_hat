from django.forms import ModelForm, widgets
from .models import Item, Meeting


class ItemForm(ModelForm):
    model = Item
    fields = [
        'text',
        'meeting',
        'major',
        'finished',
    ]


class MeetingCreateForm(ModelForm):
    class Meta:
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
        }
        model = Meeting
        fields = [
            'title',
            'date',
        ]
