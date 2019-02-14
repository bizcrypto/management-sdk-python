# -*- coding: utf-8 -*-

import cohesity_management_sdk.models.bandwidth_limit_override

class BandwidthLimit(object):

    """Implementation of the 'Bandwidth Limit.' model.

    Specifies settings for limiting the data transfer rate between
    the local and remote Clusters.

    Attributes:
        bandwidth_limit_overrides (list of BandwidthLimitOverride): Array of
            Override Bandwidth Limits.  Specifies a list of override bandwidth
            limits and time periods when those limits override the
            rateLimitBytesPerSec limit. If overlapping time periods are
            specified, the last one in the array takes precedence.
        rate_limit_bytes_per_sec (long|int): Specifies the maximum allowed
            data transfer rate between the local Cluster and remote Clusters.
            The value is specified in bytes per second. If not set, the data
            transfer rate is not limited.
        timezone (string): Specifies a time zone for the specified time
            period. The time zone is defined in the following format:
            "Area/Location", for example: "America/New_York".

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth_limit_overrides":'bandwidthLimitOverrides',
        "rate_limit_bytes_per_sec":'rateLimitBytesPerSec',
        "timezone":'timezone'
    }

    def __init__(self,
                 bandwidth_limit_overrides=None,
                 rate_limit_bytes_per_sec=None,
                 timezone=None):
        """Constructor for the BandwidthLimit class"""

        # Initialize members of the class
        self.bandwidth_limit_overrides = bandwidth_limit_overrides
        self.rate_limit_bytes_per_sec = rate_limit_bytes_per_sec
        self.timezone = timezone


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
        bandwidth_limit_overrides = None
        if dictionary.get('bandwidthLimitOverrides') != None:
            bandwidth_limit_overrides = list()
            for structure in dictionary.get('bandwidthLimitOverrides'):
                bandwidth_limit_overrides.append(cohesity_management_sdk.models.bandwidth_limit_override.BandwidthLimitOverride.from_dictionary(structure))
        rate_limit_bytes_per_sec = dictionary.get('rateLimitBytesPerSec')
        timezone = dictionary.get('timezone')

        # Return an object of this model
        return cls(bandwidth_limit_overrides,
                   rate_limit_bytes_per_sec,
                   timezone)

