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
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = 'Activa tu cuenta'
    activate_url = 'http://127.0.0.1:8000'+link
    email = EmailMessage(
        email_subject,
        'Hola '+user.email + ', Por favor, dar click en el enlace para activar su cuenta \n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()

def activate(request, uidb64, token):
    print("Token que llega", token)
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk = uid)   
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('http://localhost:8080/login')
    else:
        return redirect('')

def remember(self):
    user = self
    current_site = 'localhost:8080'
    email_body = {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.email)),
        'token': account_activation_token.make_token(user),
    }
    link = reverse('activateRe', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = ''
    activate_url = 'http://127.0.0.1:8000'+link
    email = EmailMessage(
        email_subject,
        'Hola '+user.email + ', Por favor, dar click en el enlace para restaurar tu contraseña\n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()

def activateRe(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserProfile.objects.get(email = uid)
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return redirect('http://localhost:8080/example-list')
    else:
        return redirect('http://localhost:8080/login')
