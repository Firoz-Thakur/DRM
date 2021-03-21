from django.shortcuts import render
import io
from .serializers import studentSeralizer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def studentCreate(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        seralizer=studentSeralizer(data=python_data)
        if seralizer.is_valid():
            seralizer.save()
            msg={'msg': 'data created successfully baba'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(seralizer.errors)
        return HttpResponse(json_data,content_type='application/json')

