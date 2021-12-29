from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Passenger
from .serializers import PassengerSerializer

@api_view(['GET', 'POST'])
def passenger_list(request):

    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = PassengerSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def passenger_detail(request, pk):
    try:
        passenger = Passenger.objects.get(pk=pk)
    except Passenger.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer(passenger)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PassengerSerializer(passenger, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        passenger.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

