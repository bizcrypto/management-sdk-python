# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.deploy_v_ms_to_aws_params
import cohesity_management_sdk.models.deploy_v_ms_to_azure_params
import cohesity_management_sdk.models.deploy_v_ms_to_gcp_params

class DeployVMsToCloudParams(object):

    """Implementation of the 'DeployVMsToCloudParams' model.

    Contains Cloud specific information needed to identify various resources
    when deploying a VM to Cloud.

    Attributes:
        deploy_vms_to_aws_params (DeployVMsToAWSParams): Contains AWS specific
            information needed to identify various resources when converting
            and deploying a VM to AWS.
        deploy_vms_to_azure_params (DeployVMsToAzureParams): Contains Azure
            specific information needed to identify various resources when
            converting and deploying a VM to Azure.
        deploy_vms_to_gcp_params (DeployVMsToGCPParams): Contains GCP specific
            information needed to identify various resources when converting
            and deploying a VM to GCP.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deploy_vms_to_aws_params":'deployVmsToAwsParams',
        "deploy_vms_to_azure_params":'deployVmsToAzureParams',
        "deploy_vms_to_gcp_params":'deployVmsToGcpParams'
    }

    def __init__(self,
                 deploy_vms_to_aws_params=None,
                 deploy_vms_to_azure_params=None,
                 deploy_vms_to_gcp_params=None):
        """Constructor for the DeployVMsToCloudParams class"""

        # Initialize members of the class
        self.deploy_vms_to_aws_params = deploy_vms_to_aws_params
        self.deploy_vms_to_azure_params = deploy_vms_to_azure_params
        self.deploy_vms_to_gcp_params = deploy_vms_to_gcp_params


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        deploy_vms_to_aws_params = cohesity_management_sdk.models.deploy_v_ms_to_aws_params.DeployVMsToAWSParams.from_dictionary(dictionary.get('deployVmsToAwsParams')) if dictionary.get('deployVmsToAwsParams') else None
        deploy_vms_to_azure_params = cohesity_management_sdk.models.deploy_v_ms_to_azure_params.DeployVMsToAzureParams.from_dictionary(dictionary.get('deployVmsToAzureParams')) if dictionary.get('deployVmsToAzureParams') else None
        deploy_vms_to_gcp_params = cohesity_management_sdk.models.deploy_v_ms_to_gcp_params.DeployVMsToGCPParams.from_dictionary(dictionary.get('deployVmsToGcpParams')) if dictionary.get('deployVmsToGcpParams') else None

        # Return an object of this model
        return cls(deploy_vms_to_aws_params,
                   deploy_vms_to_azure_params,
                   deploy_vms_to_gcp_params)


