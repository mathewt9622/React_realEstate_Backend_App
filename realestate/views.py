from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from realestate.serializer import RealSerializer
from realestate.models import RealEsModel
# Create your views here.

@csrf_exempt
def add(request):
    if request.method=="POST":
        recieved_data=json.loads(request.body)
        print(recieved_data)
        
        serializer_check=RealSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"added successfully"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
    
@csrf_exempt
def view(request):
    if request.method=="POST":
        realList=RealEsModel.objects.all()
        serialize_data=RealSerializer(realList,many=True)
        
        return HttpResponse(json.dumps(serialize_data.data))    
    
    
@csrf_exempt
def delete(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status" :"deleted successfully"}))
    

@csrf_exempt
def search(request):
    if request.method=="POST":
        return HttpResponse(json.dumps({"status":"search successfully"}))
        