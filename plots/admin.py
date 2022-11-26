from django.contrib import admin

from .models import Plot, Crop


@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'req_id')
