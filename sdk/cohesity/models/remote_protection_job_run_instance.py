# coding: utf-8

"""
    Cohesity REST API

    This API provides operations for interfacing with the Cohesity Cluster. NOTE: To view the documentation on the responses, click 'Model' next to 'Example Value' and keep clicking to expand the hierarchy.

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class RemoteProtectionJobRunInstance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, archive_task_uid=None, archive_version=None, expiry_time_usecs=None, index_size_bytes=None, job_run_id=None, metadata_complete=None, snapshot_time_usecs=None):
        """
        RemoteProtectionJobRunInstance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'archive_task_uid': 'RemoteProtectionJobRunInstanceArchiveTaskUid',
            'archive_version': 'int',
            'expiry_time_usecs': 'int',
            'index_size_bytes': 'int',
            'job_run_id': 'int',
            'metadata_complete': 'bool',
            'snapshot_time_usecs': 'int'
        }

        self.attribute_map = {
            'archive_task_uid': 'archiveTaskUid',
            'archive_version': 'archiveVersion',
            'expiry_time_usecs': 'expiryTimeUsecs',
            'index_size_bytes': 'indexSizeBytes',
            'job_run_id': 'jobRunId',
            'metadata_complete': 'metadataComplete',
            'snapshot_time_usecs': 'snapshotTimeUsecs'
        }

        self._archive_task_uid = archive_task_uid
        self._archive_version = archive_version
        self._expiry_time_usecs = expiry_time_usecs
        self._index_size_bytes = index_size_bytes
        self._job_run_id = job_run_id
        self._metadata_complete = metadata_complete
        self._snapshot_time_usecs = snapshot_time_usecs

    @property
    def archive_task_uid(self):
        """
        Gets the archive_task_uid of this RemoteProtectionJobRunInstance.


        :return: The archive_task_uid of this RemoteProtectionJobRunInstance.
        :rtype: RemoteProtectionJobRunInstanceArchiveTaskUid
        """
        return self._archive_task_uid

    @archive_task_uid.setter
    def archive_task_uid(self, archive_task_uid):
        """
        Sets the archive_task_uid of this RemoteProtectionJobRunInstance.


        :param archive_task_uid: The archive_task_uid of this RemoteProtectionJobRunInstance.
        :type: RemoteProtectionJobRunInstanceArchiveTaskUid
        """

        self._archive_task_uid = archive_task_uid

    @property
    def archive_version(self):
        """
        Gets the archive_version of this RemoteProtectionJobRunInstance.
        Specifies the version of the archive.

        :return: The archive_version of this RemoteProtectionJobRunInstance.
        :rtype: int
        """
        return self._archive_version

    @archive_version.setter
    def archive_version(self, archive_version):
        """
        Sets the archive_version of this RemoteProtectionJobRunInstance.
        Specifies the version of the archive.

        :param archive_version: The archive_version of this RemoteProtectionJobRunInstance.
        :type: int
        """

        self._archive_version = archive_version

    @property
    def expiry_time_usecs(self):
        """
        Gets the expiry_time_usecs of this RemoteProtectionJobRunInstance.
        Specifies the time when the archive expires. This time is recorded as a Unix epoch Timestamp (in microseconds).

        :return: The expiry_time_usecs of this RemoteProtectionJobRunInstance.
        :rtype: int
        """
        return self._expiry_time_usecs

    @expiry_time_usecs.setter
    def expiry_time_usecs(self, expiry_time_usecs):
        """
        Sets the expiry_time_usecs of this RemoteProtectionJobRunInstance.
        Specifies the time when the archive expires. This time is recorded as a Unix epoch Timestamp (in microseconds).

        :param expiry_time_usecs: The expiry_time_usecs of this RemoteProtectionJobRunInstance.
        :type: int
        """

        self._expiry_time_usecs = expiry_time_usecs

    @property
    def index_size_bytes(self):
        """
        Gets the index_size_bytes of this RemoteProtectionJobRunInstance.
        Specifies the size of the index for the archive.

        :return: The index_size_bytes of this RemoteProtectionJobRunInstance.
        :rtype: int
        """
        return self._index_size_bytes

    @index_size_bytes.setter
    def index_size_bytes(self, index_size_bytes):
        """
        Sets the index_size_bytes of this RemoteProtectionJobRunInstance.
        Specifies the size of the index for the archive.

        :param index_size_bytes: The index_size_bytes of this RemoteProtectionJobRunInstance.
        :type: int
        """

        self._index_size_bytes = index_size_bytes

    @property
    def job_run_id(self):
        """
        Gets the job_run_id of this RemoteProtectionJobRunInstance.
        Specifies the instance id of the Job Run task capturing the Snapshot.

        :return: The job_run_id of this RemoteProtectionJobRunInstance.
        :rtype: int
        """
        return self._job_run_id

    @job_run_id.setter
    def job_run_id(self, job_run_id):
        """
        Sets the job_run_id of this RemoteProtectionJobRunInstance.
        Specifies the instance id of the Job Run task capturing the Snapshot.

        :param job_run_id: The job_run_id of this RemoteProtectionJobRunInstance.
        :type: int
        """

        self._job_run_id = job_run_id

    @property
    def metadata_complete(self):
        """
        Gets the metadata_complete of this RemoteProtectionJobRunInstance.
        Specifies whether a full set of metadata is available now.

        :return: The metadata_complete of this RemoteProtectionJobRunInstance.
        :rtype: bool
        """
        return self._metadata_complete

    @metadata_complete.setter
    def metadata_complete(self, metadata_complete):
        """
        Sets the metadata_complete of this RemoteProtectionJobRunInstance.
        Specifies whether a full set of metadata is available now.

        :param metadata_complete: The metadata_complete of this RemoteProtectionJobRunInstance.
        :type: bool
        """

        self._metadata_complete = metadata_complete

    @property
    def snapshot_time_usecs(self):
        """
        Gets the snapshot_time_usecs of this RemoteProtectionJobRunInstance.
        Specify the time the Snapshot was captured as a Unix epoch Timestamp (in microseconds).

        :return: The snapshot_time_usecs of this RemoteProtectionJobRunInstance.
        :rtype: int
        """
        return self._snapshot_time_usecs

    @snapshot_time_usecs.setter
    def snapshot_time_usecs(self, snapshot_time_usecs):
        """
        Sets the snapshot_time_usecs of this RemoteProtectionJobRunInstance.
        Specify the time the Snapshot was captured as a Unix epoch Timestamp (in microseconds).

        :param snapshot_time_usecs: The snapshot_time_usecs of this RemoteProtectionJobRunInstance.
        :type: int
        """

        self._snapshot_time_usecs = snapshot_time_usecs

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other