from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

from profiles.models import UserProfile
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site

#url = 'https://delivery-food-frontend.herokuapp.com'
url = 'http://localhost:8080'
@csrf_exempt
def signup(self, request):
    user = self
    current_site = get_current_site(request)
    site = url
    print(site)
    email_body = {
        'user': user,
        'domain': site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    link = reverse('activate', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = 'Activa tu cuenta'
    activate_url = 'http://'+current_site.domain+link
    email = EmailMessage(
        email_subject,
        'Hola '+user.email + ', Por favor, dar click en el enlace para activar su cuenta \n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserProfile.objects.get(pk = uid)   
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect(url+'/login')

def remember(self, request):
    user = self
    current_site = get_current_site(request)
    site = url
    email_body = {
        'user': user,
        'domain': site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
    link = reverse('activateRe', kwargs={
                    'uidb64': email_body['uid'], 'token': email_body['token']})
    email_subject = 'Restablecer contraseña'
    activate_url = 'http://'+current_site.domain+link
    email = EmailMessage(
        email_subject,
        'Hola '+user.email + ', Por favor, dar click en el enlace para restaurar tu contraseña\n'+activate_url,
        'noreply@semycolon.com',
        [user.email],
    )
    email.send()

def activateRe(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        cad = "UserNode:"+uid
        cad = urlsafe_base64_encode(force_bytes(cad))
        cad = cad + "=="
        user = UserProfile.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, UserProfile.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        return redirect(url+'/Password/Reset'+'/'+cad)
    else:
        return redirect(url+'/login')

