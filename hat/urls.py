from django.urls import path
from .views import pull_item, index, CreateItemView


urlpatterns = [
    path("", index, name="index"),
    path("next", pull_item, name="pull-item"),
    path("add", CreateItemView.as_view(), name="new-item"),
]