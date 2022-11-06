from django.http import JsonResponse,HttpResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import action
from relationships.serializers import (
    LoginSerializer,
    UserSerilaizer,
    ChangePasswordSerializer,
    InviteUserSerializer,
    EmailSerializer,
    ResetPasswordSerializer,
)
from rest_framework.viewsets import ModelViewSet
from relationships.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        elif self.action == 'change_password':
            return ChangePasswordSerializer
        elif self.action == 'invite_user':
            return InviteUserSerializer
        elif self.action == 'resend_user_invitation' or self.action == 'forgot_password':
            return EmailSerializer
        elif self.action == 'reset_password':
            return ResetPasswordSerializer
        else:
            return UserSerilaizer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        employee_number = serializer.data.get("employee_number")
        password = serializer.data.get("password")
        user = authenticate(employee_number=employee_number, password=password)
        if not user:
            return JsonResponse(data={"msg": "ユーザーまたパスワードが間違っています。"}, status=400)
        else:
            login(request, user)
            return HttpResponse()

    @action(methods=["POST"], detail=False)
    def logout(self, request):
        logout(request)
        return HttpResponse()
