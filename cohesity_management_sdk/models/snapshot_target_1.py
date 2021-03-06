# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.archival_target
import cohesity_management_sdk.models.replication_target_1

class SnapshotTarget1(object):

    """Implementation of the 'Snapshot Target.1' model.

    Specifies settings about a target where a copied Snapshot is stored.
    A target can be a Remote Cluster or an Archival External Target such as
    AWS or Tape.

    Attributes:
        archival_target (ArchivalTarget): Specifies settings about the
            Archival External Target (such as Tape or AWS).
        replication_target (ReplicationTarget1): Specifies settings about the
            Remote Cohesity Cluster where Snapshots are copied to.
        mtype (Type26Enum): Specifies the type of a Snapshot target such as
            'kLocal', 'kRemote' or 'kArchival'. 'kLocal' means the Snapshot is
            stored on a local Cohesity Cluster. 'kRemote' means the Snapshot
            is stored on a Remote Cohesity Cluster. (It was copied to the
            Remote Cohesity Cluster using replication.) 'kArchival' means the
            Snapshot is stored on a Archival External Target (such as Tape or
            AWS). 'kCloudDeploy' means the Snapshot is stored on a Cloud
            platform.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "archival_target":'archivalTarget',
        "replication_target":'replicationTarget',
        "mtype":'type'
    }

    def __init__(self,
                 archival_target=None,
                 replication_target=None,
                 mtype=None):
        """Constructor for the SnapshotTarget1 class"""

        # Initialize members of the class
        self.archival_target = archival_target
        self.replication_target = replication_target
        self.mtype = mtype


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
        archival_target = cohesity_management_sdk.models.archival_target.ArchivalTarget.from_dictionary(dictionary.get('archivalTarget')) if dictionary.get('archivalTarget') else None
        replication_target = cohesity_management_sdk.models.replication_target_1.ReplicationTarget1.from_dictionary(dictionary.get('replicationTarget')) if dictionary.get('replicationTarget') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(archival_target,
                   replication_target,
                   mtype)


