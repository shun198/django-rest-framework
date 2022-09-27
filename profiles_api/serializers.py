from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # Use Meta to specify a model and the fields you want to use in your api
    class Meta:
        model = models.UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {
                # passwordだけwrite-onlyにしたい
                "write_only": True,
                # custom styleを追加
                # パスワードを入力した際に見えないようにする
                "style": {"input_type": "password"},
            }
        }

    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )

        return user
