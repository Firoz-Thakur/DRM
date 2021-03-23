from rest_framework import serializers
from .models import student


def start_with_r(value):
        if value[0].lower()!='r':
            raise serializers.ValidationError('Name should be start with r')
        

class studentserializer(serializers.ModelSerializer):
    name=serializers.CharField(validators=[start_with_r])
    class Meta:
        model=student
        fields='__all__'
    
 #field level validations   
    def validate_roll(self,value):
        if value>=200:
            raise serializers.ValidationError('seat full bebi')
        return value
    
  #object level validation  
    def validate(self,data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='rohit' and ct.lower()!='ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data