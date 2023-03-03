from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # ['name', 'description', 'price', 'available']
        read_only_fields = []


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'  # ['service', 'date', 'start_time', 'end_time']
        read_only_fields = []
