from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Item
from .serializers import itemSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = itemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = itemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)