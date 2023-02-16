from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField()
    pulled = models.BooleanField(default=False, editable=False)