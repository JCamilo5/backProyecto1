from graphene import ObjectType
from graphene.relay import Node

from graphene_django.filter import DjangoFilterConnectionField

from .data.user.types import UserNode
from .data.order.types import OrderNode
from .data.client.types import ClientNode
from .data.detail.types import DetailNode
from .data.contact.types import ContactNode
from .data.payment.types import PaymentNode
from .data.courier.types import CourierNode
from .data.product.types import ProductNode
from .data.manager.types import ManagerNode
from .data.delivery.types import DeliveryNode
from .data.enterprise.types import EnterpriseNode
from .data.management.types import ManagementNode
from .data.enterprise.mutations import (
    CreateEnterprise,
    UpdateEnterprise,
    DeleteEnterprise
)
from .data.client.mutations import (
    CreateClient,
    UpdateClient,
    RememberPasswordClient
)
from .data.contact.mutations import (
    CreateContact,
    UpdateContact
)


# Schema definition


class Query(ObjectType):
    """Endpoint para consultar registros"""

    delivery = Node.Field(DeliveryNode)
    courier = Node.Field(CourierNode)
    client = Node.Field(ClientNode)
    contact = Node.Field(ContactNode)
    enterprise = Node.Field(EnterpriseNode)
    order = Node.Field(OrderNode)
    product = Node.Field(ProductNode)
    manager = Node.Field(ManagerNode)
    detail = Node.Field(DetailNode)
    user = Node.Field(UserNode)
    management = Node.Field(ManagementNode)
    payment = Node.Field(PaymentNode) 
    
    all_deliveries = DjangoFilterConnectionField(DeliveryNode)
    all_couriers = DjangoFilterConnectionField(CourierNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
    all_contacts = DjangoFilterConnectionField(ContactNode)
    all_enterprises = DjangoFilterConnectionField(EnterpriseNode)
    all_orders = DjangoFilterConnectionField(OrderNode)
    all_products = DjangoFilterConnectionField(ProductNode)
    all_managers = DjangoFilterConnectionField(ManagerNode)
    all_details = DjangoFilterConnectionField(DetailNode)
    all_users = DjangoFilterConnectionField(UserNode)
    all_management = DjangoFilterConnectionField(ManagementNode)
    all_payments = DjangoFilterConnectionField(PaymentNode) 


class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_enterprise = CreateEnterprise.Field()
    update_enterprise = UpdateEnterprise.Field()
    delete_enterprise = DeleteEnterprise.Field()

    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    remember_client = RememberPasswordClient.Field()
    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()
    