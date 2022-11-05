from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from relationships.serializers import (
    LoginSerializer,
    UserSerilaizer,
)
from rest_framework.viewsets import ModelViewSet
from relationships.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()


    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        else:
            return UserSerilaizer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)
