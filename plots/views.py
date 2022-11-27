from rest_framework import generics, permissions

from .models import Plot, BookChannel
from .serializers import BookChannelListSerializer, BookChannelCreateSerializer, PlotListSerializer
from users.models import User


class BookChannelListView(generics.ListAPIView):
    serializer_class = BookChannelListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BookChannel.objects.filter(plot__user=self.request.user)


class BookChannelCreateView(generics.CreateAPIView):
    queryset = BookChannel.objects.all()
    serializer_class = BookChannelCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlotListView(generics.ListAPIView):
    serializer_class = PlotListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Plot.objects.filter(user=self.request.user)
