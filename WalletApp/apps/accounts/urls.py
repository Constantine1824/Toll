from django.urls import path
from .views import CreateUserProfileAPIView,UserProfileAPIView

urlpatterns = [
    path('create',CreateUserProfileAPIView.as_view(),name='create-profile'),
    path('',UserProfileAPIView.as_view(), name='profile-view')
]
