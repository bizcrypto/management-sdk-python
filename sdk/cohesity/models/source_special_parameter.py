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


class SourceSpecialParameter(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, physical_special_parameters=None, skip_indexing=None, source_id=None, sql_special_parameters=None, truncate_exchange_log=None, vm_credentials=None, vmware_special_parameters=None):
        """
        SourceSpecialParameter - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'physical_special_parameters': 'PhysicalSpecialParameters',
            'skip_indexing': 'bool',
            'source_id': 'int',
            'sql_special_parameters': 'SqlSpecialParameters',
            'truncate_exchange_log': 'bool',
            'vm_credentials': 'SourceSpecialParameterVmCredentials',
            'vmware_special_parameters': 'VmwareSpecialParameters'
        }

        self.attribute_map = {
            'physical_special_parameters': 'physicalSpecialParameters',
            'skip_indexing': 'skipIndexing',
            'source_id': 'sourceId',
            'sql_special_parameters': 'sqlSpecialParameters',
            'truncate_exchange_log': 'truncateExchangeLog',
            'vm_credentials': 'vmCredentials',
            'vmware_special_parameters': 'vmwareSpecialParameters'
        }

        self._physical_special_parameters = physical_special_parameters
        self._skip_indexing = skip_indexing
        self._source_id = source_id
        self._sql_special_parameters = sql_special_parameters
        self._truncate_exchange_log = truncate_exchange_log
        self._vm_credentials = vm_credentials
        self._vmware_special_parameters = vmware_special_parameters

    @property
    def physical_special_parameters(self):
        """
        Gets the physical_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Sources of 'kHost' type in a kPhysical environment.

        :return: The physical_special_parameters of this SourceSpecialParameter.
        :rtype: PhysicalSpecialParameters
        """
        return self._physical_special_parameters

    @physical_special_parameters.setter
    def physical_special_parameters(self, physical_special_parameters):
        """
        Sets the physical_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Sources of 'kHost' type in a kPhysical environment.

        :param physical_special_parameters: The physical_special_parameters of this SourceSpecialParameter.
        :type: PhysicalSpecialParameters
        """

        self._physical_special_parameters = physical_special_parameters

    @property
    def skip_indexing(self):
        """
        Gets the skip_indexing of this SourceSpecialParameter.
        Specifies not to index the objects in the Protection Source when backing up.

        :return: The skip_indexing of this SourceSpecialParameter.
        :rtype: bool
        """
        return self._skip_indexing

    @skip_indexing.setter
    def skip_indexing(self, skip_indexing):
        """
        Sets the skip_indexing of this SourceSpecialParameter.
        Specifies not to index the objects in the Protection Source when backing up.

        :param skip_indexing: The skip_indexing of this SourceSpecialParameter.
        :type: bool
        """

        self._skip_indexing = skip_indexing

    @property
    def source_id(self):
        """
        Gets the source_id of this SourceSpecialParameter.
        Specifies the object id of the Protection Source that these special settings apply. This field must refer to a leaf node such a VM or a Physical Server.

        :return: The source_id of this SourceSpecialParameter.
        :rtype: int
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this SourceSpecialParameter.
        Specifies the object id of the Protection Source that these special settings apply. This field must refer to a leaf node such a VM or a Physical Server.

        :param source_id: The source_id of this SourceSpecialParameter.
        :type: int
        """

        self._source_id = source_id

    @property
    def sql_special_parameters(self):
        """
        Gets the sql_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Protection Sources of 'kSQL' type.

        :return: The sql_special_parameters of this SourceSpecialParameter.
        :rtype: SqlSpecialParameters
        """
        return self._sql_special_parameters

    @sql_special_parameters.setter
    def sql_special_parameters(self, sql_special_parameters):
        """
        Sets the sql_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Protection Sources of 'kSQL' type.

        :param sql_special_parameters: The sql_special_parameters of this SourceSpecialParameter.
        :type: SqlSpecialParameters
        """

        self._sql_special_parameters = sql_special_parameters

    @property
    def truncate_exchange_log(self):
        """
        Gets the truncate_exchange_log of this SourceSpecialParameter.
        If true, after the Cohesity Cluster successfully captures a Snapshot during a Job Run, the Cluster truncates the Exchange transaction logs on a Microsoft Exchange Server. The default value is false. This field is deprecated. Use the field in ApplicationParameters inside source specific parameter. deprecated: true

        :return: The truncate_exchange_log of this SourceSpecialParameter.
        :rtype: bool
        """
        return self._truncate_exchange_log

    @truncate_exchange_log.setter
    def truncate_exchange_log(self, truncate_exchange_log):
        """
        Sets the truncate_exchange_log of this SourceSpecialParameter.
        If true, after the Cohesity Cluster successfully captures a Snapshot during a Job Run, the Cluster truncates the Exchange transaction logs on a Microsoft Exchange Server. The default value is false. This field is deprecated. Use the field in ApplicationParameters inside source specific parameter. deprecated: true

        :param truncate_exchange_log: The truncate_exchange_log of this SourceSpecialParameter.
        :type: bool
        """

        self._truncate_exchange_log = truncate_exchange_log

    @property
    def vm_credentials(self):
        """
        Gets the vm_credentials of this SourceSpecialParameter.


        :return: The vm_credentials of this SourceSpecialParameter.
        :rtype: SourceSpecialParameterVmCredentials
        """
        return self._vm_credentials

    @vm_credentials.setter
    def vm_credentials(self, vm_credentials):
        """
        Sets the vm_credentials of this SourceSpecialParameter.


        :param vm_credentials: The vm_credentials of this SourceSpecialParameter.
        :type: SourceSpecialParameterVmCredentials
        """

        self._vm_credentials = vm_credentials

    @property
    def vmware_special_parameters(self):
        """
        Gets the vmware_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Protection Sources of 'kVMware' type.

        :return: The vmware_special_parameters of this SourceSpecialParameter.
        :rtype: VmwareSpecialParameters
        """
        return self._vmware_special_parameters

    @vmware_special_parameters.setter
    def vmware_special_parameters(self, vmware_special_parameters):
        """
        Sets the vmware_special_parameters of this SourceSpecialParameter.
        Specifies additional special parameters that are applicable only to Protection Sources of 'kVMware' type.

        :param vmware_special_parameters: The vmware_special_parameters of this SourceSpecialParameter.
        :type: VmwareSpecialParameters
        """

        self._vmware_special_parameters = vmware_special_parameters

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