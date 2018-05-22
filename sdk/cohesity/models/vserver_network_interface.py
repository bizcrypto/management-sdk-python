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


class VserverNetworkInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, data_protocols=None, ip_address=None, name=None):
        """
        VserverNetworkInterface - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_protocols': 'list[str]',
            'ip_address': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'data_protocols': 'dataProtocols',
            'ip_address': 'ipAddress',
            'name': 'name'
        }

        self._data_protocols = data_protocols
        self._ip_address = ip_address
        self._name = name

    @property
    def data_protocols(self):
        """
        Gets the data_protocols of this VserverNetworkInterface.
        Specifies the set of data protocols supported by this interface. 'kNfs' indicates NFS connections. 'kCifs' indicates SMB (CIFS) connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates Fiber Channel connections. 'kFcache' indicates Flex Cache connections. 'kHttp' indicates HTTP connections. 'kNdmp' indicates NDMP connections. 'kManagement' indicates non-data connections used for management purposes.

        :return: The data_protocols of this VserverNetworkInterface.
        :rtype: list[str]
        """
        return self._data_protocols

    @data_protocols.setter
    def data_protocols(self, data_protocols):
        """
        Sets the data_protocols of this VserverNetworkInterface.
        Specifies the set of data protocols supported by this interface. 'kNfs' indicates NFS connections. 'kCifs' indicates SMB (CIFS) connections. 'kIscsi' indicates iSCSI connections. 'kFc' indicates Fiber Channel connections. 'kFcache' indicates Flex Cache connections. 'kHttp' indicates HTTP connections. 'kNdmp' indicates NDMP connections. 'kManagement' indicates non-data connections used for management purposes.

        :param data_protocols: The data_protocols of this VserverNetworkInterface.
        :type: list[str]
        """
        allowed_values = ["kNfs", "kCifs", "kIscsi", "kFc", "kFcache", "kHttp", "kNdmp", "kManagement"]
        if data_protocols not in allowed_values:
            raise ValueError(
                "Invalid value for `data_protocols` ({0}), must be one of {1}"
                .format(data_protocols, allowed_values)
            )

        self._data_protocols = data_protocols

    @property
    def ip_address(self):
        """
        Gets the ip_address of this VserverNetworkInterface.
        Specifies the IP address of this interface.

        :return: The ip_address of this VserverNetworkInterface.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this VserverNetworkInterface.
        Specifies the IP address of this interface.

        :param ip_address: The ip_address of this VserverNetworkInterface.
        :type: str
        """

        self._ip_address = ip_address

    @property
    def name(self):
        """
        Gets the name of this VserverNetworkInterface.
        Specifies the name of this interface.

        :return: The name of this VserverNetworkInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VserverNetworkInterface.
        Specifies the name of this interface.

        :param name: The name of this VserverNetworkInterface.
        :type: str
        """

        self._name = name

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