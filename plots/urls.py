from django.urls import path

from .views import BookChannelListView, BookChannelCreateView

urlpatterns = [
    path('book-channel/list/', BookChannelListView.as_view()),
    path('book-channel/create/', BookChannelCreateView.as_view())
]
