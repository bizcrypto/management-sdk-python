# -*- coding: utf-8 -*-

import cohesity_management_sdk.models.map_reduce_information
import cohesity_management_sdk.models.map_reduce_instance_wrapper

class ApplicationRunHistory(object):

    """Implementation of the 'Application Run History.' model.

    AppRunHistory is the struct containing the run information of the
    application instances. An application instance can be run only once. Each
    run of the application creates a new application instance.

    Attributes:
        app_info (MapReduceInformation): This will be used to encapsulate
            information about mapper and reducer only. On UI this will be used
            to show the list of available apps to the user.
        mr_instances (list of MapReduceInstanceWrapper): InstancesWrapper is
            the slice containing the information about the map reduce
            application instances.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "app_info":'appInfo',
        "mr_instances":'mrInstances'
    }

    def __init__(self,
                 app_info=None,
                 mr_instances=None):
        """Constructor for the ApplicationRunHistory class"""

        # Initialize members of the class
        self.app_info = app_info
        self.mr_instances = mr_instances


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
        app_info = cohesity_management_sdk.models.map_reduce_information.MapReduceInformation.from_dictionary(dictionary.get('appInfo')) if dictionary.get('appInfo') else None
        mr_instances = None
        if dictionary.get('mrInstances') != None:
            mr_instances = list()
            for structure in dictionary.get('mrInstances'):
                mr_instances.append(cohesity_management_sdk.models.map_reduce_instance_wrapper.MapReduceInstanceWrapper.from_dictionary(structure))

        # Return an object of this model
        return cls(app_info,
                   mr_instances)


