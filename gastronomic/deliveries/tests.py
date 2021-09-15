from django.test import TestCase
from .models import Delivery
from users.models import Courier ,Client
from  orders.models import Order
from  products.models import Product
from enterprises.models import Enterprise
# Create your tests here.
# status: revisar el cambio del estado
# delivery_time: verificar que exista un dato

class testModelDelivery(TestCase):
    def setUp(self):
       
        self.courier= Courier.objects.create(email="test@local.com",type="COURIER", is_staff=False)
        client = Client.objects.create(
            email="example@gmail.com",
            type="Client"
        )
        self.order= Order.objects.create(status=True, estimated_time="5",location="prueba",client_id=client.id)
       
        self.delivery= Delivery.objects.create(status=True,courier_id=self.courier.id, order_id=self.order.id)
        
        return super().setUp()

    def test_model_Delivery(self):
        """La hora de entrega debe ser diferente de nulo"""
        self.assertNotEqual(self.delivery.delivery_time,'null')

    def test_id_Order(self):
        """La entrega debe tener una relacion con una orden de pedido"""
        self.assertNotEqual(self.delivery.order_id,'null')

    def test_id_courier(self):
        """la entrega debe tener asociado un cliente"""
        self.assertNotEqual(self.delivery.courier_id,'null')

  

 
    
    