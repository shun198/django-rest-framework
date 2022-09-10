from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # Metaは別のデータに関する情報を提供する特定のデータセットのこと
    # モデル自体に関するデータを追加する必要がある場合は、Meta クラスを使用
    # 権限、データベース名、単数形と複数形の名前、抽象化、順序付けなど、モデルに関するさまざまなことを定義できる
    class Meta:
        model = Book
        fields = ["title", "author"]
