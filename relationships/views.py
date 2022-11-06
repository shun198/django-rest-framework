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

# Create your views here.
@api_view(['GET'])
def health_check(request):
        return JsonResponse(data={"msg":"pass"},status=200)

class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self,request):
        book = Book.objects.values("id","name")
        return Response(book)

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
    serializer_class = CustomerSerializer
    # django-filter backendを追加
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomerFilter

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            permission_classes = [IsGeneralUser]
        elif self.action == 'destroy':
            permission_classes = [IsSuperUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

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
