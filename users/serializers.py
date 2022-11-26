from django.contrib import auth
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from .models import User, phone_validator
from plots.models import Plot


class UserRegisterSerializer(serializers.ModelSerializer):
    reqid = serializers.IntegerField()
    address = serializers.CharField(max_length=256)
    land_area = serializers.IntegerField()

    class Meta:
        model = User
        fields = (
            'id', 'phone', 'first_name', 'last_name', 'password', 'reqid', 'address', 'land_area'
            )
    
    def save(self, **kwargs):
        vd = self.validated_data

        user = User.objects.create_user(
            phone=vd.get('phone'),
            password=vd.get('password'),
        )
        user.first_name = vd.get('first_name')
        user.last_name = vd.get('last_name')
        user.save()

        Plot.objects.create(
            user=user,
            reqid=vd.get('reqid'),
            address=vd.get('address'),
            land_area=vd.get('land_area')
        )
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[phone_validator])
    password = serializers.CharField(min_length=8, write_only=True)
    password_confirm = serializers.CharField(min_length=8, write_only=True)
    tokens = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password', 'password_confirm', 'tokens')
        read_only_fields = ('id', )
    
    def get_tokens(self, obj):
        user = User.objects.get(phone=obj['phone'])
        return user.get_tokens()
    
    def validate(self, attrs):
        password_confirm = attrs.get('password_confirm')
        password = attrs.get('password')
        phone = attrs.get('phone')

        user = auth.authenticate(phone=phone, password=password)

        if password_confirm != password:
            raise AuthenticationFailed('Пароли не совпадают!')
        if not user:
            raise AuthenticationFailed('Неверный номер телефона или пароль')
        if not user.is_active:
            raise AuthenticationFailed('Аккаунт не активный')
        return super().validate(attrs)
