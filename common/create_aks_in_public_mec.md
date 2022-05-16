#  Creating AKS clusters in Azure public MEC

## Pre-requisites
Before started, please make sure you have an allowlisted subscription to your Azure account, which allows you to deploy resources in Azure public MEC. If you don't have an active allowed subscription, contact the [Azure public MEC product team](https://aka.ms/azurepublicmec). We also recommend to review [key concepts for Azure public MEC Preview](https://docs.microsoft.com/en-us/azure/public-multi-access-edge-compute-mec/key-concepts) before moving on. 

To create test AKS clusters on the public MEC, you can either use Azure CLI or ARM templates to deploy your cluster in a subscription. 

## Deploying AKS using Azure CLI
You can create a cluster on the public MEC using the following commands:

Login using your credentials
```
az login
```

Set the subscription you want to create the cluster on
```
az account set --subscription <subscription_name/subscription_id>
```

Use the command below to create a cluster on the public MEC
```
az aks create -g <resource_group_name> -n <cluster_name> --kubernetes-version 1.22.4 --edge-zone <edge_zone_name> --location <edge_zone_location> --max-pods 110 --node-count 1 --node-vm-size Standard_NC4asT4_v3 --enable-addons monitoring
```

Sample command:
```
az aks create -g evslab000 -n evslab000-aks-cluster-cli --kubernetes-version 1.22.4 --edge-zone attdallas1 --location southcentralus --max-pods 110 --node-count 1 --node-vm-size Standard_NC4asT4_v3 --enable-addons monitoring
```

## Deploying AKS using ARM templates
ARM templates are JSON files that define the resources you need to deploy for your solution. To deploy your resource using ARM template on the portal, you can follow [these instructions](https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/quickstart-create-templates-use-the-portal). Use the below ARM template to create an AKS cluster on the public MEC. In this template, the extendedLocation parameter has been added to define the public MEC.

```
{
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "resourceName": {
            "type": "String",
            "metadata": {
                "description": "The name of the Managed Cluster resource."
            }
        },
        "location": {
            "type": "String",
            "metadata": {
                "description": "The location of AKS resource."
            }
        },
        "edgeZoneName": {
            "type": "String",
            "metadata": {
                "description": "The name of the public MEC."
            }
        },
        "dnsPrefix": {
            "type": "String",
            "metadata": {
                "description": "Optional DNS prefix to use with hosted Kubernetes API server FQDN."
            }
        },
        "osDiskSizeGB": {
            "defaultValue": 0,
            "minValue": 0,
            "maxValue": 1023,
            "type": "Int",
            "metadata": {
                "description": "Disk size (in GiB) to provision for each of the agent pool nodes. This value ranges from 0 to 1023. Specifying 0 will apply the default disk size for that agentVMSize."
            }
        },
        "kubernetesVersion": {
            "defaultValue": "1.22.4",
            "type": "String",
            "metadata": {
                "description": "The version of Kubernetes."
            }
        },
        "networkPlugin": {
            "allowedValues": [
                "azure",
                "kubenet"
            ],
            "type": "String",
            "metadata": {
                "description": "Network plugin used for building Kubernetes network."
            }
        },
        "enableRBAC": {
            "defaultValue": true,
            "type": "Bool",
            "metadata": {
                "description": "Boolean flag to turn on and off of RBAC."
            }
        }
    },
    "resources": [
        {
            "type": "Microsoft.ContainerService/managedClusters",
            "apiVersion": "2021-03-01",
            "name": "[parameters('resourceName')]",
            "location": "[parameters('location')]",
            "extendedLocation" : {
                "name": "[parameters('edgeZoneName')]",
                "type": "EdgeZone"
            },
            "dependsOn": [],
            "tags": {},
            "identity": {
                "type": "SystemAssigned"
            },
            "properties": {
                "kubernetesVersion": "[parameters('kubernetesVersion')]",
                "enableRBAC": "[parameters('enableRBAC')]",
                "dnsPrefix": "[parameters('dnsPrefix')]",
                "agentPoolProfiles": [
                    {
                        "name": "agentpool",
                        "osDiskSizeGB": "[parameters('osDiskSizeGB')]",
                        "count": 1,
                        "vmSize": "Standard_NC4asT4_v3",
                        "osType": "Linux",
                        "storageProfile": "ManagedDisks",
                        "type": "VirtualMachineScaleSets",
                        "mode": "System",
                        "maxPods": 110
                    }
                ],
                "networkProfile": {
                    "loadBalancerSku": "standard",
                    "networkPlugin": "[parameters('networkPlugin')]"
                },
                "addonProfiles": {
                }
            }
        }
    ],
    "outputs": {
        "controlPlaneFQDN": {
            "type": "string",
            "value": "[reference(concat('Microsoft.ContainerService/managedClusters/', parameters('resourceName'))).fqdn]"
        }
    }
}
```

The below are the sample parameters for this template. You can select the subscription you want to deploy the resource on and also change the resource name, location and specify another public MEC name.

```
{
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "resourceName": {
            "value": "test-aks-cluster"
        },
        "location": {
            "value": "southcentralus"
        },
        "edgeZoneName": {
            "value": "microsoftrrdclab1"
        },
        "dnsPrefix": {
            "value": "test-aks-cluster-dns"
        },
        "osDiskSizeGB": {
            "value": 100
        },
        "kubernetesVersion": {
            "value": "1.22.4"
        },
        "networkPlugin": {
            "value": "kubenet"
        },
        "enableRBAC": {
            "value": true
        }
    }
}
```
