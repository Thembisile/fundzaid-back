from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password', 'is_donor', 'is_campaign_organizer')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = UserProfile
        fields = ['user', 'is_organizer', 'phone_number', 'address']
