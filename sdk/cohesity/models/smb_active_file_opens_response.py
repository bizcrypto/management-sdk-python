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


class SmbActiveFileOpensResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, active_file_paths=None, cookie=None):
        """
        SmbActiveFileOpensResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'active_file_paths': 'list[SmbActiveFilePath]',
            'cookie': 'str'
        }

        self.attribute_map = {
            'active_file_paths': 'activeFilePaths',
            'cookie': 'cookie'
        }

        self._active_file_paths = active_file_paths
        self._cookie = cookie

    @property
    def active_file_paths(self):
        """
        Gets the active_file_paths of this SmbActiveFileOpensResponse.


        :return: The active_file_paths of this SmbActiveFileOpensResponse.
        :rtype: list[SmbActiveFilePath]
        """
        return self._active_file_paths

    @active_file_paths.setter
    def active_file_paths(self, active_file_paths):
        """
        Sets the active_file_paths of this SmbActiveFileOpensResponse.


        :param active_file_paths: The active_file_paths of this SmbActiveFileOpensResponse.
        :type: list[SmbActiveFilePath]
        """

        self._active_file_paths = active_file_paths

    @property
    def cookie(self):
        """
        Gets the cookie of this SmbActiveFileOpensResponse.
        Specifies an opaque string to pass to get the next set of active opens. If null is returned, this response is the last set of active opens.

        :return: The cookie of this SmbActiveFileOpensResponse.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie):
        """
        Sets the cookie of this SmbActiveFileOpensResponse.
        Specifies an opaque string to pass to get the next set of active opens. If null is returned, this response is the last set of active opens.

        :param cookie: The cookie of this SmbActiveFileOpensResponse.
        :type: str
        """

        self._cookie = cookie

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