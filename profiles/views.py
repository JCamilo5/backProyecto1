from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


from .tokens import account_activation_token
from django.conf import settings


def signup(request, id):
    print("-------------Entro")
    UserModel=settings.AUTH_USER_MODEL
    user = UserModel
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    message = render_to_string('profiles/acc_active_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
    print("-------------Mensaje enviado")
    #return HttpResponse('Please confirm your email address to complete the registration') 
