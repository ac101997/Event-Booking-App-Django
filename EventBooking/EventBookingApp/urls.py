from django.urls import path,include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import  views



router=DefaultRouter()
router.register(r'events',EventViewset,basename='events')
router.register(r'tickets',TicketsViewset,basename='tickets')
router.register(r'booking',BookingViewset,basename='booking')
router.register(r'userprofile',UserProfileViewset,basename='user-profile')
router.register(r'viewset_register',RegisterViewSet,basename='viewset-user-profile')
router.register(r'booking_viewset',BookingViewset,basename='viewset-booking')



urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/',RegisterView.as_view(),name='register'),
    path('registernested/',RegisterViewNested.as_view(),name='register-nested-serializer'),
    path('api/',include(router.urls)),
    path('api_token_auth/',views.obtain_auth_token,name='api_token_auth'),
    path('api/filter/',SearchFeature.as_view(),name='search-feature'),
]
