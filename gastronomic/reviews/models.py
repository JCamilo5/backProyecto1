from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    TextField,
    OneToOneField,
    CASCADE
)

from orders.models import Order
from .choices import REVIEW_CHOICES

# Create your models here.


class Review(Model):
    """Clase que representa una Valoración"""

    quality_service = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='calidad del servicio'
    )
    presentation = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='presentación'
    )
    preparation = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='preparación'
    )
    ingredients = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='ingredientes'
    )
    price = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='precio'
    )
    textures = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='texturas'
    )
    cooking_point = CharField(
        max_length=7,
        choices=REVIEW_CHOICES,
        help_text='punto de cocción'
    )
    comments = TextField(help_text='comentarios')
    date = DateTimeField(auto_now_add=True)

    # Relaciones
    order = OneToOneField(
        Order,
        related_name='review',
        on_delete=CASCADE
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.quality_service
