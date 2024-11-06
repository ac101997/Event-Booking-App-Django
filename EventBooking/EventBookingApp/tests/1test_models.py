from EventBookingApp.models import *
import pytest



#decorator for any test that requires database access.
#@pytest.mark.django_db decorator ensures that the test has access to a temporary database.

# @pytest.mark.django_db 
# def test_event_creation():
#     event = Events.objects.create(event_name="Django testcase", date="2024-11-05", venue="test",organizer= "organizer_10")

#     # Check if the event's name is saved correctly
#     assert event.event_name == "Django testcase"

# EventBookingApp/tests/test_models.py
import pytest
from django.contrib.auth.models import User
from EventBookingApp.models import UserProfile, Events, Tickets, Booking


@pytest.mark.django_db
def test_user_profile_creation_visitor():
    user=User.objects.create(username="testcase visitor")
    type=UserProfile.TypeChoice.VISITOR

    profile=UserProfile.objects.create(user=user,type=type)

    assert profile.user==user
    assert profile.type=="VI"
    assert str(profile)=="VI"


@pytest.mark.django_db
def test_user_profile_creation_organiser():
    user=User.objects.create(username="testcase organizer")
    type=UserProfile.TypeChoice.ORGANIZER

    profile=UserProfile.objects.create(user=user,type=type)

    assert profile.user==user
    assert profile.type=="ORG"
    assert str(profile)=="ORG"

@pytest.mark.django_db
def test_event_creation():
    #event_name,date,venue,organizer
    user=User.objects.create(username="testcase organizer")
    organizer=UserProfile.objects.create(user=user,type=UserProfile.TypeChoice.ORGANIZER)

    event=Events.objects.create()




# @pytest.mark.django_db
# def test_user_profile_creation():
#     # Create a User instance
#     user = User.objects.create(username="testuser")
#     profile = UserProfile.objects.create(user=user, type=UserProfile.TypeChoice.VISITOR)
#     assert profile.user == user
#     assert profile.type == "VI"
#     assert str(profile) == "VI"

# @pytest.mark.django_db
# def test_event_creation():
#     # Create an Organizer Profile
#     user = User.objects.create(username="organizer_user")
#     organizer_profile = UserProfile.objects.create(user=user, type=UserProfile.TypeChoice.ORGANIZER)

#     # Create an Event
#     event = Events.objects.create(event_name="Conference", date="2024-11-05 10:00", venue="Hall A", organizer=organizer_profile)
#     assert event.organizer == organizer_profile
#     assert event.event_name == "Conference"
#     assert str(event) == "Conference"

# @pytest.mark.django_db
# def test_ticket_creation():
#     # Setup Organizer Profile and Event
#     user = User.objects.create(username="organizer_user")
#     organizer_profile = UserProfile.objects.create(user=user, type=UserProfile.TypeChoice.ORGANIZER)
#     event = Events.objects.create(event_name="Concert", date="2024-12-10 18:00", venue="Stadium", organizer=organizer_profile)

#     # Create a Ticket
#     ticket = Tickets.objects.create(event=event, ticket_type=Tickets.TypeChoice.Gold, price=100, quantity=10)
#     assert ticket.event == event
#     assert ticket.ticket_type == "GLD"
#     assert str(ticket) == "GLD"

# @pytest.mark.django_db
# def test_ticket_unique_constraint():
#     # Setup Organizer Profile and Event
#     user = User.objects.create(username="organizer_user")
#     organizer_profile = UserProfile.objects.create(user=user, type=UserProfile.TypeChoice.ORGANIZER)
#     event = Events.objects.create(event_name="Festival", date="2024-12-20 19:00", venue="Arena", organizer=organizer_profile)

#     # Create two tickets of the same type for the same event
#     Tickets.objects.create(event=event, ticket_type=Tickets.TypeChoice.VIP, price=200, quantity=5)
    
#     with pytest.raises(IntegrityError):
#         # This should raise an IntegrityError because of the unique constraint
#         Tickets.objects.create(event=event, ticket_type=Tickets.TypeChoice.VIP, price=250, quantity=5)

# @pytest.mark.django_db
# def test_booking_creation():
#     # Setup Organizer Profile, Event, and Ticket
#     organizer_user = User.objects.create(username="organizer_user")
#     organizer_profile = UserProfile.objects.create(user=organizer_user, type=UserProfile.TypeChoice.ORGANIZER)
#     event = Events.objects.create(event_name="Gala", date="2024-11-10 20:00", venue="Ballroom", organizer=organizer_profile)
#     ticket = Tickets.objects.create(event=event, ticket_type=Tickets.TypeChoice.Normal, price=50, quantity=100)

#     # Setup Visitor Profile for Booking
#     visitor_user = User.objects.create(username="visitor_user")
#     visitor_profile = UserProfile.objects.create(user=visitor_user, type=UserProfile.TypeChoice.VISITOR)

#     # Create a Booking
#     booking = Booking.objects.create(booked_by=visitor_profile, event_booked=event, ticket_booked=ticket)
#     assert booking.booked_by == visitor_profile
#     assert booking.event_booked == event
#     assert booking.ticket_booked == ticket
#     assert str(booking) == f"Booking by {visitor_profile} for {event}"

# @pytest.mark.django_db
# def test_booking_unique_constraint():
#     # Setup Organizer Profile, Event, and Ticket
#     organizer_user = User.objects.create(username="organizer_user")
#     organizer_profile = UserProfile.objects.create(user=organizer_user, type=UserProfile.TypeChoice.ORGANIZER)
#     event = Events.objects.create(event_name="Expo", date="2024-12-01 15:00", venue="Expo Center", organizer=organizer_profile)
#     ticket = Tickets.objects.create(event=event, ticket_type=Tickets.TypeChoice.Silver, price=75, quantity=50)

#     # Setup Visitor Profile for Booking
#     visitor_user = User.objects.create(username="visitor_user")
#     visitor_profile = UserProfile.objects.create(user=visitor_user, type=UserProfile.TypeChoice.VISITOR)

#     # Create a Booking
#     Booking.objects.create(booked_by=visitor_profile, event_booked=event, ticket_booked=ticket)

#     # Attempt to create a duplicate booking
#     with pytest.raises(IntegrityError):
#         Booking.objects.create(booked_by=visitor_profile, event_booked=event, ticket_booked=ticket)
