from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.Serializer):
    owner = serializers.IntegerField(source='owner_id', read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    available = serializers.BooleanField()

    def create(self, validated_data):
        owner = self.context['request'].user
        service = Service(
            owner=owner,
            name=validated_data['name'],
            description=validated_data['description'],
            price=validated_data['price'],
            available=validated_data['available']
        )
        service.save()
        return service

    def update(self, instance, validated_data):
        instance.owner = self.context['request'].user
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.available = validated_data.get('available', instance.available)
        instance.save()
        return instance
