from rest_framework import serializers
from EventBookingApp.models import *



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
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()

    class Meta:
        model=UserProfile
        fields='__all__'

    def create(self,validated_data):
        user_data=validated_data.pop('user')
        user=UserSerializer.create(UserSerializer(),validated_data=user_data)

        user_profile=UserProfile.objects.create(user=user,**validated_data,contact_num=validated_data['contact_num'])
        return user_profile