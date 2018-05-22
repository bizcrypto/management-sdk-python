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


class SyslogServer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, address=None, is_cluster_auditing_enabled=None, is_filer_auditing_enabled=None, name=None, port=None, protocol=None):
        """
        SyslogServer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'address': 'str',
            'is_cluster_auditing_enabled': 'bool',
            'is_filer_auditing_enabled': 'bool',
            'name': 'str',
            'port': 'int',
            'protocol': 'str'
        }

        self.attribute_map = {
            'address': 'address',
            'is_cluster_auditing_enabled': 'isClusterAuditingEnabled',
            'is_filer_auditing_enabled': 'isFilerAuditingEnabled',
            'name': 'name',
            'port': 'port',
            'protocol': 'protocol'
        }

        self._address = address
        self._is_cluster_auditing_enabled = is_cluster_auditing_enabled
        self._is_filer_auditing_enabled = is_filer_auditing_enabled
        self._name = name
        self._port = port
        self._protocol = protocol

    @property
    def address(self):
        """
        Gets the address of this SyslogServer.
        Specifies the IP address or hostname of the syslog server.

        :return: The address of this SyslogServer.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this SyslogServer.
        Specifies the IP address or hostname of the syslog server.

        :param address: The address of this SyslogServer.
        :type: str
        """

        self._address = address

    @property
    def is_cluster_auditing_enabled(self):
        """
        Gets the is_cluster_auditing_enabled of this SyslogServer.
        Specifies if Cluster audit logs should be sent to this syslog server. If 'true', Cluster audit logs are sent to the syslog server. (default) If 'false', Cluster audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled.

        :return: The is_cluster_auditing_enabled of this SyslogServer.
        :rtype: bool
        """
        return self._is_cluster_auditing_enabled

    @is_cluster_auditing_enabled.setter
    def is_cluster_auditing_enabled(self, is_cluster_auditing_enabled):
        """
        Sets the is_cluster_auditing_enabled of this SyslogServer.
        Specifies if Cluster audit logs should be sent to this syslog server. If 'true', Cluster audit logs are sent to the syslog server. (default) If 'false', Cluster audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled.

        :param is_cluster_auditing_enabled: The is_cluster_auditing_enabled of this SyslogServer.
        :type: bool
        """

        self._is_cluster_auditing_enabled = is_cluster_auditing_enabled

    @property
    def is_filer_auditing_enabled(self):
        """
        Gets the is_filer_auditing_enabled of this SyslogServer.
        Specifies if filer audit logs should be sent to this syslog server. If 'true', filer audit logs are sent to the syslog server. (default) If 'false', filer audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled.

        :return: The is_filer_auditing_enabled of this SyslogServer.
        :rtype: bool
        """
        return self._is_filer_auditing_enabled

    @is_filer_auditing_enabled.setter
    def is_filer_auditing_enabled(self, is_filer_auditing_enabled):
        """
        Sets the is_filer_auditing_enabled of this SyslogServer.
        Specifies if filer audit logs should be sent to this syslog server. If 'true', filer audit logs are sent to the syslog server. (default) If 'false', filer audit logs are not sent to the syslog server. Either cluster audit logs or filer audit logs should be enabled.

        :param is_filer_auditing_enabled: The is_filer_auditing_enabled of this SyslogServer.
        :type: bool
        """

        self._is_filer_auditing_enabled = is_filer_auditing_enabled

    @property
    def name(self):
        """
        Gets the name of this SyslogServer.
        Specifies a unique name for the syslog server on the Cluster.

        :return: The name of this SyslogServer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SyslogServer.
        Specifies a unique name for the syslog server on the Cluster.

        :param name: The name of this SyslogServer.
        :type: str
        """

        self._name = name

    @property
    def port(self):
        """
        Gets the port of this SyslogServer.
        Specifies the port where the syslog server listens.

        :return: The port of this SyslogServer.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this SyslogServer.
        Specifies the port where the syslog server listens.

        :param port: The port of this SyslogServer.
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """
        Gets the protocol of this SyslogServer.
        Specifies the protocol used to send the logs. Specifies the protocol used to communicate to a server. e.g., kUDP, kTCP.  'kUDP' indicates UDP protocol. 'kTCP' indicates TCP protocol.

        :return: The protocol of this SyslogServer.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this SyslogServer.
        Specifies the protocol used to send the logs. Specifies the protocol used to communicate to a server. e.g., kUDP, kTCP.  'kUDP' indicates UDP protocol. 'kTCP' indicates TCP protocol.

        :param protocol: The protocol of this SyslogServer.
        :type: str
        """
        allowed_values = ["kUDP", "kTCP"]
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

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