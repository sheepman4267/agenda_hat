from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, FormView

import random

from .models import Item, Meeting

from .forms import ItemForm, MeetingCreateForm


# def index(request):
#     return render(request, 'hat/hat.html', {
#         'hat_class': 'index',  # todo: make timedelta in line 12 configurable
#         'past_items': Item.objects.filter(pulled=True, pulled_at__range=(timezone.now() - timezone.timedelta(hours=6), timezone.now())),
#         'remaining_items': get_remaining_items(),
#     })


class IndexView(ListView):
    model = Meeting
    template_name = 'hat/meeting_list.html'


def pull_item(request, meeting_pk):
    item = ''
    hat_class = ''
    meeting = Meeting.objects.get(pk=meeting_pk)
    try:
        item = random.choice(meeting.hat_items().filter(pulled=False))
        item.pulled = True
        item.pulled_at = timezone.now()
        item.save()
    except IndexError:
        hat_class = 'finished'

    return render(request, 'hat/hat.html', {
        'item': item,
        'hat_class': hat_class,
        'past_items': meeting.finished_hat_items(),
        'meeting': meeting,
    })


def finish_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.finished = True
    item.save()
    return redirect(reverse('pull-item', kwargs={'meeting_pk': item.meeting.pk}))


class DeferItemView(UpdateView):
    model = Item
    fields = [
        'meeting'
    ]
    template_name = 'hat/defer-item.html'

    def form_valid(self, form):
        old_item = Item.objects.get(pk=self.object.pk)
        self.object.previous_meeting = old_item.meeting
        self.object.save()
        return super(DeferItemView, self).form_valid(form)

    def get_success_url(self):
        return reverse('pull-item', kwargs={'meeting_pk': self.object.previous_meeting.pk})


class CreateItemView(CreateView):
    model = Item
    template_name = "hat/new_item.html"
    fields = [
        'text',
        'meeting',
        'major',
    ]
    # success_url = reverse_lazy('new-item')
    extra_context = {
    }


class MeetingListView(ListView):
    model = Meeting
    template_name = "hat/meeting_list.html"


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = "hat/meeting_details.html"

    def get_context_data(self, **kwargs):
        context = super(MeetingDetailView, self).get_context_data(**kwargs)
        context['finished_items'] = context['meeting'].items.filter(pulled=True, finished=True)

        return context


class MeetingCreateView(CreateView):
    model = Meeting
    template_name = "hat/meeting_create.html"
    form_class = MeetingCreateForm


class ItemUpdateView(UpdateView):
    model = Item
    fields = [
        'text',
        'meeting',
        'major',
        'finished',
    ]
    template_name = 'hat/update_item.html'

