import boto3
from colorama import Fore

class vpc:
    sub_id =[]
    def create_service(Properties):
        type = boto3.resource('ec2')
        try:
            print("Creating VPC ....")

            vpc_meta = type.create_vpc(CidrBlock=Properties['CIDR'])
            vpc_meta.create_tags(Tags=[{"Key": "Name", "Value": Properties["Name"]}])
            vpc_meta.wait_until_available()

            ec2Client = boto3.client('ec2')
            ec2Client.modify_vpc_attribute( VpcId = vpc_meta.id , EnableDnsSupport = { 'Value': True } )
            ec2Client.modify_vpc_attribute( VpcId = vpc_meta.id , EnableDnsHostnames = { 'Value': True } )

            if (Properties.get("IGW",False)):
                internetgateway = type.create_internet_gateway()
                vpc_meta.attach_internet_gateway(InternetGatewayId=internetgateway.id)

            for sub in Properties['Subnet']:
                routetable = vpc_meta.create_route_table()
                subnet = type.create_subnet(CidrBlock=sub['CIDR'], VpcId=vpc_meta.id)
                if sub['Public']:
                    routetable.create_route(DestinationCidrBlock='0.0.0.0/0', GatewayId=internetgateway.id)
                routetable.create_tags(Tags=[{"Key": "Name", "Value": sub["Name"]}])
                vpc.sub_id.append({"id":subnet.id,"name":sub['Name']})
                routetable.associate_with_subnet(SubnetId=subnet.id)      

            print(Fore.GREEN + "VPC Created Successfully ..") 

        except Exception as e:
            print(Fore.RED +e)         


