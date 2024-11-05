# BOTO3-AWS-INFRA

Python based project for provisioning basic aws infrastructure

# API Deployment Guide

This README provides instructions for deploying APIs and API version sets in Grand Central using Argo CD and Helm.

## Deployment Structure

- All API YAML files are stored in **`api/<api-name>.yaml`**, with each new API defined in its own file.
- Each API has a corresponding API version set, which is created in **`apiversionsets.values.yaml`**.

## Steps to Deploy a New API

1. **Define API Version Set**:
   - Open [apiversionsets.values.yaml](apiversionsets.values.yaml).
   - Add an entry for the new API’s version set, using the example provided in the same file as a reference.
   - The version set ensures that each API version can be uniquely referenced and managed.

2. **Create API YAML Configuration**:
   - Open [api](apis/) folder.
   - Create a new YAML file for the API, following the structure in `apis/generic-api.yaml`.
   - Each API should be created as an Argo CD application, with the configuration file pointing to the relevant Helm chart stored in the ACR
   - **Important Deployment Notes**

      - **repoURL**: The source repository where the Helm charts are stored
      > [!NOTE]
      > Standard customers cannot modify the `repoURL`. Only premium customers can use custom registries to publish and deploy their own integrations.
      - **chart**: A unique chart name(api-name) used in the configurations
      - **targetRevision**: Defines the specific chart version to deploy.
      - **releaseName**: A unique release name for each version you deploy.
      - **valueFiles**: File path for values, which should not be altered.

         **Example**

         ```yaml
         - repoURL: gcshared671.azurecr.io/charts
         chart: test-api
         targetRevision: 1.1.8-11347054944
         helm:
            releaseName: test-api-v1
            valueFiles:
            - $apps-live/runtimes/dev/apim/apis/common.apim.values.yaml
         ```


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
