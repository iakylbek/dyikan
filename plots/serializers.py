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
    water_volume = serializers.SerializerMethodField(read_only=True)
    book_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Plot
        fields = ('id', 'reqid', 'address', 'water_volume', 'book_price', 'land_area')

    def get_water_volume(self, obj) -> float:
        volume = obj.land_area * obj.crop.water_consumption
        self.volume = volume
        return volume

    def get_book_price(self, obj) -> int:
        return self.volume * 0.5 * obj.book_channels.count()


class CropListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crop
        fields = ('id', 'name')
