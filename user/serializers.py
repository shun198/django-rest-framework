from django.contrib.auth import get_user_model
from rest_framework import serializers
# serializers are way to convert python objects
# takes json input
# validates inputs
# converts to python objects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # カスタムユーザモデルを使用
        model = get_user_model()
        fields = ["email","password","name"]
        extra_kwargs = {"password":{"write_only":True,"min_length":5}}

    # override create method
    def create(self,validated_data):
        return get_user_model().objects.create_user(**validated_data)