from rest_framework import serializers
from accounts.models import CustomUser

from django.contrib.auth import get_user_model


class CustomUserSerializer(serializers.ModelSerializer):
    
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def validate(self, data):
        password1 = data.get('password1')
        password2 = data.get('password2')

        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError('Passwords do not match')
        return data
    
    def create(self, validated_data):
        """
        Create and return a new `CustomUser` instance with the validated data.
        """
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data, password=password)
        return user