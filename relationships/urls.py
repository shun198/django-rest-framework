from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PlaceAPIView

urlpatterns = [
    path("place/<str:pk>/", PlaceAPIView.as_view()),
]
