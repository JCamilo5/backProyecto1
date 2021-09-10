from graphene import InputObjectType
from graphene.types.scalars import Int
from graphene.types.scalars import ID
from graphene.types.scalars import String
from graphene.types.scalars import Boolean

# Create your inputs here


class CreateReportInput(InputObjectType):
    
    id_interprise = String(Required=True)
    report_type = String(Required= True)
    report_information = String()
    

    # relaciones

    

