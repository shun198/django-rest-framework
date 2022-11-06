from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from study import settings
from .permissions import (
    IsManagementUser,
    IsGeneralUser,
    IsSuperUser,
)
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from .serializers import (
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    EmailSerializer,
    ResetPasswordSerializer,
)
from rest_framework.viewsets import ModelViewSet
from .models import User
from .emails import send_welcome_email, send_password_reset
from .tokens import generate_token

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ["login","logout"]:
            return LoginSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "send_invite_user_mail":
            return EmailSerializer
        elif self.action == "send_reset_password_mail":
            return ResetPasswordSerializer
        else:
            return UserSerializer

    # permission_classes=[]がないと権限がなくてログインできない
    @action(detail=False, methods=["POST"],permission_classes=[])
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

    @action(detail=False, methods=["POST"], permission_classes=[IsManagementUser])
    def send_invite_user_mail(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get("username")
        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        data = {
            'username': username,
            'email': email,
        }
        # token = generate_token(data, settings.VERIFY_USER_TOKEN_EXPIRE)
        serializer.save()
        send_welcome_email(user_email=email, username=name)
        return HttpResponse()

    @action(detail=False, methods=["POST"], permission_classes=[IsManagementUser])
    def send_reset_password_mail(self, request):
        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return HttpResponse()
        data = {"email": email}
        # token = generate_token(data, settings.PASSWORD_RESET_TOKEN_EXPIRE)
        send_password_reset(email)
        return HttpResponse()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsManagementUser]
        elif self.action == "destroy":
            permission_classes = [IsSuperUser]
        elif self.action == ["list","retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
