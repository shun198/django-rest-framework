from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from .serializers import (
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    InviteUserSerializer,
    EmailSerializer,
    ResetPasswordSerializer,
)
from rest_framework.viewsets import ModelViewSet
from .models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == "login":
            return LoginSerializer
        if self.action == "logout":
            return LoginSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "invite_user":
            return InviteUserSerializer
        elif self.action == "resend_user_invitation" or self.action == "forgot_password":
            return EmailSerializer
        elif self.action == "reset_password":
            return ResetPasswordSerializer
        else:
            return UserSerializer

    @action(detail=False, methods=["POST"])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        employee_number = serializer.data.get("employee_number")
        password = serializer.data.get("password")
        user = authenticate(employee_number=employee_number, password=password)
        if not user:
            return JsonResponse(data={"msg": "either employee number or password is incorrect"}, status=400)
        else:
            login(request, user)
            return JsonResponse(data={'role': user.Role(user.role).name})

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        logout(request)
        return HttpResponse()
