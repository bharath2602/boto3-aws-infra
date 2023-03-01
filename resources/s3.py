import boto3
import colorama

# Initialize colorama module
colorama.init()

# Define colors
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


class s3:
    def create_service(Properties):
        s3 = boto3.resource("s3")
        if s3.Bucket(Properties["Name"]).creation_date:
            print(RED + "Bucket Already Exists" + RESET)
        else:
            try:
                print("Creating Bucket ....")
                s3.create_bucket(Bucket=Properties["Name"].lower())
                print(GREEN + "Bucket Created Successfully ..." + RESET)

            except Exception as e:
                print(e)
                print(RED + "Bucket Creation Failed" + RESET)
