# users/serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'role', 'profile_pic', 'date_joined']
        # make sure password isn't returned in the reponse
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Override create method to hash password before saving"""
        password = validated_data.pop('password', None)  # Extract password safely
        user = User(**validated_data)
        if password:
            user.set_password(password)  # Hash password
        user.save()
        return user
