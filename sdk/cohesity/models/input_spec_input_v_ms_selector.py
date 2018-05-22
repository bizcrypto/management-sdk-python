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


class InputSpecInputVMsSelector(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, file_time_filter=None, filename_glob=None, job_ids=None, max_snapshot_timestamp=None, min_snapshot_timestamp=None, partition_ids=None, process_latest_only=None, root_dir=None, source_entity_ids=None, view_box_ids=None, view_names=None):
        """
        InputSpecInputVMsSelector - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file_time_filter': 'InputSpecFileTimeFilter',
            'filename_glob': 'list[str]',
            'job_ids': 'list[int]',
            'max_snapshot_timestamp': 'int',
            'min_snapshot_timestamp': 'int',
            'partition_ids': 'list[int]',
            'process_latest_only': 'bool',
            'root_dir': 'str',
            'source_entity_ids': 'list[int]',
            'view_box_ids': 'list[int]',
            'view_names': 'list[str]'
        }

        self.attribute_map = {
            'file_time_filter': 'fileTimeFilter',
            'filename_glob': 'filenameGlob',
            'job_ids': 'jobIds',
            'max_snapshot_timestamp': 'maxSnapshotTimestamp',
            'min_snapshot_timestamp': 'minSnapshotTimestamp',
            'partition_ids': 'partitionIds',
            'process_latest_only': 'processLatestOnly',
            'root_dir': 'rootDir',
            'source_entity_ids': 'sourceEntityIds',
            'view_box_ids': 'viewBoxIds',
            'view_names': 'viewNames'
        }

        self._file_time_filter = file_time_filter
        self._filename_glob = filename_glob
        self._job_ids = job_ids
        self._max_snapshot_timestamp = max_snapshot_timestamp
        self._min_snapshot_timestamp = min_snapshot_timestamp
        self._partition_ids = partition_ids
        self._process_latest_only = process_latest_only
        self._root_dir = root_dir
        self._source_entity_ids = source_entity_ids
        self._view_box_ids = view_box_ids
        self._view_names = view_names

    @property
    def file_time_filter(self):
        """
        Gets the file_time_filter of this InputSpecInputVMsSelector.
        Time filter for file's last change time.

        :return: The file_time_filter of this InputSpecInputVMsSelector.
        :rtype: InputSpecFileTimeFilter
        """
        return self._file_time_filter

    @file_time_filter.setter
    def file_time_filter(self, file_time_filter):
        """
        Sets the file_time_filter of this InputSpecInputVMsSelector.
        Time filter for file's last change time.

        :param file_time_filter: The file_time_filter of this InputSpecInputVMsSelector.
        :type: InputSpecFileTimeFilter
        """

        self._file_time_filter = file_time_filter

    @property
    def filename_glob(self):
        """
        Gets the filename_glob of this InputSpecInputVMsSelector.
        After VMDKs are selected as above, the files within them can be selected by using these predicates.

        :return: The filename_glob of this InputSpecInputVMsSelector.
        :rtype: list[str]
        """
        return self._filename_glob

    @filename_glob.setter
    def filename_glob(self, filename_glob):
        """
        Sets the filename_glob of this InputSpecInputVMsSelector.
        After VMDKs are selected as above, the files within them can be selected by using these predicates.

        :param filename_glob: The filename_glob of this InputSpecInputVMsSelector.
        :type: list[str]
        """

        self._filename_glob = filename_glob

    @property
    def job_ids(self):
        """
        Gets the job_ids of this InputSpecInputVMsSelector.


        :return: The job_ids of this InputSpecInputVMsSelector.
        :rtype: list[int]
        """
        return self._job_ids

    @job_ids.setter
    def job_ids(self, job_ids):
        """
        Sets the job_ids of this InputSpecInputVMsSelector.


        :param job_ids: The job_ids of this InputSpecInputVMsSelector.
        :type: list[int]
        """

        self._job_ids = job_ids

    @property
    def max_snapshot_timestamp(self):
        """
        Gets the max_snapshot_timestamp of this InputSpecInputVMsSelector.
        Exclusive end of snapshot_timestamp range. If missing, inf will be used as the timestamp range.

        :return: The max_snapshot_timestamp of this InputSpecInputVMsSelector.
        :rtype: int
        """
        return self._max_snapshot_timestamp

    @max_snapshot_timestamp.setter
    def max_snapshot_timestamp(self, max_snapshot_timestamp):
        """
        Sets the max_snapshot_timestamp of this InputSpecInputVMsSelector.
        Exclusive end of snapshot_timestamp range. If missing, inf will be used as the timestamp range.

        :param max_snapshot_timestamp: The max_snapshot_timestamp of this InputSpecInputVMsSelector.
        :type: int
        """

        self._max_snapshot_timestamp = max_snapshot_timestamp

    @property
    def min_snapshot_timestamp(self):
        """
        Gets the min_snapshot_timestamp of this InputSpecInputVMsSelector.
        Inclusive. If missing, 0 will the default lower end of timestamp range

        :return: The min_snapshot_timestamp of this InputSpecInputVMsSelector.
        :rtype: int
        """
        return self._min_snapshot_timestamp

    @min_snapshot_timestamp.setter
    def min_snapshot_timestamp(self, min_snapshot_timestamp):
        """
        Sets the min_snapshot_timestamp of this InputSpecInputVMsSelector.
        Inclusive. If missing, 0 will the default lower end of timestamp range

        :param min_snapshot_timestamp: The min_snapshot_timestamp of this InputSpecInputVMsSelector.
        :type: int
        """

        self._min_snapshot_timestamp = min_snapshot_timestamp

    @property
    def partition_ids(self):
        """
        Gets the partition_ids of this InputSpecInputVMsSelector.


        :return: The partition_ids of this InputSpecInputVMsSelector.
        :rtype: list[int]
        """
        return self._partition_ids

    @partition_ids.setter
    def partition_ids(self, partition_ids):
        """
        Sets the partition_ids of this InputSpecInputVMsSelector.


        :param partition_ids: The partition_ids of this InputSpecInputVMsSelector.
        :type: list[int]
        """

        self._partition_ids = partition_ids

    @property
    def process_latest_only(self):
        """
        Gets the process_latest_only of this InputSpecInputVMsSelector.
        Boolean flag to indicate if only latest snapshot of each object should be processed.

        :return: The process_latest_only of this InputSpecInputVMsSelector.
        :rtype: bool
        """
        return self._process_latest_only

    @process_latest_only.setter
    def process_latest_only(self, process_latest_only):
        """
        Sets the process_latest_only of this InputSpecInputVMsSelector.
        Boolean flag to indicate if only latest snapshot of each object should be processed.

        :param process_latest_only: The process_latest_only of this InputSpecInputVMsSelector.
        :type: bool
        """

        self._process_latest_only = process_latest_only

    @property
    def root_dir(self):
        """
        Gets the root_dir of this InputSpecInputVMsSelector.
        Within each volume, traversal will be rooted at this directory. A typical value here might be /home

        :return: The root_dir of this InputSpecInputVMsSelector.
        :rtype: str
        """
        return self._root_dir

    @root_dir.setter
    def root_dir(self, root_dir):
        """
        Sets the root_dir of this InputSpecInputVMsSelector.
        Within each volume, traversal will be rooted at this directory. A typical value here might be /home

        :param root_dir: The root_dir of this InputSpecInputVMsSelector.
        :type: str
        """

        self._root_dir = root_dir

    @property
    def source_entity_ids(self):
        """
        Gets the source_entity_ids of this InputSpecInputVMsSelector.


        :return: The source_entity_ids of this InputSpecInputVMsSelector.
        :rtype: list[int]
        """
        return self._source_entity_ids

    @source_entity_ids.setter
    def source_entity_ids(self, source_entity_ids):
        """
        Sets the source_entity_ids of this InputSpecInputVMsSelector.


        :param source_entity_ids: The source_entity_ids of this InputSpecInputVMsSelector.
        :type: list[int]
        """

        self._source_entity_ids = source_entity_ids

    @property
    def view_box_ids(self):
        """
        Gets the view_box_ids of this InputSpecInputVMsSelector.


        :return: The view_box_ids of this InputSpecInputVMsSelector.
        :rtype: list[int]
        """
        return self._view_box_ids

    @view_box_ids.setter
    def view_box_ids(self, view_box_ids):
        """
        Sets the view_box_ids of this InputSpecInputVMsSelector.


        :param view_box_ids: The view_box_ids of this InputSpecInputVMsSelector.
        :type: list[int]
        """

        self._view_box_ids = view_box_ids

    @property
    def view_names(self):
        """
        Gets the view_names of this InputSpecInputVMsSelector.


        :return: The view_names of this InputSpecInputVMsSelector.
        :rtype: list[str]
        """
        return self._view_names

    @view_names.setter
    def view_names(self, view_names):
        """
        Sets the view_names of this InputSpecInputVMsSelector.


        :param view_names: The view_names of this InputSpecInputVMsSelector.
        :type: list[str]
        """

        self._view_names = view_names

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