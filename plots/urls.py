from django.urls import path

from .views import BookChannelListView, BookChannelCreateView, PlotListView

urlpatterns = [
    path('list/', PlotListView.as_view()),

    path('book-channel/list/', BookChannelListView.as_view()),
    path('book-channel/create/', BookChannelCreateView.as_view()),
]
