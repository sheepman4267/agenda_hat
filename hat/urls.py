from django.urls import path
from .views import pull_item, CreateItemView, MeetingListView, MeetingCreateView, MeetingDetailView, ItemUpdateView, DeferItemView, finish_item


urlpatterns = [
    path("", MeetingListView.as_view(), name="index"),
    path("meeting/<int:meeting_pk>/next", pull_item, name="pull-item"),
    path('meeting/<int:pk>', MeetingDetailView.as_view(), name="meeting"),
    path('meeting/new', MeetingCreateView.as_view(), name='new-meeting'),
    path("add", CreateItemView.as_view(), name="new-item"),
    path('item/<int:pk>', ItemUpdateView.as_view(), name="update-item"),
    path('item/<int:pk>/defer', DeferItemView.as_view(), name="defer-item"),
    path('item/<int:pk>/finish', finish_item, name="finish-item"),
]