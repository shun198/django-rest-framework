from django.urls import path
from .views import BookList, BookListAPI

urlpatterns = [path("list/", BookList.as_view()), path("api/", BookListAPI.as_view())]
