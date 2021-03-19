from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.
# single object

def student_detail(request):
    stu=Student.objects.get(id=4)
    serialized=StudentSerializer(stu)
    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data,content_type='application/json')


#query set

def student_list(request):
    stu=Student.objects.all()
    print(stu)
    serialized=StudentSerializer(stu,many=True)
    print(serialized.data)
    json_data=JSONRenderer().render(serialized.data)
    return HttpResponse(json_data,content_type='application/json')
