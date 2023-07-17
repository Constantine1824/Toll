from rest_framework.views import APIView
from .serializers import UserProfileCreationSerializer,UserProfileSerializer
from .models import UserProfile,User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated

class CreateUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = UserProfileCreationSerializer
        data = request.data
        serializer = serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = UserProfileSerializer
        user_obj = request.user
        profile = UserProfile.objects.get(user=user_obj)
        serializer = serializer(profile)
        return Response(serializer.data,status=status.HTTP_200_OK)