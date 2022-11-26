from django.db import models

from users.models import User


class Crop(models.Model):
    name = models.CharField('Культура', max_length=128)

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name = 'Культура'
        verbose_name_plural = 'Культуры'


class Plot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plots')
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, null=True)
    reqid = models.CharField('Регистрационный номер земельного участка', max_length=32, unique=True)
    address = models.CharField('Адрес', max_length=256)
    land_area = models.IntegerField('Площадь земли')

    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участки'
    
    def __str__(self) -> str:
        return str(self.user.phone) + str(self.reqid)


class BookChannel(models.Model):
    plot = models.ForeignKey(
        Plot, 
        on_delete=models.CASCADE, 
        related_name='book_channels', 
        unique_for_date='date'
        )
    date = models.DateField()

    class Meta:
        verbose_name = 'Бронь канала'
        verbose_name_plural = 'Бронь каналов'

    def __str__(self) -> str:
        return str(self.plot.reqid) + str(self.date)
