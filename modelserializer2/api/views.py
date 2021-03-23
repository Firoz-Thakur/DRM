from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import student
from .serializers import studentserializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
# Create your views here.
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=student.objects.get(id=id)
            serializer=studentserializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
        stu=student.objects.all()
        serializer=studentserializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=studentserializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':"Data created bab"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        serializer=studentserializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data update'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted baby'}
        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
            
















