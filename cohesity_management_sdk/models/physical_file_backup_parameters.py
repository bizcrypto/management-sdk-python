# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import cohesity_management_sdk.models.backup_path_information

class PhysicalFileBackupParameters(object):

    """Implementation of the 'Physical File Backup Parameters.' model.

    Message to capture params when backing up files on a Physical source.

    Attributes:
        backup_path_info_vec (list of BackupPathInformation): Specifies the
            paths to backup on the Physical source.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "backup_path_info_vec":'backupPathInfoVec'
    }

    def __init__(self,
                 backup_path_info_vec=None):
        """Constructor for the PhysicalFileBackupParameters class"""

        # Initialize members of the class
        self.backup_path_info_vec = backup_path_info_vec


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
        backup_path_info_vec = None
        if dictionary.get('backupPathInfoVec') != None:
            backup_path_info_vec = list()
            for structure in dictionary.get('backupPathInfoVec'):
                backup_path_info_vec.append(cohesity_management_sdk.models.backup_path_information.BackupPathInformation.from_dictionary(structure))

        # Return an object of this model
        return cls(backup_path_info_vec)


