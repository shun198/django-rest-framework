import csv, io,datetime
from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    JsonResponse,
)
from django.shortcuts import get_object_or_404
from django.core import serializers
from .serializers import (
    BookSerializer,
    AuthorSerializer,
    CustomerSerializer,
    WorkplaceSerializer,
    BankSerializer,
    CreateCustomerSerializer,
    DetailCustomerSerializer,
    # AuthTokenSerializer,
)
from .models import Author, Customer, Book,Workplace,Bank
from .filters import (
    CustomerFilter,
    WorkPlaceFilter,
)
from .permissions import (
    IsGeneralUser,
    IsSuperUser,
)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# class CreateTokenView(ObtainAuthToken):
#     # 自作した認証用シリアライザを使用
#     serializer_class = AuthTokenSerializer

# Create your views here.
@api_view(['GET'])
def health_check(request):
    return JsonResponse(data={"msg":"pass"},status=200)

class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    # django-filter backendを追加
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = CustomerFilter

    # POSTの時だけ
    def get_serializer_class(self):
        if self.action == "create":
            return CreateCustomerSerializer
        elif self.action == "retrieve":
            return DetailCustomerSerializer
        else:
            return CustomerSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        csv_file = request.FILES["file"]
        decoded_file = csv_file.read().decode("utf-8")
        io_string = io.StringIO(decoded_file)
        # header(1行目)を無視
        header = next(csv.reader(io_string))
        for row in csv.reader(io_string, delimiter=","):
            year = int(row[2].split("/")[0])
            month = int(row[2].split("/")[1])
            day = int(row[2].split("/")[2])
            birthday = datetime.date(year, month, day)
            # Customerに必要なデータ
            csv_data = {
                "name": row[0],
                "kana": row[1],
                "birthday": birthday,
                "post_no": row[3],
                "phone_no": "0" + row[4],
                "email": row[5],
            }
            serializer = CustomerSerializer(data=csv_data)
            if serializer.is_valid():
                serializer.save(created_by=request.user,updated_by=request.user)
            else:
                return JsonResponse({"msg":"CSVファイルのアップロードに失敗しました"},status=status.HTTP_400_CREATED)
        return JsonResponse({"msg":"CSVファイルのアップロードに成功しました"},status=status.HTTP_201_CREATED)


class WorkplaceViewSets(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
    # django-filter backendを追加
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkPlaceFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class BankViewSets(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


