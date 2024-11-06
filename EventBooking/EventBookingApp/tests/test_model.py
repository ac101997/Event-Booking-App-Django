import pytest
from django.contrib.auth.models import User
from EventBookingApp.models import *

@pytest.mark.django_db
def test_profile_creation():

    user= User.objects.create(username='testcase user visitor')
    type= UserProfile.TypeChoice.VISITOR

    profile=UserProfile.objects.create(user=user,type=type)
    

    assert profile.user==user
    assert profile.type=='VI'



@pytest.mark.django_db
def test_event_creation():

    user= User.objects.create(username='testcase user organizer')
    type= UserProfile.TypeChoice.ORGANIZER

    org_profile=UserProfile.objects.create(user=user,type=type)

    event = Events.objects.create(event_name="test_event", date="2024-11-05 10:00", venue="test A", organizer=org_profile)

    assert event.organizer.type=='ORG'
    assert event.event_name== 'test_event'


@pytest.mark.django_db
def test_ticket_booking():
    user=User.objects.create(username="test booking")
    booked_by=UserProfile.objects.create(user=user,type=UserProfile.TypeChoice.VISITOR)

    # organizer=UserProfile.objects.create(user=user,type=UserProfile.TypeChoice.ORGANIZER)
    
    event_booked=Events.objects.create(event_name="test_event",date="2024-11-05 9:00", venue="Mumbai", organizer=booked_by)

    ticket_booked=Tickets.objects.create(event=event_booked,ticket_type=Tickets.TypeChoice.VIP,price=5000,is_available=True)


    booking=Booking.objects.create(booked_by=booked_by,event_booked=event_booked,ticket_booked=ticket_booked)

    assert booking.event_booked==event_booked
    assert booking.ticket_booked.is_available==True
    assert booking.booked_by.type=="VI"


    
