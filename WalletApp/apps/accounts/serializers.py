from rest_framework import serializers
from .models import UserProfile
import re

def get_ip(request):
    x_forwarded_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_address:
        ip_addr = x_forwarded_address.split(',')[0]
        return ip_addr
    return request.META.get('REMOTE_ADDR')

class UserProfileCreationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name', 'mobile_number']

    def validate_mobile_number(self,attrs):
        pattern = r'^\+?\d*234\d{9,10}$'
        if re.match(pattern, attrs) is None:
            raise serializers.ValidationError('Invalid mobile number')
        return attrs
        
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        print(user)
        ip_addr = get_ip(request)
        queryset = self.Meta.model(**validated_data)
        queryset.user = user
        queryset.ip_address = ip_addr
        queryset.save()
        return queryset
    
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        models = UserProfile
        fields = '__all__'