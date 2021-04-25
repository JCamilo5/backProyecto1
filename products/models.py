from django.db.models import (
    Model,
    CharField,
    PositiveBigIntegerField,
    PositiveSmallIntegerField,
    TextField,
    ImageField,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)

from enterprises.models import Enterprise

# Create your models here.


class Product(Model):
    """Clase que representa un Producto"""

    name = CharField(max_length=45, help_text='nombre')
    price = PositiveBigIntegerField(help_text='precio')
    ingredients = TextField(help_text='ingredientes')
    preparation = TextField(null=True, blank=True, help_text='preparación')
    estimated_time = PositiveSmallIntegerField(help_text='tiempo estimado')

    # Relaciones
    enterprise = ForeignKey(
        Enterprise,
        related_name='products',
        on_delete=CASCADE,
        help_text='establecimiento'
    )
    accompaniments = ManyToManyField(
        'self',
        blank=True,
        related_name='products',
        help_text='acompañamientos'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.name


class Image(Model):
    """Clase que representa una Imagen"""

    url = ImageField(upload_to='uploads/images')

    # Relaciones
    product = ForeignKey(
        'Product',
        related_name='images',
        on_delete=CASCADE,
        help_text='producto'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.url.name
