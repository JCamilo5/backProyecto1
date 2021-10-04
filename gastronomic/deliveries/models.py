from django.db.models import (
    Model,
    BooleanField,
    DateTimeField,
    ForeignKey,
    OneToOneField,
    CASCADE
)

from orders.models import Order
from users.models import Courier

# Create your models here.


class Delivery(Model):
    """Clase que representa una Entrega"""

    status = BooleanField(default=False, help_text='estado')
    delivery_time = DateTimeField(auto_now_add=True, help_text='hora entrega')

    class Meta:
        verbose_name_plural = 'deliveries'

    # Relaciones
    courier = ForeignKey(
        Courier,
        related_name='deliveries',
        on_delete=CASCADE,
        help_text='mensajero'
    )
    order = OneToOneField(
        Order,
        related_name='delivery',
        on_delete=CASCADE,
        help_text='orden de pedido'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return self.delivery_time.strftime('%a %H:%M  %d/%m/%y')
