from rest_framework import serializers
from EventBookingApp.models import *
from django.core.exceptions import ValidationError


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Events
        fields='__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tickets
        fields='__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields=['id','booked_by','event_booked','ticket_booked']

    def create(self,validated_data):
        ticket=validated_data['ticket_booked']
        ticket.quantity-=1
        ticket.save()
        return Booking.objects.create(**validated_data)
    
    def validate(self,data):
        ticket=data['ticket_booked']
        event=data['event_booked']
        if ticket.event!= event:
            raise serializers.ValidationError("This ticket does not belong to the specified event")
        
        if ticket.is_available ==False:
            raise serializers.ValidationError("No ticket available (Already Booked)")
        
        return data



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={'password':{'write_only':True}}

    #override the create function to make extra modification in how the entry is being created.
    def create(self,validated_data):
        password=validated_data['password']
        user=User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    

    # def create(self,validated_data):
    #     user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
    #     user.set_password(validated_data['password'])
    #     user.save()

    #     return user


class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model=UserProfile
        fields='__all__'


    def create(self,validated_data):

        user_data=validated_data.pop('user')                               #pop the user data from the request recieved
        #profile_data=validated_data.pop('profile')
        #user=UserSerializer().create(user_data)
        user=User.objects.create_user(**user_data)                          #create the user with the user data.
        user.set_password(user_data['password'])
        profile=UserProfile.objects.create(user=user,**validated_data)      #Give reference to the user just created(will be used for permission)
        return profile


    #override this method to show customised response to user.
    def to_representation(self,instance):
        data=super().to_representation(instance)
        username=data['user']['username']
        email=data['user']['email']
        # Return a properly formatted dictionary
        return {
            'message': f'Thank you {username}, your {email} is registered with us.'
        }


    # def create(self,validated_data):
    #     user_data=validated_data['user']
    #     user_table=User.create(user_data)


    # def create(self,validated_data):
    #     user_data=validated_data.pop('user')
    #     user=UserSerializer.create(UserSerializer(),validated_data=user_data)

    #     user_profile=UserProfile.objects.create(user=user,**validated_data,contact_num=validated_data['contact_num'])
    #     return user_profile