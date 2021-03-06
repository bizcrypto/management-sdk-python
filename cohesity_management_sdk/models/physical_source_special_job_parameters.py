# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.application_specific_parameters
import cohesity_management_sdk.models.file_or_directory_to_protect
import cohesity_management_sdk.models.windows_host_snapshot_parameters

class PhysicalSourceSpecialJobParameters(object):

    """Implementation of the 'Physical Source Special Job Parameters.' model.

    Specifies additional special settings applicable for a Protection Source
    of 'kPhysical' type in a Protection Job.

    Attributes:
        application_parameters (ApplicationSpecificParameters): TODO: type
            description here.
        enable_system_backup (bool): Specifies whether to allow system backup
            using 3rd party tools installed on the Protection Host. System
            backups are used for doing bare metal recovery later. This field
            is applicable only for System backups.
        file_paths (list of FileOrDirectoryToProtect): Array of File Paths to
            Back Up.  Specifies a list of directories or files to protect in a
            Physical Server.
        volume_guid (list of string): Array of Mounted Volumes to Back Up. 
            Specifies the subset of mounted volumes to protect in a Physical
            Server. If not specified, all mounted volumes on a Physical Server
            are protected.
        windows_parameters (WindowsHostSnapshotParameters): Specifies settings
            that are meaningful only on Windows hosts.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "application_parameters":'applicationParameters',
        "enable_system_backup":'enableSystemBackup',
        "file_paths":'filePaths',
        "volume_guid":'volumeGuid',
        "windows_parameters":'windowsParameters'
    }

    def __init__(self,
                 application_parameters=None,
                 enable_system_backup=None,
                 file_paths=None,
                 volume_guid=None,
                 windows_parameters=None):
        """Constructor for the PhysicalSourceSpecialJobParameters class"""

        # Initialize members of the class
        self.application_parameters = application_parameters
        self.enable_system_backup = enable_system_backup
        self.file_paths = file_paths
        self.volume_guid = volume_guid
        self.windows_parameters = windows_parameters


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
        application_parameters = cohesity_management_sdk.models.application_specific_parameters.ApplicationSpecificParameters.from_dictionary(dictionary.get('applicationParameters')) if dictionary.get('applicationParameters') else None
        enable_system_backup = dictionary.get('enableSystemBackup')
        file_paths = None
        if dictionary.get('filePaths') != None:
            file_paths = list()
            for structure in dictionary.get('filePaths'):
                file_paths.append(cohesity_management_sdk.models.file_or_directory_to_protect.FileOrDirectoryToProtect.from_dictionary(structure))
        volume_guid = dictionary.get('volumeGuid')
        windows_parameters = cohesity_management_sdk.models.windows_host_snapshot_parameters.WindowsHostSnapshotParameters.from_dictionary(dictionary.get('windowsParameters')) if dictionary.get('windowsParameters') else None

        # Return an object of this model
        return cls(application_parameters,
                   enable_system_backup,
                   file_paths,
                   volume_guid,
                   windows_parameters)


