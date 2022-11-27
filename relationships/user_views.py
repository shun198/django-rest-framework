from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ObjectDoesNotExist
from .permissions import (
    IsSuperUser,
    IsManagementUser,
    IsGeneralUser,
    IsPartTimeUser,
)
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from .serializers import (
    LoginSerializer,
    UserSerializer,
    ChangePasswordSerializer,
    EmailSerializer,
    ResetPasswordSerializer,
    CustomerSerializer,
)
from rest_framework.viewsets import ModelViewSet
from .models import User,Customer
from .emails import send_welcome_email, send_password_reset

class UserViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == "send_invite_user_mail":
            return Customer.objects.all()
        else:
            return User.objects.all()

    def get_serializer_class(self):
        if self.action in ["login","logout"]:
            return LoginSerializer
        elif self.action == "change_password":
            return ChangePasswordSerializer
        elif self.action == "send_invite_user_mail":
            return CustomerSerializer
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

    @action(methods=["POST"], detail=False,permission_classes=[])
    def logout(self, request):
        logout(request)
        return HttpResponse()

    @action(methods=["POST"], detail=False)
    def change_password(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        user = request.user

        if user.check_password(serializer.validated_data['current_password']):
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return HttpResponse()
        else:
            return JsonResponse(data={"msg": "current password is incorrect"}, status=400)

    @action(detail=False, methods=["POST"], permission_classes=[IsManagementUser])
    def send_invite_user_mail(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        name = serializer.validated_data.get("name")
        email = serializer.validated_data.get("email")
        send_welcome_email(name=name,email=email)
        return HttpResponse()

    @action(detail=False, methods=["POST"], permission_classes=[IsManagementUser])
    def send_reset_password_mail(self, request):
        serializer = EmailSerializer(data=request.data)
        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        email = serializer.data.get("email")
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return HttpResponse()
        data = {"email": email}
        send_password_reset(email)
        return HttpResponse()

    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            permission_classes = [IsManagementUser]
        if self.action == "create":
            permission_classes = [IsGeneralUser]
        elif self.action == "destroy":
            permission_classes = [IsSuperUser]
        elif self.action in ["list","retrieve"]:
            permission_classes = [IsPartTimeUser]
        elif self.action in ["login"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
