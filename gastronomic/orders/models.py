from django.db import models

from users.models import Client
from products.models import Product

# Create your models here.


class Order(models.Model):
    """"Clase Orden de Pedido"""
    date = models.DateTimeField(auto_now_add=True, help_text='fecha')
    # TODO: revisar status = models.BooleanField(default=True, help_text='estado')
    estimated_time = models.TimeField(help_text='tiempo estimado')
    location = models.CharField(max_length=45, help_text='ubicación')

    # Relaciones
    client = models.ForeignKey(
        Client,
        related_name='orders',
        on_delete=models.CASCADE,
        help_text='cliente'
    )

    def __str__(self) -> str:
        return self.date.strftime('%a %H:%M  %d/%m/%y')


class Detail(models.Model):
    """Clase Detalle"""
    quantity = models.PositiveIntegerField(help_text='cantidad')

    # Relaciones
    product = models.ForeignKey(
        Product,
        related_name='details',
        on_delete=models.CASCADE,
        help_text='producto'
    )
    order = models.ForeignKey(
        'Order',
        related_name='details',
        on_delete=models.CASCADE,
        help_text='order de pedido'
    )
