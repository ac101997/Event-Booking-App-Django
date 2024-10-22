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
from EventBookingApp.permissions import *

# Create your views here.

class  HomeView(View):
    def get(self,request):
        return HttpResponse("HomePage")
    

# Same view as RegisterNested but here we are  using class based view for logic and not using nested serilizers.
#It may not work with nested serializer.
class RegisterView(CreateAPIView):
    user_serializer_class=UserSerializer
    user_profile_serializer_class=UserProfileSerializer
    permission_classes=[AllowAny]


    def post(self,request):
        try:

            user_data=request.data.get('user')
            profile_data=request.data.get('profile')

            user_serializer=self.user_serializer_class(data=user_data)
            if user_serializer.is_valid():
                user=user_serializer.save()

                profile_data['user']=user.id
                profile_serializer=self.user_profile_serializer_class(data=profile_data)

                if profile_serializer.is_valid():
                    profile_serializer.save()

                    return Response(user_serializer.data,status=status.HTTP_201_CREATED)
                
                return Response(profile_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
            return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({"error":"Invalid Data"},status=status.HTTP_400_BAD_REQUEST)
        


class RegisterViewNested(CreateAPIView):
    serializer_class=UserProfileSerializer
    permission_classes=[AllowAny]


class RegisterViewSet(viewsets.ModelViewSet):
    permission_classes=[AllowAny]
    serializer_class=UserProfileSerializer

    # def create(self,request):
    #     serializer=self.get_serializer(data=request.data)

    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)

class EventViewset(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventSerializer
    permission_classes = [IsOrganizer]

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

class  TicketsViewset(viewsets.ModelViewSet):
    queryset=Tickets.objects.all()
    serializer_class=TicketSerializer
    permission_classes=[IsOrganizer]

class  BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[IsVisitor]

    def perform_create(self,serializer):
        print(f"User: {self.request.user}")  # Debugging line
        user_profile=self.request.user.user_profile
        serializer.save(booked_by=user_profile)

class  UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer



