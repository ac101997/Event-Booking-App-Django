from django.contrib import admin
from EventBookingApp.models import *

# Register your models here.

@admin.register(UserProfile)
class UserProfileClass(admin.ModelAdmin):
    list_display=['id','user','type','contact_num']


# @admin.register(Customer)
# class CustomerClass(admin.ModelAdmin):
#     list_display=['id','name','email','user_type']


# @admin.register(Organizer)
# class OrganizerClass(admin.ModelAdmin):
#     list_display=['id','name','email','organizer_profile']


@admin.register(Events)
class EventClass(admin.ModelAdmin):
    list_display=['id','event_name','date','venue','organizer']


@admin.register(Tickets)
class TicketsClass(admin.ModelAdmin):
    list_display=['id','event','ticket_type','price','is_available','quantity']


@admin.register(Booking)
class BookingClass(admin.ModelAdmin):
    list_display=['id','booked_by','event_booked','ticket_booked']