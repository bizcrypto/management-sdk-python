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


class AzureCloudCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, storage_access_key=None, storage_account_name=None):
        """
        AzureCloudCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'storage_access_key': 'str',
            'storage_account_name': 'str'
        }

        self.attribute_map = {
            'storage_access_key': 'storageAccessKey',
            'storage_account_name': 'storageAccountName'
        }

        self._storage_access_key = storage_access_key
        self._storage_account_name = storage_account_name

    @property
    def storage_access_key(self):
        """
        Gets the storage_access_key of this AzureCloudCredentials.
        Specifies the access key to use when accessing a storage tier in a Azure cloud service.

        :return: The storage_access_key of this AzureCloudCredentials.
        :rtype: str
        """
        return self._storage_access_key

    @storage_access_key.setter
    def storage_access_key(self, storage_access_key):
        """
        Sets the storage_access_key of this AzureCloudCredentials.
        Specifies the access key to use when accessing a storage tier in a Azure cloud service.

        :param storage_access_key: The storage_access_key of this AzureCloudCredentials.
        :type: str
        """

        self._storage_access_key = storage_access_key

    @property
    def storage_account_name(self):
        """
        Gets the storage_account_name of this AzureCloudCredentials.
        Specifies the account name to use when accessing a storage tier in a Azure cloud service.

        :return: The storage_account_name of this AzureCloudCredentials.
        :rtype: str
        """
        return self._storage_account_name

    @storage_account_name.setter
    def storage_account_name(self, storage_account_name):
        """
        Sets the storage_account_name of this AzureCloudCredentials.
        Specifies the account name to use when accessing a storage tier in a Azure cloud service.

        :param storage_account_name: The storage_account_name of this AzureCloudCredentials.
        :type: str
        """

        self._storage_account_name = storage_account_name

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