from django.urls import path
from .views import CreateUserProfileAPIView,UserProfileAPIView, Verify_PhoneAPIView, ActivateUserAPIView

urlpatterns = [
    path('create',CreateUserProfileAPIView.as_view(),name='create-profile'),
    path('',UserProfileAPIView.as_view(), name='profile-view'),
    path('verify-phone',Verify_PhoneAPIView.as_view(),name='verify phone'),
    path('activate/<uid>/<token>', ActivateUserAPIView.as_view({'get':'activation'}), name='activate-user')
]
