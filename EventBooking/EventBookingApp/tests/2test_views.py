import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status
from EventBookingApp.models import *

def test_home_view():
    client=Client()

    url=reverse('home')    
    response=client.get(url)

    assert response.status_code==200
    assert response.content.decode()=="HomePage"


@pytest.mark.django_db
def test_register_view():
    

    data = {
    "user": {
        "username": "organiser_11",
        "email": "organizer11@gmail.com",
        "password": "password123"
    },
    "type": "ORG",
    "contact_num": "9876766876"
}
    client=Client()
    url=reverse('register-nested-serializer')

    response=client.post(url,data,format='json')
    print("****************",response)

    if response.status_code != status.HTTP_201_CREATED:
        print("Error response:", response.data)

    assert response.status_code!=status.HTTP_201_CREATED
