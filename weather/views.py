from django.views.generic import ListView
from rest_framework.generics import RetrieveAPIView
from weather.serializer import WeatherSerializer
from .models import Weather
from .serializer import WeatherSerializer

# Create your views here.
class TopView(ListView):
    model = Weather
    template_name = "top.html"


class WeatherAPIView(RetrieveAPIView):
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer
