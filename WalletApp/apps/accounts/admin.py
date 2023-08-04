from django.contrib import admin
from .models import UserProfile,User,OneTimeCode

list_display = ['user', 'first_name', 'last_name']
admin.site.register(UserProfile,list_display=list_display)
admin.site.register(User,list_display=['email'])
admin.site.register(OneTimeCode, list_display=['user'])
# Register your models here.
