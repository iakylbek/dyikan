from django.contrib import admin

from .models import Plot, Crop, BookChannel


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'reqid')


@admin.register(BookChannel)
class BookChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'plot', 'date')
    list_display_links = ('plot',)
