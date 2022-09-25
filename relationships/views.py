from rest_framework import viewsets

from .serializers import CustomerSerializer,BookSerializer
from .models import Customer,Book

# Create your views here.
class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    
class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
