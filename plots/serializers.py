from rest_framework import serializers

from .models import BookChannel, Plot


class BookChannelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookChannel
        fields = ('id', 'date')


class BookChannelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookChannel
        fields = ('id', 'plot', 'date')


class PlotListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plot
        fields = ('id', 'reqid', 'address', 'land_area')
