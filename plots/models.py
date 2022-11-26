from django.db import models

from users.models import User


class Crop(models.Model):
    name = models.CharField('Культура', max_length=128)


class Plot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plots')
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True)
    req_id = models.CharField('Регистрационный номер земельного участка', max_length=32)
    address = models.CharField('Адрес', max_length=256)
    land_area = models.IntegerField('Площадь земли')

    class Meta:
        pass
