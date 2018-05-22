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


class CloseSmbFileOpenParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, file_path=None, open_id=None, view_name=None):
        """
        CloseSmbFileOpenParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file_path': 'str',
            'open_id': 'int',
            'view_name': 'str'
        }

        self.attribute_map = {
            'file_path': 'filePath',
            'open_id': 'openId',
            'view_name': 'viewName'
        }

        self._file_path = file_path
        self._open_id = open_id
        self._view_name = view_name

    @property
    def file_path(self):
        """
        Gets the file_path of this CloseSmbFileOpenParameters.
        Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified.

        :return: The file_path of this CloseSmbFileOpenParameters.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the file_path of this CloseSmbFileOpenParameters.
        Specifies the filepath in the view relative to the root filesystem. If this field is specified, viewName field must also be specified.

        :param file_path: The file_path of this CloseSmbFileOpenParameters.
        :type: str
        """

        self._file_path = file_path

    @property
    def open_id(self):
        """
        Gets the open_id of this CloseSmbFileOpenParameters.
        Specifies the id of the active open.

        :return: The open_id of this CloseSmbFileOpenParameters.
        :rtype: int
        """
        return self._open_id

    @open_id.setter
    def open_id(self, open_id):
        """
        Sets the open_id of this CloseSmbFileOpenParameters.
        Specifies the id of the active open.

        :param open_id: The open_id of this CloseSmbFileOpenParameters.
        :type: int
        """

        self._open_id = open_id

    @property
    def view_name(self):
        """
        Gets the view_name of this CloseSmbFileOpenParameters.
        Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified.

        :return: The view_name of this CloseSmbFileOpenParameters.
        :rtype: str
        """
        return self._view_name

    @view_name.setter
    def view_name(self, view_name):
        """
        Sets the view_name of this CloseSmbFileOpenParameters.
        Specifies the name of the View in which to search. If a view name is not specified, all the views in the Cluster is searched. This field is mandatory if filePath field is specified.

        :param view_name: The view_name of this CloseSmbFileOpenParameters.
        :type: str
        """

        self._view_name = view_name

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