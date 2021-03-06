# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.file_or_directory_path_filter

class NASEnvironmentJobParameters(object):

    """Implementation of the 'NAS Environment Job Parameters.' model.

    Specifies job parameters applicable for all 'kGenericNas' Environment
    type
    Protection Sources in a Protection Job.

    Attributes:
        continue_on_error (bool): Specifies if the backup should continue on
            with other Protection Sources even if the backup operation of some
            Protection Source fails. If true, the Cohesity Cluster ignores the
            errors and continues with remaining Protection Sources in the job.
            If false, the backup operation stops when an error occurs. This
            does not apply to non-snapshot based generic NAS backup jobs. If
            not set, default value is true.
        enable_faster_incremental_backups (bool): Specifies whether this job
            will enable faster incremental backups using change list or
            similar APIs
        file_path_filters (FileOrDirectoryPathFilter): Specifies filters to
            match files and directories on a Server. Two kinds of filters are
            supported. a) prefix which always starts with '/'. b) posix which
            always starts with '*' (cannot be "*" only). Regular expressions
            are not supported. If a directory is matched, the action is
            applicable to all of its descendants. File paths not matching any
            protectFilters are not backed up.  An example is: Protect Filters:
            "/" Exclude Filters: "/tmp", "*.mp4" Using such a policy will
            include everything under the root directory except the /tmp
            directory and all the mp4 files.
        nas_protocol (NasProtocol1Enum): Specifies the preferred protocol to
            use for backup. This does not apply to generic NAS and will be
            ignored. Specifies the protocol used by a NAS server. 'kNfs3'
            indicates NFS v3 protocol. 'kCifs1' indicates CIFS v1.0 protocol.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "continue_on_error":'continueOnError',
        "enable_faster_incremental_backups":'enableFasterIncrementalBackups',
        "file_path_filters":'filePathFilters',
        "nas_protocol":'nasProtocol'
    }

    def __init__(self,
                 continue_on_error=None,
                 enable_faster_incremental_backups=None,
                 file_path_filters=None,
                 nas_protocol=None):
        """Constructor for the NASEnvironmentJobParameters class"""

        # Initialize members of the class
        self.continue_on_error = continue_on_error
        self.enable_faster_incremental_backups = enable_faster_incremental_backups
        self.file_path_filters = file_path_filters
        self.nas_protocol = nas_protocol


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
        continue_on_error = dictionary.get('continueOnError')
        enable_faster_incremental_backups = dictionary.get('enableFasterIncrementalBackups')
        file_path_filters = cohesity_management_sdk.models.file_or_directory_path_filter.FileOrDirectoryPathFilter.from_dictionary(dictionary.get('filePathFilters')) if dictionary.get('filePathFilters') else None
        nas_protocol = dictionary.get('nasProtocol')

        # Return an object of this model
        return cls(continue_on_error,
                   enable_faster_incremental_backups,
                   file_path_filters,
                   nas_protocol)


