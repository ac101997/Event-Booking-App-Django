from EventBookingApp.models import *

def orm():
    query=Tickets.objects.select_related('event')
    return query