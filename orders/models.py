from django.db.models import (
    Model,
    DateTimeField,
    PositiveSmallIntegerField,
    CharField,
    ForeignKey,
    ManyToManyField,
    CASCADE
)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from products.models import Product
from users.models import Client
from .choices import STATUS_CHOICES, NEW

# Create your models here.


class Order(Model):
    """"Clase que representa una Orden de Pedido"""

    date = DateTimeField(auto_now_add=True, help_text='fecha')
    status = CharField(max_length=15, choices=STATUS_CHOICES, default=NEW, help_text='estado')
    estimated_time = PositiveSmallIntegerField(help_text='tiempo estimado')
    location = CharField(max_length=250, help_text='ubicación')

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

    def clean(self) -> None:
        if self.quantity == 0:
            raise ValidationError(_('No se puede guardar 0'))
        return super().clean()

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """

        return str(self.quantity)

class Report(Model):
    """
    Clase que representa el los informes de
    los Pedidos
    """

    id_interprise = CharField(max_length=250, help_text='id interprise')
    report_type = CharField(max_length=250, help_text='tipo de reporte')
    report_information = CharField(max_length=250, help_text='report_information')
