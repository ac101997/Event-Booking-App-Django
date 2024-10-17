from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    class TypeChoice(models.TextChoices):
        VISITOR='VI','VISITOR'
        ORGANIZER='ORG','ORGANIZER'

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    type=models.CharField(max_length=3,choices=TypeChoice.choices)
    contact_num=models.PositiveBigIntegerField(default=None,null=True)

    def __str__(self):
        return self.type


# class Customer(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True,max_length=100)
#     user_type=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='user_type')

#     def __str__(self):
#         return self.name

# class Organizer(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.EmailField(unique=True,max_length=100)
#     organizer_profile=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='organizer_profile')

#     #events_organised=Reverse Foreignkey(events)

#     def __str__(self):
#         return self.name
    

class Events(models.Model):
    event_name=models.CharField(unique=True, max_length=100)
    date=models.DateTimeField()
    venue=models.CharField(max_length=100)
    organizer=models.ForeignKey(UserProfile,on_delete=models.CASCADE,limit_choices_to={'type':'ORG'},related_name='event_organizer')

    def __str__(self):
        return self.event_name


class Tickets(models.Model):
    class TypeChoice(models.TextChoices):
        Normal='NOR','NORMAL'
        Silver='SIL','SILVER'
        Gold='GLD','GOLD'
        VIP='VIP','VIP'
    event=models.ForeignKey(Events,on_delete=models.CASCADE,default=None,related_name='event_for_ticket')
    ticket_type=models.CharField(max_length=3,choices=TypeChoice.choices)
    price=models.PositiveIntegerField()
    is_available=models.BooleanField(default=False)
    quantity=models.PositiveIntegerField(default=0)

    class Meta:
        constraints=[models.UniqueConstraint(fields=['event', 'ticket_type'], name='unique-ticket')]

    def __str__(self):
        return self.ticket_type

class Booking(models.Model):
    booked_by=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='booked_by')
    event_booked=models.ForeignKey(Events,on_delete=models.CASCADE,related_name='event_booked')
    ticket_booked=models.ForeignKey(Tickets,on_delete=models.CASCADE,related_name='ticket_booked')

    class Meta:
        constraints=[models.UniqueConstraint(fields=['event_booked', 'ticket_booked'], name='unique-booking')]
    def __str__(self):
            return f"Booking by {self.booked_by} for {self.event_booked}"
