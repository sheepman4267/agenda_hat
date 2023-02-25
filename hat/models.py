from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField()
    pulled = models.BooleanField(default=False, editable=False)
    agenda = models.ForeignKey(
        to='Agenda',
        unique=False,
        on_delete=models.CASCADE,
        related_name='items',
    )


class Agenda(models.Model):
    title = models.CharField()
    last_item = models.ForeignKey(
        to=Item,
        unique=True,
        on_delete=models.DO_NOTHING,
    ),
