from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=65)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=654)
    
