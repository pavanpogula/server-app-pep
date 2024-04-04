import sys,os
sys.path.append(sys.path[0]+"/app/aws")
from typing import Annotated
from fastapi import Depends
from boto3 import resource
from config import Settings

settings = Settings()


# AWS_ACCESS_KEY_ID = settings.aws_secret_key_id
# AWS_SECRET_ACCESS_KEY = settings.aws_secret_access_key
# REGION_NAME = settings.region_name
 
# table_resource = resource(
#    'dynamodb',
#    aws_access_key_id     = AWS_ACCESS_KEY_ID,
#    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
#    region_name           = REGION_NAME
# )
# #To access or modify the table’s entries, we have to get the table using the resource

# user_table = table_resource.Table('user_table')

def get_items_all():
   #  response = user_table.scan()
    print(settings.aws_secret_access_key)
    return "response"