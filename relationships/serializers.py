from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Book, Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "name", "address"]
        
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ["id","title","price"]
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=Book.objects.all(),
#                 fields=("title","price"),
#                 message="タイトルと価格はユニークである必要があります"
#             )
#         ]
#         extra_kwargs = {
#             "title": {
#                 validators: [
#                     RegexValidator(r'^D.+$',message="タイトルはDで初めてください"),
#                 ],
#             },
#         }
        
# class BookSerializer(serializers.ListSerializer):
#     child = BookSerializer()
    
