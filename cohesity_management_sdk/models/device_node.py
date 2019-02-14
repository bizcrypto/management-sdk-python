# -*- coding: utf-8 -*-

import cohesity_management_sdk.models.device_tree
import cohesity_management_sdk.models.file_partition_block

class DeviceNode(object):

    """Implementation of the 'Device Node.' model.

    Specifies the list of devices that need to be combined to form the
    storage space.
    Only one of the fields is populated with a device node.
    If the device node is a leaf node, leafNode is populated with details
    about the partition blocks in the file.
    If the device node is an intermediate node, intermediateNode is
    populated with a device sub-tree.

    Attributes:
        intermediate_node (DeviceTree): TODO: type description here.
        leaf_node (FilePartitionBlock): Defines a leaf node of a device tree.
            This refers to a logical partition in a virtual disk file.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "intermediate_node":'intermediateNode',
        "leaf_node":'leafNode'
    }

    def __init__(self,
                 intermediate_node=None,
                 leaf_node=None):
        """Constructor for the DeviceNode class"""

        # Initialize members of the class
        self.intermediate_node = intermediate_node
        self.leaf_node = leaf_node


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
        intermediate_node = cohesity_management_sdk.models.device_tree.DeviceTree.from_dictionary(dictionary.get('intermediateNode')) if dictionary.get('intermediateNode') else None
        leaf_node = cohesity_management_sdk.models.file_partition_block.FilePartitionBlock.from_dictionary(dictionary.get('leafNode')) if dictionary.get('leafNode') else None

        # Return an object of this model
        return cls(intermediate_node,
                   leaf_node)


