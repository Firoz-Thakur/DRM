from rest_framework import serializers
from .models import stduent
class studentdeserilizer(serializers.Serializer):
    name=serializers.CharField(max_length=54)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=65)

    def create(self, validate_data):
        return Student.object.create(**validate_data)