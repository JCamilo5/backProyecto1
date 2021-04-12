from enterprises.models import Enterprise
from django.db import models

from orders.models import Order
from payments.models import Payment

# Create your models here.


class Delivery(models.Model):
    """Clase Entrega"""
    status = models.BooleanField(default=False, help_text='estado')
    delivery_time = models.DateTimeField(auto_now_add=True, help_text='hora entrega')

    class Meta:
        verbose_name_plural = 'deliveries'

    # Relaciones
    courier = models.ForeignKey(
        'Courier',
        related_name='deliveries',
        on_delete=models.CASCADE,
        help_text='mensajero'
    )
    order = models.OneToOneField(
        Order,
        related_name='delivery',
        on_delete=models.CASCADE,
        help_text='orden de pedido'
    )
    payment = models.OneToOneField(
        Payment,
        related_name='delivery',
        on_delete=models.CASCADE,
        help_text='pago'
    )

    def __str__(self) -> str:
        return self.status


class Courier(models.Model):
    """Clase Mensajero"""
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    telephone = models.CharField(max_length=15)

    enterprise = models.ForeignKey(
        Enterprise,
        related_name='couriers',
        on_delete=models.CASCADE,
        help_text='establecimiento'
    )

    def __str__(self) -> str:
        return self.name
