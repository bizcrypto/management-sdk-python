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


class NasCredentials(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, host=None, mount_path=None, password=None, share_type=None, username=None):
        """
        NasCredentials - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'host': 'str',
            'mount_path': 'str',
            'password': 'str',
            'share_type': 'str',
            'username': 'str'
        }

        self.attribute_map = {
            'host': 'host',
            'mount_path': 'mountPath',
            'password': 'password',
            'share_type': 'shareType',
            'username': 'username'
        }

        self._host = host
        self._mount_path = mount_path
        self._password = password
        self._share_type = share_type
        self._username = username

    @property
    def host(self):
        """
        Gets the host of this NasCredentials.
        Specifies the hostname or IP address of the NAS server.

        :return: The host of this NasCredentials.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this NasCredentials.
        Specifies the hostname or IP address of the NAS server.

        :param host: The host of this NasCredentials.
        :type: str
        """

        self._host = host

    @property
    def mount_path(self):
        """
        Gets the mount_path of this NasCredentials.
        Specifies the mount path to the NAS server.

        :return: The mount_path of this NasCredentials.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """
        Sets the mount_path of this NasCredentials.
        Specifies the mount path to the NAS server.

        :param mount_path: The mount_path of this NasCredentials.
        :type: str
        """

        self._mount_path = mount_path

    @property
    def password(self):
        """
        Gets the password of this NasCredentials.
        If using the CIFS protocol and a Username was specified, specify the password for the username.

        :return: The password of this NasCredentials.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this NasCredentials.
        If using the CIFS protocol and a Username was specified, specify the password for the username.

        :param password: The password of this NasCredentials.
        :type: str
        """

        self._password = password

    @property
    def share_type(self):
        """
        Gets the share_type of this NasCredentials.
        Specifies the sharing protocol type used to mount the file system. Currently, only NFS is supported. 'kNFS' indicates use the NFS protocol to mount the file system. 'kCIFS' indicates use the CIFS protocol to mount the file system.

        :return: The share_type of this NasCredentials.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """
        Sets the share_type of this NasCredentials.
        Specifies the sharing protocol type used to mount the file system. Currently, only NFS is supported. 'kNFS' indicates use the NFS protocol to mount the file system. 'kCIFS' indicates use the CIFS protocol to mount the file system.

        :param share_type: The share_type of this NasCredentials.
        :type: str
        """
        allowed_values = ["kNFS", "kCIFS"]
        if share_type not in allowed_values:
            raise ValueError(
                "Invalid value for `share_type` ({0}), must be one of {1}"
                .format(share_type, allowed_values)
            )

        self._share_type = share_type

    @property
    def username(self):
        """
        Gets the username of this NasCredentials.
        If using the CIFS protocol, you can optional specify a username to use when mounting.

        :return: The username of this NasCredentials.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this NasCredentials.
        If using the CIFS protocol, you can optional specify a username to use when mounting.

        :param username: The username of this NasCredentials.
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