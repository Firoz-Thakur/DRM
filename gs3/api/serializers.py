from rest_framework import serializers
# Create your views here.
from .models import student
class studentSeralizer(serializers.Serializer):
    name=serializers.CharField(max_length=54)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=54)

    def create(self, validate_data):
        return student.objects.create(**validate_data)