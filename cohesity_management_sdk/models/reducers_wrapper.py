# -*- coding: utf-8 -*-

import cohesity_management_sdk.models.information_about_a_reducer

class ReducersWrapper(object):

    """Implementation of the 'Reducers Wrapper.' model.

    ReducersWrapper is the struct to define the list of reducers.

    Attributes:
        reducers (list of InformationAboutAReducer): Reducers specifies the
            list of available reducers in analytics workbench.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reducers":'reducers'
    }

    def __init__(self,
                 reducers=None):
        """Constructor for the ReducersWrapper class"""

        # Initialize members of the class
        self.reducers = reducers


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
        reducers = None
        if dictionary.get('reducers') != None:
            reducers = list()
            for structure in dictionary.get('reducers'):
                reducers.append(cohesity_management_sdk.models.information_about_a_reducer.InformationAboutAReducer.from_dictionary(structure))

        # Return an object of this model
        return cls(reducers)

