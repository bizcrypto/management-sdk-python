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


class ClusterAuditLog(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, action=None, details=None, domain=None, entity_id=None, entity_name=None, entity_type=None, human_timestamp=None, new_record=None, previous_record=None, timestamp_usecs=None, user_name=None):
        """
        ClusterAuditLog - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action': 'str',
            'details': 'str',
            'domain': 'str',
            'entity_id': 'str',
            'entity_name': 'str',
            'entity_type': 'str',
            'human_timestamp': 'str',
            'new_record': 'str',
            'previous_record': 'str',
            'timestamp_usecs': 'int',
            'user_name': 'str'
        }

        self.attribute_map = {
            'action': 'action',
            'details': 'details',
            'domain': 'domain',
            'entity_id': 'entityId',
            'entity_name': 'entityName',
            'entity_type': 'entityType',
            'human_timestamp': 'humanTimestamp',
            'new_record': 'newRecord',
            'previous_record': 'previousRecord',
            'timestamp_usecs': 'timestampUsecs',
            'user_name': 'userName'
        }

        self._action = action
        self._details = details
        self._domain = domain
        self._entity_id = entity_id
        self._entity_name = entity_name
        self._entity_type = entity_type
        self._human_timestamp = human_timestamp
        self._new_record = new_record
        self._previous_record = previous_record
        self._timestamp_usecs = timestamp_usecs
        self._user_name = user_name

    @property
    def action(self):
        """
        Gets the action of this ClusterAuditLog.
        Specifies the action that caused the log to be generated.

        :return: The action of this ClusterAuditLog.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ClusterAuditLog.
        Specifies the action that caused the log to be generated.

        :param action: The action of this ClusterAuditLog.
        :type: str
        """

        self._action = action

    @property
    def details(self):
        """
        Gets the details of this ClusterAuditLog.
        Specifies more information about the action.

        :return: The details of this ClusterAuditLog.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this ClusterAuditLog.
        Specifies more information about the action.

        :param details: The details of this ClusterAuditLog.
        :type: str
        """

        self._details = details

    @property
    def domain(self):
        """
        Gets the domain of this ClusterAuditLog.
        Specifies the domain of the user who caused the action that generated the log.

        :return: The domain of this ClusterAuditLog.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this ClusterAuditLog.
        Specifies the domain of the user who caused the action that generated the log.

        :param domain: The domain of this ClusterAuditLog.
        :type: str
        """

        self._domain = domain

    @property
    def entity_id(self):
        """
        Gets the entity_id of this ClusterAuditLog.
        Specifies the id of the entity (object) that the action is invoked on.

        :return: The entity_id of this ClusterAuditLog.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this ClusterAuditLog.
        Specifies the id of the entity (object) that the action is invoked on.

        :param entity_id: The entity_id of this ClusterAuditLog.
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_name(self):
        """
        Gets the entity_name of this ClusterAuditLog.
        Specifies the entity (object) name that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns BackupEng.

        :return: The entity_name of this ClusterAuditLog.
        :rtype: str
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, entity_name):
        """
        Sets the entity_name of this ClusterAuditLog.
        Specifies the entity (object) name that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns BackupEng.

        :param entity_name: The entity_name of this ClusterAuditLog.
        :type: str
        """

        self._entity_name = entity_name

    @property
    def entity_type(self):
        """
        Gets the entity_type of this ClusterAuditLog.
        Specifies the type of the entity (object) that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns 'Protection Job'.

        :return: The entity_type of this ClusterAuditLog.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this ClusterAuditLog.
        Specifies the type of the entity (object) that the action is invoked on. For example, if a Job called BackupEng is paused, this field returns 'Protection Job'.

        :param entity_type: The entity_type of this ClusterAuditLog.
        :type: str
        """

        self._entity_type = entity_type

    @property
    def human_timestamp(self):
        """
        Gets the human_timestamp of this ClusterAuditLog.
        Specifies the time when the log was generated. The time is specified using a human readable timestamp.

        :return: The human_timestamp of this ClusterAuditLog.
        :rtype: str
        """
        return self._human_timestamp

    @human_timestamp.setter
    def human_timestamp(self, human_timestamp):
        """
        Sets the human_timestamp of this ClusterAuditLog.
        Specifies the time when the log was generated. The time is specified using a human readable timestamp.

        :param human_timestamp: The human_timestamp of this ClusterAuditLog.
        :type: str
        """

        self._human_timestamp = human_timestamp

    @property
    def new_record(self):
        """
        Gets the new_record of this ClusterAuditLog.
        Specifies the record after the action is invoked.

        :return: The new_record of this ClusterAuditLog.
        :rtype: str
        """
        return self._new_record

    @new_record.setter
    def new_record(self, new_record):
        """
        Sets the new_record of this ClusterAuditLog.
        Specifies the record after the action is invoked.

        :param new_record: The new_record of this ClusterAuditLog.
        :type: str
        """

        self._new_record = new_record

    @property
    def previous_record(self):
        """
        Gets the previous_record of this ClusterAuditLog.
        Specifies the record before the action is invoked.

        :return: The previous_record of this ClusterAuditLog.
        :rtype: str
        """
        return self._previous_record

    @previous_record.setter
    def previous_record(self, previous_record):
        """
        Sets the previous_record of this ClusterAuditLog.
        Specifies the record before the action is invoked.

        :param previous_record: The previous_record of this ClusterAuditLog.
        :type: str
        """

        self._previous_record = previous_record

    @property
    def timestamp_usecs(self):
        """
        Gets the timestamp_usecs of this ClusterAuditLog.
        Specifies the time when the log was generated. The time is specified using a Unix epoch Timestamp (in microseconds).

        :return: The timestamp_usecs of this ClusterAuditLog.
        :rtype: int
        """
        return self._timestamp_usecs

    @timestamp_usecs.setter
    def timestamp_usecs(self, timestamp_usecs):
        """
        Sets the timestamp_usecs of this ClusterAuditLog.
        Specifies the time when the log was generated. The time is specified using a Unix epoch Timestamp (in microseconds).

        :param timestamp_usecs: The timestamp_usecs of this ClusterAuditLog.
        :type: int
        """

        self._timestamp_usecs = timestamp_usecs

    @property
    def user_name(self):
        """
        Gets the user_name of this ClusterAuditLog.
        Specifies the user who caused the action that generated the log.

        :return: The user_name of this ClusterAuditLog.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ClusterAuditLog.
        Specifies the user who caused the action that generated the log.

        :param user_name: The user_name of this ClusterAuditLog.
        :type: str
        """

        self._user_name = user_name

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