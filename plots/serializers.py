from rest_framework import serializers

from .models import BookChannel, Plot, Crop


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


class PlotInfoSerializer(serializers.ModelSerializer):
    water_volume = serializers.SerializerMethodField()
    book_price = serializers.SerializerMethodField()

    class Meta:
        model = Plot
        fields = ('id', 'reqid', 'address', 'water_volume', 'book_price')
    
    def get_water_volume(self, obj) -> float:
        return 1

    def get_book_price(self, obj) -> int:
        return 1


class CropListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = ('id', 'name')
