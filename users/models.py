from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken


phone_validator = RegexValidator(regex=r'^996\d{9}$', message='Передайте действительный номер телефона в формате 996ХХХХХХХХХ')

class UserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError(_('The Phone must be set'))
        user = self.model(phone=phone, **extra_fields)
        user.phone = phone
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone = models.CharField(
        verbose_name='Телефон',
        max_length=12,
        validators=[phone_validator],
        unique=True
    )
    first_name = models.CharField('Имя', max_length=34)
    last_name = models.CharField('Фамилия', max_length=34)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Список пользователей'

    def __str__(self):
        return str(self.phone)
    
    def get_tokens(self) -> dict:
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh), 
            'access': str(refresh.access_token)
            }
