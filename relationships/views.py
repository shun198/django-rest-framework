from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from django_filters.rest_framework import DjangoFilterBackend
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


# Create your views here.
class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self,request):
        book = Book.objects.values("id","name")
        return Response(book)

    @action(methods=['POST'], detail=True)
    def post_books(self,request,pk=None):
        book = self.get_object()
        serializer = self.get_serializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # django-filter backendを追加
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CustomerFilter


class WorkplaceViewSets(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer
    # django-filter backendを追加
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WorkPlaceFilter

class BankViewSets(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


@api_view(['GET'])
def health_check(request):
    try:
        return JsonResponse(data={"msg":"pass"},status=200)
    except:
        return JsonResponse(data={"msg":"fail"},status=500)
