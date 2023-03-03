from datetime import *
from .models import Reception
from rest_framework import serializers


def is_valid_time(start: time, end: time, queryset, day=date.today()) -> bool:
    work_time = {'s': time(hour=9),
                 'e': time(hour=18)}
    if day < date.today():
        return False
    if work_time['e'] < start < work_time['s'] or work_time['e'] < end or \
            datetime.combine(day, start) + timedelta(minutes=15) > datetime.combine(day, end):
        return False
    return all([start >= q.end_time or end <= q.start_time for q in queryset if q.date == day])


class ReceptionSerializer(serializers.Serializer):
    service = serializers.IntegerField(source='service_id')
    user = serializers.IntegerField(source='user_id', read_only=True)
    date = serializers.DateField()
    start_time = serializers.TimeField()
    end_time = serializers.TimeField()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        start_time: time = validated_data['start_time']
        end_time: time = validated_data['end_time']
        if is_valid_time(start_time, end_time, Reception.objects.all(), day=validated_data['date']):
            return Reception.objects.create(**validated_data)
        raise serializers.ValidationError('ERROR: Wrong time')

    def update(self, instance, validated_data):
        start_time = validated_data.get('start_time', instance.start_time)
        end_time = validated_data.get('end_time', instance.end_time)
        if is_valid_time(start_time, end_time, Reception.objects.all(), day=validated_data['date']):
            instance.service = validated_data.get('service', instance.service)
            instance.user = self.context['request'].user
            instance.date = validated_data.get('date', instance.date)
            instance.start_time = start_time
            instance.end_time = end_time
            instance.save()
            return instance
        raise serializers.ValidationError('ERROR: Wrong time')
