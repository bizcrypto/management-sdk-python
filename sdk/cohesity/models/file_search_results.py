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


class FileSearchResults(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, files=None, total_count=None):
        """
        FileSearchResults - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'files': 'list[FileSearchResult]',
            'total_count': 'int'
        }

        self.attribute_map = {
            'files': 'files',
            'total_count': 'totalCount'
        }

        self._files = files
        self._total_count = total_count

    @property
    def files(self):
        """
        Gets the files of this FileSearchResults.
        Specifies the list of files and folders returned by this request that match the specified search and filter criteria. The number of files returned is limited by the pageCount field.

        :return: The files of this FileSearchResults.
        :rtype: list[FileSearchResult]
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this FileSearchResults.
        Specifies the list of files and folders returned by this request that match the specified search and filter criteria. The number of files returned is limited by the pageCount field.

        :param files: The files of this FileSearchResults.
        :type: list[FileSearchResult]
        """

        self._files = files

    @property
    def total_count(self):
        """
        Gets the total_count of this FileSearchResults.
        Specifies the total number of files and folders that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result.

        :return: The total_count of this FileSearchResults.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this FileSearchResults.
        Specifies the total number of files and folders that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result.

        :param total_count: The total_count of this FileSearchResults.
        :type: int
        """

        self._total_count = total_count

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