from django.urls import path
from .views import pull_item


urlpatterns = [
    path('', pull_item)
]