from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from profiles.models import UserProfile
from django.http import HttpRequest
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.contrib.sites.shortcuts import get_current_site


from .views import signup
# Create your models here.


class ClientManager(models.Manager):
    """Clase que filtra por Usuario Cliente"""

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        """
        Función que retorna usuarios de tipo cliente
        """

        queryset = super().get_queryset(*args, **kwargs)
        users = queryset.filter(type=UserProfile.Types.CLIENT)

        return users


class Client(UserProfile):
    """
    Clase que representa un Usuario Cliente
    """

    class Meta:
        proxy = True

    objects = ClientManager()

    def save(self, *args, **kwargs) -> None:
        """Función que guarda un usuario tipo cliente"""
        
        if not self.pk:
            self.type = UserProfile.Types.CLIENT
        
        return super().save(*args, **kwargs)


class ManagerManager(models.Manager):
    """
    Clase que filtra por
    Usuario Administrador del Establecimiento
    """

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        """
        Función que retorna usuarios
        de tipo administrador del establecimiento
        """

        queryset = super().get_queryset(*args, **kwargs)
        users = queryset.filter(type=UserProfile.Types.MANAGER)

        return users


class Manager(UserProfile):
    """
    Clase que representa un
    Usuario Administrador del Establecimiento
    """

    class Meta:
        proxy = True

    objects = ManagerManager()

    def save(self, *args, **kwargs) -> None:
        """
        Función que guarda un usuario
        tipo administrador del establecimiento
        """

        if not self.pk:
            self.type = UserProfile.Types.MANAGER

        return super().save(*args, **kwargs)


class CourierManager(models.Manager):
    """Clase que filtra por Usuario Mensajero"""

    def get_queryset(self, *args, **kwargs) -> QuerySet:
        """
        Función que retorna usuarios de tipo mensajero
        """

        queryset = super().get_queryset(*args, **kwargs)
        users = queryset.filter(type=UserProfile.Types.COURIER)

        return users


class Courier(UserProfile):
    """
    Clase que representa un Usuario Mensajero
    """

    class Meta:
        proxy = True

    objects = CourierManager()

    def save(self, *args, **kwargs) -> None:
        """
        Función que guarda un Usuario Mensajero
        """

        if not self.pk:
            self.type = UserProfile.Types.COURIER
        return super().save(*args, **kwargs)


class Contact(models.Model):
    """
    Clase que representa un Contacto del Usuario
    """

    names = models.CharField(max_length=45, help_text='nombres')
    lastnames = models.CharField(max_length=45, help_text='apellidos')
    location = models.CharField(max_length=45, help_text='ubicación')
    telephone = models.CharField(max_length=15, help_text='telefono')
    license_plate = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        help_text='placa'
    )
    created = models.DateTimeField(auto_now_add=True, help_text='creado')
    updated = models.DateTimeField(auto_now=True, help_text='actualizado')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='contact',
        on_delete=models.CASCADE,
        help_text='usuario'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return '{} {}'.format(self.names, self.lastnames)
