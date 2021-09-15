
import graphene
class Report(graphene.ObjectType):
    enterprise= graphene.String()       
    report_date = graphene.DateTime()
    payment_value = graphene.Int()
