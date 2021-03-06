# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.net_app_cluster_information
import cohesity_management_sdk.models.net_app_volume_information
import cohesity_management_sdk.models.net_app_vserver_information

class NetAppProtectionSource(object):

    """Implementation of the 'NetApp Protection Source.' model.

    Specifies a Protection Source in a NetApp environment.

    Attributes:
        cluster_info (NetAppClusterInformation): Specifies information about a
            NetApp Cluster Protection Source.
        is_top_level (bool): Specifies if this Object is a top level Object.
            Because a top level Object can either be a NetApp cluster or a
            Vserver, this cannot be determined only by type.
        name (string): Specifies the name of the NetApp Object.
        mtype (Type11Enum): Specifies the type of managed NetApp Object in a
            NetApp Protection Source such as 'kCluster', 'kVserver' or
            'kVolume'. 'kCluster' indicates a Netapp cluster as a protection
            source. 'kVserver' indicates a Netapp vserver in a cluster as a
            protection source. 'kVolume' indicates  a volume in Netapp vserver
            as a protection source.
        uuid (string): Specifies the globally unique ID of this Object
            assigned by the NetApp server.
        volume_info (NetAppVolumeInformation): Specifies information about a
            volume in a NetApp cluster.
        vserver_info (NetAppVserverInformation): Specifies information about a
            NetApp Vserver in a NetApp Protection Source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_info":'clusterInfo',
        "is_top_level":'isTopLevel',
        "name":'name',
        "mtype":'type',
        "uuid":'uuid',
        "volume_info":'volumeInfo',
        "vserver_info":'vserverInfo'
    }

    def __init__(self,
                 cluster_info=None,
                 is_top_level=None,
                 name=None,
                 mtype=None,
                 uuid=None,
                 volume_info=None,
                 vserver_info=None):
        """Constructor for the NetAppProtectionSource class"""

        # Initialize members of the class
        self.cluster_info = cluster_info
        self.is_top_level = is_top_level
        self.name = name
        self.mtype = mtype
        self.uuid = uuid
        self.volume_info = volume_info
        self.vserver_info = vserver_info


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
        cluster_info = cohesity_management_sdk.models.net_app_cluster_information.NetAppClusterInformation.from_dictionary(dictionary.get('clusterInfo')) if dictionary.get('clusterInfo') else None
        is_top_level = dictionary.get('isTopLevel')
        name = dictionary.get('name')
        mtype = dictionary.get('type')
        uuid = dictionary.get('uuid')
        volume_info = cohesity_management_sdk.models.net_app_volume_information.NetAppVolumeInformation.from_dictionary(dictionary.get('volumeInfo')) if dictionary.get('volumeInfo') else None
        vserver_info = cohesity_management_sdk.models.net_app_vserver_information.NetAppVserverInformation.from_dictionary(dictionary.get('vserverInfo')) if dictionary.get('vserverInfo') else None

        # Return an object of this model
        return cls(cluster_info,
                   is_top_level,
                   name,
                   mtype,
                   uuid,
                   volume_info,
                   vserver_info)


