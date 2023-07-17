from django.contrib import admin
from .models import UserProfile,User

list_display = ['user', 'first_name', 'last_name']
admin.site.register(UserProfile,list_display=list_display)
admin.site.register(User,list_display=['email'])
# Register your models here.
