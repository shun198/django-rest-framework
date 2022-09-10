from django.shortcuts import render
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView

from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(ListView):
    template_name = "list.html"
    model = Book


class BookListAPI(ListCreateAPIView):
    # どのデータを取得すべきかquerysetに指定
    queryset = Book.objects.all()
    # シリアライザと紐つける
    serializer_class = BookSerializer
    # 認証内容
    # permission_classes = [IsAuthenticated]
