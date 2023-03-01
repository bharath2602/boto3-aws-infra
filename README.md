# BOTO#-AWS-INFRA

Python based project for provisioning basic aws infrastructure

## Getting started
1. Clone the repository
2. Export aws credentials to your terminal
3. Find the sample [resource.yaml](resource.yaml) file and fill out the required resources with its parameters

```
python3 resources/main.py
```

# Functionality
1. Connects to the provided aws credentials and use boto3 apis
2.  Creates the resources mentioned on the template using python class
