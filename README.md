# BOTO3-AWS-INFRA

Python based project for provisioning basic aws infrastructure

$\color{red}{\textsf{**Note**: Below are the examples of how the kubernetes secrets should be structured. Please note that all secrets must be encrypted using SOPS, which can be done via this [link](../secrets/README.md).}}$

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
