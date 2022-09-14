from django.urls import path
from .views import PlaceAPIView

urlpatterns = [
    path("place/<int:pk>/", PlaceAPIView.as_view()),
]
