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
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse


from .tokens import account_activation_token
from django.conf import settings


def signup(self):
    print("-------------Entro")
    #UserModel=settings.AUTH_USER_MODEL
    user = self
    current_site = 'localhost:8080'
    email_body = {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    print(current_site)
    link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = 'Activate your account'

    activate_url = 'http://'+current_site+link

    email = EmailMessage(
        email_subject,
        'Hi '+user.email + ', Please the link below to activate your account \n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()
    print("-------------Mensaje enviado")
    #return HttpResponse('Please confirm your email address to complete the registration') 

class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            UserModel=settings.AUTH_USER_MODEL
            user =  UserModel._default_manager.get(pk=id)
            if not account_activation_token.check_token(user, token):
                return redirect('http://localhost:8080/login',+'?message='+'User already activated')

            if user.is_active:
                user.is_active = True
                user.save()
                return redirect('http://localhost:8080/login')

            messages.success(request, 'Account activated successfully')
            return redirect('http://localhost:8080/login')

        except Exception as ex:
            pass

        return redirect('http://localhost:8080/login')
