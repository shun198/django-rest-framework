from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView

from relationships.serializers import PlaceSerializer
from .models import Place

# Create your views here.
class PlaceAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
