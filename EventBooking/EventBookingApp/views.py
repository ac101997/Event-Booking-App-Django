from django.shortcuts import render
from .models import *
from django.views import View
from django.http import HttpResponse
import requests

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.

class  HomeView(View):
    def get(self,request):
        return HttpResponse("HomePage")
    

class RegisterView(CreateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[AllowAny]

class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    serializer_class=UserProfileSerializer

    def create(self,request):
        serializer=self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)



class  EventViewset(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventSerializer

    # def retrieve(self,request,pk=None):{'msg':'Data cannot be validated using the viewset'}
    #     try:
    #         event=Events.objects.get(id=pk)
    #         serializer=self.get_serializer(event)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Events.DoesNotExist:
    # #         return Response({"error":"Event not found"},status=status.HTTP_404_NOT_FOUND)

    # @action(detail=False,methods=['get'],url_path='by_event/(?P<event_name>[^/.]+)')
    # def retrieve_by_event(self,request,event_name=None):
    #     try:
    #         event=Events.objects.filter(event_name=event_name)
    #         serializer=self.get_serializer(event,many=True)
    #         return Response(serializer.data,status=status.HTTP_200_OK)
    #     except Events.DoesNotExist:
    #         return Response({"error":"Event not found"},status=status.HTTP_404_NOT_FOUND)

class  BookViewset(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventSerializer






























class  TicketsViewset(viewsets.ModelViewSet):
    queryset=Tickets.objects.all()
    serializer_class=TicketSerializer

class  BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

class  UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer



