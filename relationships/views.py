from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
    JsonResponse,
)
from .serializers import (
    CustomerSerializer,
    BookSerializer,
    WorkplaceSerializer,
    BankSerializer
)
from .models import Customer, Book,Workplace,Bank

# Create your views here.
class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        # query = self.request.GET.get('query', None)
        # self.queryset = Customer.objects.filter(name__icontains=query)
        # return self.queryset
        return Response({'data': 'my custom JSON'})


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class WorkplaceViewSets(viewsets.ModelViewSet):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class BankViewSets(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
