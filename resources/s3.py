import boto3
from colorama import Fore

class s3:
    def create_service(Properties):
        s3 = boto3.resource('s3')
        if s3.Bucket(Properties['Name']).creation_date:
            print(Fore.RED +"Bucket Already Exists")
        else:
            try:
                print("Creating Bucket ....")
                s3.create_bucket(Bucket=Properties['Name'].lower())
                print(Fore.GREEN +'Bucket Created Successfully ...')
                
            except Exception as e:
               print(Fore.RED+e)
      