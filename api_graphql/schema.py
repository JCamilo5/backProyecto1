from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .data.order.types import OrderNode
from .data.client.types import ClientNode
from .data.courier.types import CourierNode
from .data.product.types import ProductNode
from .data.delivery.types import DeliveryNode
from .data.enterprise.types import EnterpriseNode
from api_graphql.data.client.mutations import CreateClient, UpdateClient, DeleteClient
from api_graphql.data.enterprise.mutations import CreateEnterprise, UpdateEnterprise, DeleteEnterprise

# Schema definition


class Query(ObjectType):
    """Endpoint para consultar registros"""
    delivery = Node.Field(DeliveryNode)
    courier = Node.Field(CourierNode)
    cllient = Node.Field(ClientNode)
    enterprise = Node.Field(EnterpriseNode)
    order = Node.Field(OrderNode)
    product = Node.Field(ProductNode)
    all_deliveries = DjangoFilterConnectionField(DeliveryNode)
    all_couriers = DjangoFilterConnectionField(CourierNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
    all_enterprises = DjangoFilterConnectionField(EnterpriseNode)
    all_orders = DjangoFilterConnectionField(OrderNode)
    all_products = DjangoFilterConnectionField(ProductNode)


class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""
    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    delete_client = DeleteClient.Field()

    create_enterprise = CreateEnterprise.Field()
    update_enterprise = UpdateEnterprise.Field()
    delete_enterprise = DeleteEnterprise.Field()