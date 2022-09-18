from django.urls import path
from .views import PlaceAPIView

urlpatterns = [
    path("place/<str:pk>/", PlaceAPIView.as_view()),
]
