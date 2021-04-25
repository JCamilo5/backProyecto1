from django.db.models import (
    Model,
    DateTimeField,
    BooleanField,
    PositiveSmallIntegerField,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE
)

from products.models import Product
from users.models import Client

# Create your models here.


class Order(Model):
    """"Clase que representa una Orden de Pedido"""

    date = DateTimeField(auto_now_add=True, help_text='fecha')
    status = BooleanField(default=True, help_text='estado')
    estimated_time = PositiveSmallIntegerField(help_text='tiempo estimado')
    location = CharField(max_length=45, help_text='ubicación')

    # Relaciones
    client = ForeignKey(
        Client,
        related_name='orders',
        on_delete=CASCADE,
        help_text='cliente'
    )
    products = ManyToManyField(
        Product,
        related_name='orders',
        through='Detail',
        blank=True,
        help_text='productos'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.date.strftime('%a %H:%M  %d/%m/%y')


class Detail(Model):
    """
    Clase que representa el Detalle entre
    Productos y Ordenes de Pedidos
    """

    quantity = PositiveSmallIntegerField(help_text='cantidad')

    # Relaciones
    product = ForeignKey(
        Product,
        related_name='details',
        on_delete=CASCADE,
        help_text='producto'
    )
    order = ForeignKey(
        'Order',
        related_name='details',
        on_delete=CASCADE,
        help_text='order de pedido'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return str(self.quantity)
