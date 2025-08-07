from django.shortcuts import render
from django.http import JsonResponse
from .serializers import PinSerializer
from .serializers import TitlePinSerializer
from .models import Pin
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.


@api_view(["GET"])
def getUser(request):
    return Response({'username': request.user.username})


@api_view(["GET"])
def linkList(request):

    pins = Pin.objects.all().order_by('-id')
    serializer = PinSerializer(pins, many=True, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create(request):
    serializer = PinSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save(author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def view(request, pk):
    pin = Pin.objects.get(id=pk)
    serializer = PinSerializer(pin, many=False, context={"request": request})
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete(request, pk):
    pin = Pin.objects.get(id=pk)
    
    pin.delete()
    
@api_view(['GET'])
def updatetitle(request, pk):
    title = Pin.objects.get(id=pk)
    serializer = TitlePinSerializer(instance=title, title=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.data)

