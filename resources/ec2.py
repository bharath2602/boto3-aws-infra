import boto3
from vpc import *
import colorama

# Initialize colorama module
colorama.init()

# Define colors
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


class ec2:
    def create_service(prop):
        type = boto3.resource("ec2")
        try:
            subnet_id = ""
            if prop["Subnet_id"]:
                if "." in prop["Subnet_id"]:
                    name = prop["Subnet_id"].split(".")
                    for sub in vpc.sub_id:
                        if sub["name"] == name:
                            subnet_id = sub["id"]
                else:
                    subnet_id = prop["Subnet_id"]
            else:
                subnet_id = "subnet-066d02b07194da41c"

            print("Creating instance ...")
            instances = type.create_instances(
                ImageId=prop["Image"],
                InstanceType=prop["Type"],
                MaxCount=1,
                MinCount=1,
                NetworkInterfaces=[
                    {
                        "SubnetId": subnet_id,
                        "DeviceIndex": 0,
                        "AssociatePublicIpAddress": True,
                    }
                ],
                KeyName=prop["Key"],
            )
            type.create_tags(
                Resources=[instances[0].id],
                Tags=[{"Key": "Name", "Value": prop["Name"]}],
            )

            print(GREEN + "Instance Created successfully ..." + RESET)
        except Exception as e:
                print(e)
                print(RED + "Instance Creation Failed" + RESET)
