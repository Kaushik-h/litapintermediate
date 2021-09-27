from django.contrib.auth import authenticate
from Auth.models import User

from rest_framework import serializers

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'primaryEmail','primaryPhone','isTribeLeader')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'username', 'primaryEmail','primaryPhone')
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class SocialSerializer(serializers.Serializer):

    access_token = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True,
    )