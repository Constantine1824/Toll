from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, OneTimeCode
from .SMS_helper import send_sms

@receiver(post_save, sender=UserProfile)
def send_confirmation_sms(sender, instance,created):
    if created:
        code = OneTimeCode.objects.create(user=instance.user).generate_random_code()
        send_sms(client_phone_number=instance.phone_no,token=code)