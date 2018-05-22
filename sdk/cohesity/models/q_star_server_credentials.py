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


class QStarServerCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, host=None, integral_volume_names=None, password=None, port=None, share_type=None, use_https=None, username=None):
        """
        QStarServerCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'host': 'str',
            'integral_volume_names': 'list[str]',
            'password': 'str',
            'port': 'int',
            'share_type': 'str',
            'use_https': 'bool',
            'username': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'integral_volume_names': 'integralVolumeNames',
            'password': 'password',
            'port': 'port',
            'share_type': 'shareType',
            'use_https': 'useHttps',
            'username': 'username'
        }

        self._host = host
        self._integral_volume_names = integral_volume_names
        self._password = password
        self._port = port
        self._share_type = share_type
        self._use_https = use_https
        self._username = username

    @property
    def host(self):
        """
        Gets the host of this QStarServerCredentials.
        Specifies the IP address or DNS name of the server where QStar service is running.

        :return: The host of this QStarServerCredentials.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this QStarServerCredentials.
        Specifies the IP address or DNS name of the server where QStar service is running.

        :param host: The host of this QStarServerCredentials.
        :type: str
        """

        self._host = host

    @property
    def integral_volume_names(self):
        """
        Gets the integral_volume_names of this QStarServerCredentials.
        Specifies a list of existing Integral Volume names available on the QStar server for storing objects.

        :return: The integral_volume_names of this QStarServerCredentials.
        :rtype: list[str]
        """
        return self._integral_volume_names

    @integral_volume_names.setter
    def integral_volume_names(self, integral_volume_names):
        """
        Sets the integral_volume_names of this QStarServerCredentials.
        Specifies a list of existing Integral Volume names available on the QStar server for storing objects.

        :param integral_volume_names: The integral_volume_names of this QStarServerCredentials.
        :type: list[str]
        """

        self._integral_volume_names = integral_volume_names

    @property
    def password(self):
        """
        Gets the password of this QStarServerCredentials.
        Specifies the password used to access the QStar host.

        :return: The password of this QStarServerCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this QStarServerCredentials.
        Specifies the password used to access the QStar host.

        :param password: The password of this QStarServerCredentials.
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """
        Gets the port of this QStarServerCredentials.
        Specifies the listening port where QStar WEB API service is running.

        :return: The port of this QStarServerCredentials.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this QStarServerCredentials.
        Specifies the listening port where QStar WEB API service is running.

        :param port: The port of this QStarServerCredentials.
        :type: int
        """

        self._port = port

    @property
    def share_type(self):
        """
        Gets the share_type of this QStarServerCredentials.
        Specifies the sharing protocol type used by QStar to mount the integral volume. See the Cohesity online help for the recommended protocol for your environment.

        :return: The share_type of this QStarServerCredentials.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """
        Sets the share_type of this QStarServerCredentials.
        Specifies the sharing protocol type used by QStar to mount the integral volume. See the Cohesity online help for the recommended protocol for your environment.

        :param share_type: The share_type of this QStarServerCredentials.
        :type: str
        """

        self._share_type = share_type

    @property
    def use_https(self):
        """
        Gets the use_https of this QStarServerCredentials.
        Specifies whether to use http or https to connect to the service. If true, a secure connection (https) is used.

        :return: The use_https of this QStarServerCredentials.
        :rtype: bool
        """
        return self._use_https

    @use_https.setter
    def use_https(self, use_https):
        """
        Sets the use_https of this QStarServerCredentials.
        Specifies whether to use http or https to connect to the service. If true, a secure connection (https) is used.

        :param use_https: The use_https of this QStarServerCredentials.
        :type: bool
        """

        self._use_https = use_https

    @property
    def username(self):
        """
        Gets the username of this QStarServerCredentials.
        Specifies the account name used to access the QStar host.

        :return: The username of this QStarServerCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this QStarServerCredentials.
        Specifies the account name used to access the QStar host.

        :param username: The username of this QStarServerCredentials.
        :type: str
        """

        self._username = username

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