from django.urls import path

from .views import BookChannelListView, BookChannelCreateView, PlotListView, CropListView, PlotInfoView

urlpatterns = [
    path('list/', PlotListView.as_view()),
    path('info/<int:pk>/', PlotInfoView.as_view()),
    path('crop/list/', CropListView.as_view()),

    path('book-channel/list/', BookChannelListView.as_view()),
    path('book-channel/create/', BookChannelCreateView.as_view()),
]
