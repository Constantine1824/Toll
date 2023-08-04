from twilio.rest import Client
from django.conf import settings

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN



def send_sms(client_phone_number, token):
    phone_no = settings.PHONE_NUMBER
    try:
        client = Client(account_sid, auth_token)
        resp = client.messages.create(
        from_=phone_no,
        to= client_phone_number,
        body = f'{token} is your toll number verification token. This token will expire in 30 minutes \
        From the Toll Team\
        '
    )
    except Exception as e:
        print(e)