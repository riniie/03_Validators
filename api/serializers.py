from rest_framework import serializers
from .models import Student


# Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name must start with r!')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field Level Validation
    def validate_roll(self, roll):
        if roll > 100:
            raise serializers.ValidationError('Seat Full')
        return roll

    # Object Level Validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == 'nina' and city != 'LA':
            raise serializers.ValidationError('Nina must live in LA')
        return data
