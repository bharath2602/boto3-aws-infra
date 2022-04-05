import yaml
import boto3
import sys
from yaml.loader import SafeLoader
from s3 import *
from vpc import *
from ec2 import *

class Create:

    def create_resources(self,resources):
        boto3.setup_default_session(profile_name='default')
        for each_resource in resources:
            resource = each_resource['Type'].lower()
            if each_resource['Value'] == True:
                resource_obj = self.str_to_class(resource)
                obj = resource_obj
                obj.create_service(each_resource['Properties'])

    def str_to_class(self,str):
        return getattr(sys.modules[__name__], str)
   

#if __name__ == "__main__" :
with open('sample.yaml', 'r') as f:
    read_resource = yaml.load(f, Loader=SafeLoader)
obj_create = Create()
obj_create.create_resources(read_resource['Resources'])  

