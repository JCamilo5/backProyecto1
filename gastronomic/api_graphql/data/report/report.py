import graphene

import graphql
import datetime
from datetime import datetime
from datetime import timedelta
from payments.models import Payment

class Report(graphene.ObjectType):   
    report_date = graphene.String()
    payment_value = graphene.Int()

class Reports(graphene.ObjectType):
    enterprise= graphene.String()       
    report_type = graphene.Int()
    report_list = graphene.List(Report)
    total_value = graphene.Float()


