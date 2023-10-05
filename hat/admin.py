from django.contrib import admin

from .models import Item
from .models import Meeting

# Register your models here.
admin.site.register(Item)
admin.site.register(Meeting)