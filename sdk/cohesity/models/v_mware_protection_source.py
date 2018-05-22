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


class VMwareProtectionSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, agent_id=None, agents=None, connection_state=None, datastore_info=None, folder_type=None, has_persistent_agent=None, host_type=None, id=None, name=None, tag_attributes=None, tools_running_status=None, type=None, virtual_disks=None):
        """
        VMwareProtectionSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'agent_id': 'int',
            'agents': 'list[AgentInformation]',
            'connection_state': 'str',
            'datastore_info': 'DatastoreInfo',
            'folder_type': 'str',
            'has_persistent_agent': 'bool',
            'host_type': 'str',
            'id': 'VMwareObjectId',
            'name': 'str',
            'tag_attributes': 'list[TagAttribute]',
            'tools_running_status': 'str',
            'type': 'str',
            'virtual_disks': 'list[VirtualDiskInfo]'
        }

        self.attribute_map = {
            'agent_id': 'agentId',
            'agents': 'agents',
            'connection_state': 'connectionState',
            'datastore_info': 'datastoreInfo',
            'folder_type': 'folderType',
            'has_persistent_agent': 'hasPersistentAgent',
            'host_type': 'hostType',
            'id': 'id',
            'name': 'name',
            'tag_attributes': 'tagAttributes',
            'tools_running_status': 'toolsRunningStatus',
            'type': 'type',
            'virtual_disks': 'virtualDisks'
        }

        self._agent_id = agent_id
        self._agents = agents
        self._connection_state = connection_state
        self._datastore_info = datastore_info
        self._folder_type = folder_type
        self._has_persistent_agent = has_persistent_agent
        self._host_type = host_type
        self._id = id
        self._name = name
        self._tag_attributes = tag_attributes
        self._tools_running_status = tools_running_status
        self._type = type
        self._virtual_disks = virtual_disks

    @property
    def agent_id(self):
        """
        Gets the agent_id of this VMwareProtectionSource.
        Specifies the id of the persistent agent.

        :return: The agent_id of this VMwareProtectionSource.
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this VMwareProtectionSource.
        Specifies the id of the persistent agent.

        :param agent_id: The agent_id of this VMwareProtectionSource.
        :type: int
        """

        self._agent_id = agent_id

    @property
    def agents(self):
        """
        Gets the agents of this VMwareProtectionSource.
        This is set only if the Virtual Machine has persistent agent.

        :return: The agents of this VMwareProtectionSource.
        :rtype: list[AgentInformation]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """
        Sets the agents of this VMwareProtectionSource.
        This is set only if the Virtual Machine has persistent agent.

        :param agents: The agents of this VMwareProtectionSource.
        :type: list[AgentInformation]
        """

        self._agents = agents

    @property
    def connection_state(self):
        """
        Gets the connection_state of this VMwareProtectionSource.
        Specifies the connection state of the Object and are only valid for ESXi hosts ('kHostSystem') or Virtual Machines ('kVirtualMachine'). These enums are equivalent to the connection states documented in VMware's reference documentation. Examples of Cohesity connection states include 'kConnected', 'kDisconnected', 'kInacccessible', etc.

        :return: The connection_state of this VMwareProtectionSource.
        :rtype: str
        """
        return self._connection_state

    @connection_state.setter
    def connection_state(self, connection_state):
        """
        Sets the connection_state of this VMwareProtectionSource.
        Specifies the connection state of the Object and are only valid for ESXi hosts ('kHostSystem') or Virtual Machines ('kVirtualMachine'). These enums are equivalent to the connection states documented in VMware's reference documentation. Examples of Cohesity connection states include 'kConnected', 'kDisconnected', 'kInacccessible', etc.

        :param connection_state: The connection_state of this VMwareProtectionSource.
        :type: str
        """
        allowed_values = ["kConnected", "kDisconnected", "kInacccessible", "kInvalid", "kOrphaned", "kNotResponding"]
        if connection_state not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_state` ({0}), must be one of {1}"
                .format(connection_state, allowed_values)
            )

        self._connection_state = connection_state

    @property
    def datastore_info(self):
        """
        Gets the datastore_info of this VMwareProtectionSource.
        Specifies additional information of entities of type 'kDatastore'.

        :return: The datastore_info of this VMwareProtectionSource.
        :rtype: DatastoreInfo
        """
        return self._datastore_info

    @datastore_info.setter
    def datastore_info(self, datastore_info):
        """
        Sets the datastore_info of this VMwareProtectionSource.
        Specifies additional information of entities of type 'kDatastore'.

        :param datastore_info: The datastore_info of this VMwareProtectionSource.
        :type: DatastoreInfo
        """

        self._datastore_info = datastore_info

    @property
    def folder_type(self):
        """
        Gets the folder_type of this VMwareProtectionSource.
        Specifies the folder type for the 'kFolder' Object. 'kVMFolder' indicates folder can hold VMs or vApps. 'kHostFolder' indicates folder can hold hosts and compute resources. 'kDatastoreFolder' indicates folder can hold datastores and storage pods. 'kNetworkFolder' indicates folder can hold networks and switches. 'kRootFolder' indicates folder can hold datacenters.

        :return: The folder_type of this VMwareProtectionSource.
        :rtype: str
        """
        return self._folder_type

    @folder_type.setter
    def folder_type(self, folder_type):
        """
        Sets the folder_type of this VMwareProtectionSource.
        Specifies the folder type for the 'kFolder' Object. 'kVMFolder' indicates folder can hold VMs or vApps. 'kHostFolder' indicates folder can hold hosts and compute resources. 'kDatastoreFolder' indicates folder can hold datastores and storage pods. 'kNetworkFolder' indicates folder can hold networks and switches. 'kRootFolder' indicates folder can hold datacenters.

        :param folder_type: The folder_type of this VMwareProtectionSource.
        :type: str
        """
        allowed_values = ["kVMFolder", "kHostFolder", "kDatastoreFolder", "kNetworkFolder", "kRootFolder"]
        if folder_type not in allowed_values:
            raise ValueError(
                "Invalid value for `folder_type` ({0}), must be one of {1}"
                .format(folder_type, allowed_values)
            )

        self._folder_type = folder_type

    @property
    def has_persistent_agent(self):
        """
        Gets the has_persistent_agent of this VMwareProtectionSource.
        Set to true if a persistent agent is running on the Virtual Machine. This is populated for entities of type 'kVirtualMachine'.

        :return: The has_persistent_agent of this VMwareProtectionSource.
        :rtype: bool
        """
        return self._has_persistent_agent

    @has_persistent_agent.setter
    def has_persistent_agent(self, has_persistent_agent):
        """
        Sets the has_persistent_agent of this VMwareProtectionSource.
        Set to true if a persistent agent is running on the Virtual Machine. This is populated for entities of type 'kVirtualMachine'.

        :param has_persistent_agent: The has_persistent_agent of this VMwareProtectionSource.
        :type: bool
        """

        self._has_persistent_agent = has_persistent_agent

    @property
    def host_type(self):
        """
        Gets the host_type of this VMwareProtectionSource.
        Specifies the host type for the 'kVirtualMachine' Object. 'kLinux' indicates the Linux operating system. 'kWindows' indicates the Microsoft Windows operating system.

        :return: The host_type of this VMwareProtectionSource.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        """
        Sets the host_type of this VMwareProtectionSource.
        Specifies the host type for the 'kVirtualMachine' Object. 'kLinux' indicates the Linux operating system. 'kWindows' indicates the Microsoft Windows operating system.

        :param host_type: The host_type of this VMwareProtectionSource.
        :type: str
        """
        allowed_values = ["kLinux", "kWindows"]
        if host_type not in allowed_values:
            raise ValueError(
                "Invalid value for `host_type` ({0}), must be one of {1}"
                .format(host_type, allowed_values)
            )

        self._host_type = host_type

    @property
    def id(self):
        """
        Gets the id of this VMwareProtectionSource.
        Specifies the UUID of the VMware Protection Source.

        :return: The id of this VMwareProtectionSource.
        :rtype: VMwareObjectId
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VMwareProtectionSource.
        Specifies the UUID of the VMware Protection Source.

        :param id: The id of this VMwareProtectionSource.
        :type: VMwareObjectId
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this VMwareProtectionSource.
        Specifies a human readable name of the Protection Source.

        :return: The name of this VMwareProtectionSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VMwareProtectionSource.
        Specifies a human readable name of the Protection Source.

        :param name: The name of this VMwareProtectionSource.
        :type: str
        """

        self._name = name

    @property
    def tag_attributes(self):
        """
        Gets the tag_attributes of this VMwareProtectionSource.
        Specifies the optional list of VM Tag attributes associated with this Object.

        :return: The tag_attributes of this VMwareProtectionSource.
        :rtype: list[TagAttribute]
        """
        return self._tag_attributes

    @tag_attributes.setter
    def tag_attributes(self, tag_attributes):
        """
        Sets the tag_attributes of this VMwareProtectionSource.
        Specifies the optional list of VM Tag attributes associated with this Object.

        :param tag_attributes: The tag_attributes of this VMwareProtectionSource.
        :type: list[TagAttribute]
        """

        self._tag_attributes = tag_attributes

    @property
    def tools_running_status(self):
        """
        Gets the tools_running_status of this VMwareProtectionSource.
        Specifies the status of VMware Tools for the guest OS on the VM. This is only valid for the 'kVirtualMachine' type. 'kGuestToolsRunning' means the VMware tools are running on the guest OS. 'kGuestToolsNotRunning' means the VMware tools are not running on the guest OS. 'kUnknown' means the state of the VMware tools on the guest OS is not known. 'kGuestToolsExecutingScripts' means the guest OS is currently executing scripts using VMware tools.

        :return: The tools_running_status of this VMwareProtectionSource.
        :rtype: str
        """
        return self._tools_running_status

    @tools_running_status.setter
    def tools_running_status(self, tools_running_status):
        """
        Sets the tools_running_status of this VMwareProtectionSource.
        Specifies the status of VMware Tools for the guest OS on the VM. This is only valid for the 'kVirtualMachine' type. 'kGuestToolsRunning' means the VMware tools are running on the guest OS. 'kGuestToolsNotRunning' means the VMware tools are not running on the guest OS. 'kUnknown' means the state of the VMware tools on the guest OS is not known. 'kGuestToolsExecutingScripts' means the guest OS is currently executing scripts using VMware tools.

        :param tools_running_status: The tools_running_status of this VMwareProtectionSource.
        :type: str
        """
        allowed_values = ["kUnknown", "kGuestToolsExecutingScripts", "kGuestToolsNotRunning", "kGuestToolsRunning"]
        if tools_running_status not in allowed_values:
            raise ValueError(
                "Invalid value for `tools_running_status` ({0}), must be one of {1}"
                .format(tools_running_status, allowed_values)
            )

        self._tools_running_status = tools_running_status

    @property
    def type(self):
        """
        Gets the type of this VMwareProtectionSource.
        Specifies the type of managed Object in a VMware Protection Source. Examples of VMware Objects include 'kVCenter', 'kFolder', 'kDatacenter', 'kResourcePool', 'kDatastore', 'kVirtualMachine', etc.

        :return: The type of this VMwareProtectionSource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VMwareProtectionSource.
        Specifies the type of managed Object in a VMware Protection Source. Examples of VMware Objects include 'kVCenter', 'kFolder', 'kDatacenter', 'kResourcePool', 'kDatastore', 'kVirtualMachine', etc.

        :param type: The type of this VMwareProtectionSource.
        :type: str
        """
        allowed_values = ["kVCenter", "kFolder", "kDatacenter", "kComputeResource", "kClusterComputeResource", "kResourcePool", "kDatastore", "kHostSystem", "kVirtualMachine", "kVirtualApp", "kStandaloneHost", "kStoragePod", "kNetwork", "kDistributedVirtualPortgroup", "kTagCategory", "kTag"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def virtual_disks(self):
        """
        Gets the virtual_disks of this VMwareProtectionSource.
        This is populated for entities of type 'kVirtualMachine'.

        :return: The virtual_disks of this VMwareProtectionSource.
        :rtype: list[VirtualDiskInfo]
        """
        return self._virtual_disks

    @virtual_disks.setter
    def virtual_disks(self, virtual_disks):
        """
        Sets the virtual_disks of this VMwareProtectionSource.
        This is populated for entities of type 'kVirtualMachine'.

        :param virtual_disks: The virtual_disks of this VMwareProtectionSource.
        :type: list[VirtualDiskInfo]
        """

        self._virtual_disks = virtual_disks

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