from rest_framework import generics
from user.serializers import UserSerializer
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    # define what serializer you want to use
    serializer_class = UserSerializer
