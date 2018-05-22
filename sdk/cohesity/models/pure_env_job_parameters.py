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


class PureEnvJobParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, max_snapshots_on_primary=None):
        """
        PureEnvJobParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'max_snapshots_on_primary': 'int'
        }

        self.attribute_map = {
            'max_snapshots_on_primary': 'maxSnapshotsOnPrimary'
        }

        self._max_snapshots_on_primary = max_snapshots_on_primary

    @property
    def max_snapshots_on_primary(self):
        """
        Gets the max_snapshots_on_primary of this PureEnvJobParameters.
        Specifies how many recent snapshots of each backed up entity to retain on the primary environment. If not specified, then snapshots will not be be deleted from the primary environment.

        :return: The max_snapshots_on_primary of this PureEnvJobParameters.
        :rtype: int
        """
        return self._max_snapshots_on_primary

    @max_snapshots_on_primary.setter
    def max_snapshots_on_primary(self, max_snapshots_on_primary):
        """
        Sets the max_snapshots_on_primary of this PureEnvJobParameters.
        Specifies how many recent snapshots of each backed up entity to retain on the primary environment. If not specified, then snapshots will not be be deleted from the primary environment.

        :param max_snapshots_on_primary: The max_snapshots_on_primary of this PureEnvJobParameters.
        :type: int
        """

        self._max_snapshots_on_primary = max_snapshots_on_primary

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