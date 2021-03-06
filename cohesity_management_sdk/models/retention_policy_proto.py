# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.worm_retention_proto

class RetentionPolicyProto(object):

    """Implementation of the 'Retention Policy Proto.' model.

    Message that specifies the retention policy for backup snapshots.

    Attributes:
        num_days_to_keep (long|int): The number of days to keep the snapshots
            for a backup run.
        worm_retention (WormRetentionProto): Message that specifies the WORM
            attributes. WORM attributes can be associated with any of the
            following: 1. backup policy: compliance or administrative policy
            with worm retention. 2. backup runs: worm retention inherited from
            policy at successful backup run completion.. 3. backup tasks do
            not inherit WORM retention. Instead they check for WORM property
            on the corresponding backup run. There are no WORM attributes
            associated with the backup job.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_days_to_keep":'numDaysToKeep',
        "worm_retention":'wormRetention'
    }

    def __init__(self,
                 num_days_to_keep=None,
                 worm_retention=None):
        """Constructor for the RetentionPolicyProto class"""

        # Initialize members of the class
        self.num_days_to_keep = num_days_to_keep
        self.worm_retention = worm_retention


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
        num_days_to_keep = dictionary.get('numDaysToKeep')
        worm_retention = cohesity_management_sdk.models.worm_retention_proto.WormRetentionProto.from_dictionary(dictionary.get('wormRetention')) if dictionary.get('wormRetention') else None

        # Return an object of this model
        return cls(num_days_to_keep,
                   worm_retention)


