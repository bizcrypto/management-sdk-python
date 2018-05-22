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


class HypervCloneParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, disable_network=None, network_id=None, powered_on=None, prefix=None, resource_id=None, suffix=None):
        """
        HypervCloneParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'disable_network': 'bool',
            'network_id': 'int',
            'powered_on': 'bool',
            'prefix': 'str',
            'resource_id': 'int',
            'suffix': 'str'
        }

        self.attribute_map = {
            'disable_network': 'disableNetwork',
            'network_id': 'networkId',
            'powered_on': 'poweredOn',
            'prefix': 'prefix',
            'resource_id': 'resourceId',
            'suffix': 'suffix'
        }

        self._disable_network = disable_network
        self._network_id = network_id
        self._powered_on = powered_on
        self._prefix = prefix
        self._resource_id = resource_id
        self._suffix = suffix

    @property
    def disable_network(self):
        """
        Gets the disable_network of this HypervCloneParameters.
        Specifies whether the network should be left in disabled state. Attached network is enabled by default. Set this flag to true to disable it.

        :return: The disable_network of this HypervCloneParameters.
        :rtype: bool
        """
        return self._disable_network

    @disable_network.setter
    def disable_network(self, disable_network):
        """
        Sets the disable_network of this HypervCloneParameters.
        Specifies whether the network should be left in disabled state. Attached network is enabled by default. Set this flag to true to disable it.

        :param disable_network: The disable_network of this HypervCloneParameters.
        :type: bool
        """

        self._disable_network = disable_network

    @property
    def network_id(self):
        """
        Gets the network_id of this HypervCloneParameters.
        Specifies a network configuration to be attached to the cloned or recovered object. For kCloneVMs and kRecoverVMs tasks, original network configuration is detached if the cloned or recovered object is kept under a different parent Protection Source or a different Resource Pool. By default, for kRecoverVMs task, original network configuration is preserved if the recovered object is kept under the same parent Protection Source and the same Resource Pool. Specify this field to override the preserved network configuration or to attach a new network configuration to the cloned or recovered objects. You can get the networkId of the kNetwork object by setting includeNetworks to 'true' in the GET /public/protectionSources operation. In the response, get the id of the desired kNetwork object, the resource pool, and the registered parent Protection Source.

        :return: The network_id of this HypervCloneParameters.
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """
        Sets the network_id of this HypervCloneParameters.
        Specifies a network configuration to be attached to the cloned or recovered object. For kCloneVMs and kRecoverVMs tasks, original network configuration is detached if the cloned or recovered object is kept under a different parent Protection Source or a different Resource Pool. By default, for kRecoverVMs task, original network configuration is preserved if the recovered object is kept under the same parent Protection Source and the same Resource Pool. Specify this field to override the preserved network configuration or to attach a new network configuration to the cloned or recovered objects. You can get the networkId of the kNetwork object by setting includeNetworks to 'true' in the GET /public/protectionSources operation. In the response, get the id of the desired kNetwork object, the resource pool, and the registered parent Protection Source.

        :param network_id: The network_id of this HypervCloneParameters.
        :type: int
        """

        self._network_id = network_id

    @property
    def powered_on(self):
        """
        Gets the powered_on of this HypervCloneParameters.
        Specifies the power state of the cloned or recovered objects. By default, the cloned or recovered objects are powered off.

        :return: The powered_on of this HypervCloneParameters.
        :rtype: bool
        """
        return self._powered_on

    @powered_on.setter
    def powered_on(self, powered_on):
        """
        Sets the powered_on of this HypervCloneParameters.
        Specifies the power state of the cloned or recovered objects. By default, the cloned or recovered objects are powered off.

        :param powered_on: The powered_on of this HypervCloneParameters.
        :type: bool
        """

        self._powered_on = powered_on

    @property
    def prefix(self):
        """
        Gets the prefix of this HypervCloneParameters.
        Specifies a prefix to prepended to the source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :return: The prefix of this HypervCloneParameters.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this HypervCloneParameters.
        Specifies a prefix to prepended to the source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :param prefix: The prefix of this HypervCloneParameters.
        :type: str
        """

        self._prefix = prefix

    @property
    def resource_id(self):
        """
        Gets the resource_id of this HypervCloneParameters.
        The resource (HyperV host) to which the restored VM will be attached.  This field is optional for a kRecoverVMs task if the VMs are being restored to its original parent source. If not specified, restored VMs will be attached to its original host. This field is mandatory if the VMs are being restored to a different parent source.

        :return: The resource_id of this HypervCloneParameters.
        :rtype: int
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this HypervCloneParameters.
        The resource (HyperV host) to which the restored VM will be attached.  This field is optional for a kRecoverVMs task if the VMs are being restored to its original parent source. If not specified, restored VMs will be attached to its original host. This field is mandatory if the VMs are being restored to a different parent source.

        :param resource_id: The resource_id of this HypervCloneParameters.
        :type: int
        """

        self._resource_id = resource_id

    @property
    def suffix(self):
        """
        Gets the suffix of this HypervCloneParameters.
        Specifies a suffix to appended to the original source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :return: The suffix of this HypervCloneParameters.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this HypervCloneParameters.
        Specifies a suffix to appended to the original source object name to derive a new name for the recovered or cloned object. By default, cloned or recovered objects retain their original name. Length of this field is limited to 8 characters.

        :param suffix: The suffix of this HypervCloneParameters.
        :type: str
        """

        self._suffix = suffix

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