from rest_framework.generics import RetrieveAPIView

from .serializers import PlaceSerializer
from .models import Place

# Create your views here.
class PlaceAPIView(RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
