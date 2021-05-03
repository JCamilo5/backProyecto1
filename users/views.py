from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import HttpResponse

from profiles.models import UserProfile
from .tokens import account_activation_token
from django.conf import settings


def signup(self):
    user = self
    current_site = 'localhost:8080'
    email_body = {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.email)),
        'token': account_activation_token.make_token(user),
    }
    link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = 'Activate your account'
    activate_url = 'http://127.0.0.1:8000'+link
    email = EmailMessage(
        email_subject,
        'Hi '+user.email + ', Please the link below to activate your account \n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()
    return HttpResponse('Please confirm your email address to complete the registration') 

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserProfile.objects.get(email = uid)
        user.is_active = True
        user.save()
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    return redirect('http://localhost:8080/login')
    '''
    if user is not None and default_token_generator.check_token(user, token):
        
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('')
    '''
