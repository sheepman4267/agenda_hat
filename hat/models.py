from django.db import models
from django.urls import reverse_lazy


# Create your models here.
class Item(models.Model):
    text = models.TextField()
    pulled = models.BooleanField(default=False, editable=False)
    pulled_at = models.DateTimeField(null=True, blank=True)
    finished = models.BooleanField(default=False)
    major = models.BooleanField(default=False)
    meeting = models.ForeignKey(
        to='Meeting',
        unique=False,
        related_name='items',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    previous_meeting = models.ForeignKey(
        to='Meeting',
        unique=False,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse_lazy('meeting', kwargs={'pk': self.meeting.pk})


    # todo: shame meeting for taking forever. We already have a query of all items pulled today,
    # todo: and we're storing times... timedelta, then add red highlight or something to long items


class Meeting(models.Model):
    title = models.CharField(null=False, max_length=50)
    date = models.DateField(null=False)

    def get_absolute_url(self):
        return reverse_lazy('meeting', kwargs={'pk': self.pk})

    def major_items(self):
        return self.items.filter(major=True)

    def hat_items(self):
        return self.items.filter(major=False, finished=False)

    def new_hat_items(self):
        return self.items.filter(major=False, finished=False, pulled=False)

    def finished_hat_items(self):
        return self.items.filter(major=False, finished=True)

    def __str__(self):
        return f'{self.date} ({self.title})'

