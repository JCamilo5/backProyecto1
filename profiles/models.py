from django.db.models import (
    TextChoices,
    EmailField,
    CharField,
    BooleanField,
    ForeignKey,
    CASCADE
)
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
#from django.http import request



# Create your models here.


class UserProfileManager(BaseUserManager):
    """Administrador para perfiles de Usuario"""

    def create_user(self, email: str, password: str) -> User:
        """Crea un nuevo usuario"""

        if not email:
            raise ValueError('User must have an email address')
        print("-----------------Antes de guardar usuarios")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)     
        return user

    def create_superuser(self, email: str, password: str) -> User:
        """Crea un nuevo superusuario"""

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Clase que representa a los Usuarios en el sistema"""

    class Types(TextChoices):
        CLIENT = "CLIENT", "Client"
        MANAGER = "MANAGER", "Manager"
        COURIER = "COURIER", "Courier"

    email = EmailField(max_length=45, unique=True)
    type = CharField(
        max_length=7,
        choices=Types.choices,
        null=True,
        blank=True,
        help_text='tipo de usuario'
    )
    is_active = BooleanField(
        default=False,
        help_text='usuario activo'
    )
    is_staff = BooleanField(
        default=False,
        help_text='personal de administrador de Django'
    )

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    # Relaciones
    enterprise = ForeignKey(
        'enterprises.Enterprise',
        related_name='couriers',
        on_delete=CASCADE,
        null=True,
        blank=True,
        help_text='establecimiento'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.email
