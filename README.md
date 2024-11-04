# BOTO3-AWS-INFRA

Python based project for provisioning basic aws infrastructure

- **repoURL**: The source repository where the Helm charts are stored
  > [!NOTE]
  > Standard customers cannot modify the `repoURL`. Only premium customers can use custom registries to publish and deploy their own integrations.
- **chart**: A unique chart name(api-name) used in the configurations
- **targetRevision**: Defines the specific chart version to deploy.
- **releaseName**: A unique release name for each version you deploy.
- **valueFiles**: File paths for values, which should not be altered.

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
