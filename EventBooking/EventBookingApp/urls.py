from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter



router=DefaultRouter()
router.register(r'events',EventViewset,basename='events')
router.register(r'tickets',TicketsViewset,basename='tickets')
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'userprofile',UserProfileViewset,basename='user-profile')
router.register(r'viewset_register',RegisterViewSet,basename='viewset-user-profile')




urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('api/',include(router.urls)),
]
