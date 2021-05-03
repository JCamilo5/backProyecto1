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
#import api_graphql.data.client.types 
#import users.models 

from .tokens import account_activation_token
from django.conf import settings
'''
def signup(self):
    user =self
    mail_subject = 'Activate your account.'
    current_site = 'localhost:8080'
    message = render_to_string('users/acc_active_email.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    #to_email = form.cleaned_data.get('email')
    to_email= self.email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
    #return HttpResponse('Please confirm your email address to complete the registration')    
'''

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
    print("-------------Mensaje enviado")
    return HttpResponse('Please confirm your email address to complete the registration') 

def activate(request, uidb64, token):
    print("-----Entro a activate---")
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        User=settings.AUTH_USER_MODEL
        user = Client.objects.get(pk=uid)
        #user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

'''class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            UserModel=settings.AUTH_USER_MODEL
            user =  UserModel._default_manager.get(pk=id)
            if not account_activation_token.check_token(user, token):
                return redirect('http://localhost:8080/login',+'?message='+'User already activated')

            if not user.is_active:
                user.is_active = True
                user.save()
                return redirect('http://localhost:8080/login')

            messages.success(request, 'Account activated successfully')
            return redirect('http://localhost:8080/login')

        except Exception as ex:
            pass

        return redirect('http://localhost:8080/login')
'''
