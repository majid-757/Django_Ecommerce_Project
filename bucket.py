import boto3
from django.conf import settings




class Bucket:
    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name = settings.AWS_SERVICE_NAME,
        )





