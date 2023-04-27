from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField()
    pulled = models.BooleanField(default=False, editable=False)
    pulled_at = models.DateTimeField(null=True, blank=True)


    # todo: shame meeting for taking forever. We already have a query of all items pulled today,
    # todo: and we're storing times... timedelta, then add red highlight or something to long items
