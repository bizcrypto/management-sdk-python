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


class GetMRJarUploadPathResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, error=None, jar_upload_path=None):
        """
        GetMRJarUploadPathResult - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error': 'ErrorProto',
            'jar_upload_path': 'str'
        }

        self.attribute_map = {
            'error': 'error',
            'jar_upload_path': 'jarUploadPath'
        }

        self._error = error
        self._jar_upload_path = jar_upload_path

    @property
    def error(self):
        """
        Gets the error of this GetMRJarUploadPathResult.
        Status code for this http rpc.

        :return: The error of this GetMRJarUploadPathResult.
        :rtype: ErrorProto
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this GetMRJarUploadPathResult.
        Status code for this http rpc.

        :param error: The error of this GetMRJarUploadPathResult.
        :type: ErrorProto
        """

        self._error = error

    @property
    def jar_upload_path(self):
        """
        Gets the jar_upload_path of this GetMRJarUploadPathResult.
        Path where Jars can be uploaded by Iris.

        :return: The jar_upload_path of this GetMRJarUploadPathResult.
        :rtype: str
        """
        return self._jar_upload_path

    @jar_upload_path.setter
    def jar_upload_path(self, jar_upload_path):
        """
        Sets the jar_upload_path of this GetMRJarUploadPathResult.
        Path where Jars can be uploaded by Iris.

        :param jar_upload_path: The jar_upload_path of this GetMRJarUploadPathResult.
        :type: str
        """

        self._jar_upload_path = jar_upload_path

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