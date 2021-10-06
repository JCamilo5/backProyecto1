from graphene import ObjectType
from graphene.relay import Node
import graphene
import graphql
import graphql_jwt
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt.mutations import Verify


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
from .data.review.types import ReviewNode
from .data.image.types import ImageNode
from .data.report.report import Reports, get_data_report, get_query_report
from .data.enterprise.mutations import (
    CreateEnterprise,
    UpdateEnterprise,
    DeleteEnterprise
)
from .data.client.mutations import (
    CreateClient,
    UpdateClient,
    RememberPasswordClient,
    ActivateClient
)
from .data.courier.mutations import (
    CreateCourier,
    UpdateCourier
)
from .data.contact.mutations import (
    CreateContact,
    UpdateContact
)

from .data.detail.mutations import (
    CreateDetail,
    UpdateDetail,
    DeleteDetail
)
from .data.order.mutations import(
    CreateOrder,
    UpdateOrder,
    DeleteOrder
)
from .data.review.mutations import(
    CreateReview,
    UpdateReview
)
from .data.product.mutations import (
    CreateProduct,
    UpdateProduct,
    DeleteProduct
)
from .data.image.mutations import (
    CreateImage,
    UpdateImage
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
    review = Node.Field(ReviewNode)
    image = Node.Field(ImageNode)

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
    all_reviews = DjangoFilterConnectionField(ReviewNode)
    all_images = DjangoFilterConnectionField(ImageNode)

    reports = graphene.Field(Reports, enterprise=graphene.String(), start_date=graphene.DateTime(), final_date=graphene.DateTime())
    def resolve_reports(self, info: graphql.ResolveInfo,enterprise,start_date,final_date):
        query_reports= get_query_report(enterprise,start_date,final_date)
        object_reports= get_data_report(query_reports,start_date,final_date)
        return object_reports

class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""
    
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    create_enterprise = CreateEnterprise.Field()
    update_enterprise = UpdateEnterprise.Field()
    delete_enterprise = DeleteEnterprise.Field()

    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()
    remember_client = RememberPasswordClient.Field()
    activate_client = ActivateClient.Field()

    create_courier = CreateCourier.Field()
    update_courier = UpdateCourier.Field()

    create_contact = CreateContact.Field()
    update_contact = UpdateContact.Field()

    create_detail = CreateDetail.Field()
    update_detail = UpdateDetail.Field()
    delete_detail = DeleteDetail.Field()

    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()

    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    
    
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

    create_image = CreateImage.Field()
    update_image = UpdateImage.Field()
