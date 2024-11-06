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
from EventBookingApp.tasks import  *

from django.db.models import Q
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

class  TicketsViewset(viewsets.ModelViewSet):
    queryset=Tickets.objects.all()
    serializer_class=TicketSerializer
    permission_classes=[IsOrganizer]

class  BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes=[IsVisitor]

    def perform_create(self,serializer):
        print(f"User: {self.request.user}")  # Debugging line (just to check if code is working or not)
        user_profile = self.request.user.user_profile
        #serializer.save(booked_by=user_profile)

        email_send.delay(email=self.request.user.email)
        # return Response({'message': 'Ticket booked successfully!'}, status=status.HTTP_201_CREATED)


class  UserProfileViewset(viewsets.ModelViewSet):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer



# def orm(request):
#     query=Tickets.objects.select_related('event').all()

#     pre_query=Events.objects.prefetch_related('event_for_ticket').all()
#     for q in pre_query:
#         for price in q.event_for_ticket.all():
#             print(price.price)
#         #print(q.event_name,[price for q.event_for_ticket.price.all()])
#     return HttpResponse(pre_query)



class SearchFeature(APIView):
    def get(self,request):
        events=Events.objects.all()

        #get query parameters from request
        event_name=request.query_params.get('event_name',None)
        venue=request.query_params.get('venue',None)
        organizer=request.query_params.get('organizer',None)
        date=request.query_params.get('date',None)

        #Applying filters based on request params

        # if event_name:
        #     print("****",event_name)
        #     events=events.filter(event_name__icontains=event_name)

        # if venue:
        #     events=events.filter(venue__icontains=venue)

        # if date:
        #     events=events.filter(date=date)

        # if organizer:
        #     events=events.filter(organizer__user__username=organizer)

        # events=events.filter(Q(event_name__icontains=event_name) |(Q(venue__icontains=venue) )|
        #                               Q(date__icontains=date) | Q(organizer__user__username=organizer))

        query=Q()
        if event_name:
            query |=Q(event_name__icontains=event_name)

        if venue:
            query |=Q(venue__icontains=venue)

        if date:
            query |=Q(date__icontains=date)

        if organizer:
            query |=Q(organizer__user__username=organizer)

        events=events.filter(query) if query else events

        event_serializer=EventSerializer(events,many=True)
        return Response(event_serializer.data,status=status.HTTP_200_OK)

        

    