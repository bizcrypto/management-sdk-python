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


class ViewBoxPairInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, local_view_box_id=None, local_view_box_name=None, remote_view_box_id=None, remote_view_box_name=None):
        """
        ViewBoxPairInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'local_view_box_id': 'int',
            'local_view_box_name': 'str',
            'remote_view_box_id': 'int',
            'remote_view_box_name': 'str'
        }

        self.attribute_map = {
            'local_view_box_id': 'localViewBoxId',
            'local_view_box_name': 'localViewBoxName',
            'remote_view_box_id': 'remoteViewBoxId',
            'remote_view_box_name': 'remoteViewBoxName'
        }

        self._local_view_box_id = local_view_box_id
        self._local_view_box_name = local_view_box_name
        self._remote_view_box_id = remote_view_box_id
        self._remote_view_box_name = remote_view_box_name

    @property
    def local_view_box_id(self):
        """
        Gets the local_view_box_id of this ViewBoxPairInfo.
        Specifies the id of the Storage Domain (View Box) on the local Cluster.

        :return: The local_view_box_id of this ViewBoxPairInfo.
        :rtype: int
        """
        return self._local_view_box_id

    @local_view_box_id.setter
    def local_view_box_id(self, local_view_box_id):
        """
        Sets the local_view_box_id of this ViewBoxPairInfo.
        Specifies the id of the Storage Domain (View Box) on the local Cluster.

        :param local_view_box_id: The local_view_box_id of this ViewBoxPairInfo.
        :type: int
        """

        self._local_view_box_id = local_view_box_id

    @property
    def local_view_box_name(self):
        """
        Gets the local_view_box_name of this ViewBoxPairInfo.
        Specifies the name of the Storage Domain (View Box) on the local Cluster.

        :return: The local_view_box_name of this ViewBoxPairInfo.
        :rtype: str
        """
        return self._local_view_box_name

    @local_view_box_name.setter
    def local_view_box_name(self, local_view_box_name):
        """
        Sets the local_view_box_name of this ViewBoxPairInfo.
        Specifies the name of the Storage Domain (View Box) on the local Cluster.

        :param local_view_box_name: The local_view_box_name of this ViewBoxPairInfo.
        :type: str
        """

        self._local_view_box_name = local_view_box_name

    @property
    def remote_view_box_id(self):
        """
        Gets the remote_view_box_id of this ViewBoxPairInfo.
        Specifies the id of the Storage Domain (View Box) on the remote Cluster.

        :return: The remote_view_box_id of this ViewBoxPairInfo.
        :rtype: int
        """
        return self._remote_view_box_id

    @remote_view_box_id.setter
    def remote_view_box_id(self, remote_view_box_id):
        """
        Sets the remote_view_box_id of this ViewBoxPairInfo.
        Specifies the id of the Storage Domain (View Box) on the remote Cluster.

        :param remote_view_box_id: The remote_view_box_id of this ViewBoxPairInfo.
        :type: int
        """

        self._remote_view_box_id = remote_view_box_id

    @property
    def remote_view_box_name(self):
        """
        Gets the remote_view_box_name of this ViewBoxPairInfo.
        Specifies the name of the Storage Domain (View Box) on the remote Cluster.

        :return: The remote_view_box_name of this ViewBoxPairInfo.
        :rtype: str
        """
        return self._remote_view_box_name

    @remote_view_box_name.setter
    def remote_view_box_name(self, remote_view_box_name):
        """
        Sets the remote_view_box_name of this ViewBoxPairInfo.
        Specifies the name of the Storage Domain (View Box) on the remote Cluster.

        :param remote_view_box_name: The remote_view_box_name of this ViewBoxPairInfo.
        :type: str
        """

        self._remote_view_box_name = remote_view_box_name

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