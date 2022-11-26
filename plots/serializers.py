from rest_framework import serializers

from .models import BookChannel


class BookChannelListSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookChannel
        fields = ('id', 'date')


class BookChannelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookChannel
        fields = ('id', 'plot', 'date')
