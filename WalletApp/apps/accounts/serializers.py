from rest_framework.serializers import ModelSerializer
from .models import UserProfile

def get_ip(request):
    x_forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_address:
        ip_addr = x_forwarded_address.split(',')[0]
        return ip_addr
    return request.META.get('REMOTE_ADDR')

class UserProfileCreationSerializer(ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        print(user)
        ip_addr = get_ip(request)
        queryset = self.Meta.model(**validated_data)
        queryset.user = user
        queryset.ip_address = ip_addr
        queryset.save()
        return queryset
    
class UserProfileSerializer(ModelSerializer):

    class Meta:
        models = UserProfile
        fields = '__all__'