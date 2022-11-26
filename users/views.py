from rest_framework import generics, permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserLoginView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
