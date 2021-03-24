from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
# @api_view() by default is 'GET'

# # def helow_world(request):
# #     return Response({'msg':'hellow world'})

@api_view(['GET','POST'])
def helow_world(request):
     if request.method=='GET':
         return Response({'msg':'hellow world'})
     else:
         print(request.data)
         return Response({'msg': 'this is post requst','data':request.data})
 
