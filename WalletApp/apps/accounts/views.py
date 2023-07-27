from rest_framework.views import APIView
from .serializers import UserProfileCreationSerializer,UserProfileSerializer
from .models import UserProfile,User,OneTimeCode
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from .SMS_helper import send_sms

class CreateUserProfileAPIView(APIView):
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

class Verify_PhoneAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """This endpoint should only be contacted when the user fails to verify the code the first time"""
        code = OneTimeCode.objects.create(user=request.user).generate_random_code()
        user_profile = UserProfile.objects.get(user=request.user)
        if user_profile.number_verified: #If the number has been verified already....... there's no need for this anymore
            raise exceptions.NotAcceptable()
        try:
            send_sms(client_phone_number=user_profile.mobile_number,token=code)
            return Response({
            'detail' : 'code sent',
            'code' : code
        })
        except Exception as e:
            return Response({
                'detail' : 'An error occured',
                'error' : e
            })

    def post(self, request):
        """This endpoint verifies the sent code/token"""
        try:
            code = request.data['code']
            try: #This will throw an error if code doesn't exist..... it's better to handle it 
                code_obj = OneTimeCode.objects.get(code=code)
                code_obj.delete()
                return Response({
                    'detail' : 'verified'
                })
            except OneTimeCode.DoesNotExist:
                return Response({
                    'detail' : 'Code does not exist'
                })
        except KeyError:
            raise exceptions.ParseError()
