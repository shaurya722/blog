from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth.models import User

def send_otp_via_email(email):

    subject = 'Your account verification email.'
    message = 'How are you? Hope will be fine...'
    email_from = settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    user_obj = User.objects.get(email = email)
    user_obj.save()
