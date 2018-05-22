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


class ActiveDirectoryEntry(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, domain_name=None, fallback_user_id_mapping_info=None, machine_accounts=None, ou_name=None, password=None, trusted_domains=None, unix_root_sid=None, user_id_mapping_info=None, user_name=None, workgroup=None):
        """
        ActiveDirectoryEntry - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'domain_name': 'str',
            'fallback_user_id_mapping_info': 'UserIdMapping',
            'machine_accounts': 'list[str]',
            'ou_name': 'str',
            'password': 'str',
            'trusted_domains': 'list[str]',
            'unix_root_sid': 'str',
            'user_id_mapping_info': 'UserIdMapping',
            'user_name': 'str',
            'workgroup': 'str'
        }

        self.attribute_map = {
            'domain_name': 'domainName',
            'fallback_user_id_mapping_info': 'fallbackUserIdMappingInfo',
            'machine_accounts': 'machineAccounts',
            'ou_name': 'ouName',
            'password': 'password',
            'trusted_domains': 'trustedDomains',
            'unix_root_sid': 'unixRootSid',
            'user_id_mapping_info': 'userIdMappingInfo',
            'user_name': 'userName',
            'workgroup': 'workgroup'
        }

        self._domain_name = domain_name
        self._fallback_user_id_mapping_info = fallback_user_id_mapping_info
        self._machine_accounts = machine_accounts
        self._ou_name = ou_name
        self._password = password
        self._trusted_domains = trusted_domains
        self._unix_root_sid = unix_root_sid
        self._user_id_mapping_info = user_id_mapping_info
        self._user_name = user_name
        self._workgroup = workgroup

    @property
    def domain_name(self):
        """
        Gets the domain_name of this ActiveDirectoryEntry.
        Specifies the fully qualified domain name (FQDN) of an Active Directory.

        :return: The domain_name of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """
        Sets the domain_name of this ActiveDirectoryEntry.
        Specifies the fully qualified domain name (FQDN) of an Active Directory.

        :param domain_name: The domain_name of this ActiveDirectoryEntry.
        :type: str
        """

        self._domain_name = domain_name

    @property
    def fallback_user_id_mapping_info(self):
        """
        Gets the fallback_user_id_mapping_info of this ActiveDirectoryEntry.
        Specifies the fallback id mapping info which is used when an ID mapping for a user is not found via the above IdMappingInfo. Only supported for two types of fallback mapping types - 'kRid' and 'kFixed'.

        :return: The fallback_user_id_mapping_info of this ActiveDirectoryEntry.
        :rtype: UserIdMapping
        """
        return self._fallback_user_id_mapping_info

    @fallback_user_id_mapping_info.setter
    def fallback_user_id_mapping_info(self, fallback_user_id_mapping_info):
        """
        Sets the fallback_user_id_mapping_info of this ActiveDirectoryEntry.
        Specifies the fallback id mapping info which is used when an ID mapping for a user is not found via the above IdMappingInfo. Only supported for two types of fallback mapping types - 'kRid' and 'kFixed'.

        :param fallback_user_id_mapping_info: The fallback_user_id_mapping_info of this ActiveDirectoryEntry.
        :type: UserIdMapping
        """

        self._fallback_user_id_mapping_info = fallback_user_id_mapping_info

    @property
    def machine_accounts(self):
        """
        Gets the machine_accounts of this ActiveDirectoryEntry.
        Specifies an array of computer names used to identify the Cohesity Cluster on the domain.

        :return: The machine_accounts of this ActiveDirectoryEntry.
        :rtype: list[str]
        """
        return self._machine_accounts

    @machine_accounts.setter
    def machine_accounts(self, machine_accounts):
        """
        Sets the machine_accounts of this ActiveDirectoryEntry.
        Specifies an array of computer names used to identify the Cohesity Cluster on the domain.

        :param machine_accounts: The machine_accounts of this ActiveDirectoryEntry.
        :type: list[str]
        """

        self._machine_accounts = machine_accounts

    @property
    def ou_name(self):
        """
        Gets the ou_name of this ActiveDirectoryEntry.
        Specifies an optional Organizational Unit name.

        :return: The ou_name of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """
        Sets the ou_name of this ActiveDirectoryEntry.
        Specifies an optional Organizational Unit name.

        :param ou_name: The ou_name of this ActiveDirectoryEntry.
        :type: str
        """

        self._ou_name = ou_name

    @property
    def password(self):
        """
        Gets the password of this ActiveDirectoryEntry.
        Specifies the password for the specified userName.

        :return: The password of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ActiveDirectoryEntry.
        Specifies the password for the specified userName.

        :param password: The password of this ActiveDirectoryEntry.
        :type: str
        """

        self._password = password

    @property
    def trusted_domains(self):
        """
        Gets the trusted_domains of this ActiveDirectoryEntry.


        :return: The trusted_domains of this ActiveDirectoryEntry.
        :rtype: list[str]
        """
        return self._trusted_domains

    @trusted_domains.setter
    def trusted_domains(self, trusted_domains):
        """
        Sets the trusted_domains of this ActiveDirectoryEntry.


        :param trusted_domains: The trusted_domains of this ActiveDirectoryEntry.
        :type: list[str]
        """

        self._trusted_domains = trusted_domains

    @property
    def unix_root_sid(self):
        """
        Gets the unix_root_sid of this ActiveDirectoryEntry.
        Specifies the SID of the Active Directory domain user to be mapped to Unix root user.

        :return: The unix_root_sid of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._unix_root_sid

    @unix_root_sid.setter
    def unix_root_sid(self, unix_root_sid):
        """
        Sets the unix_root_sid of this ActiveDirectoryEntry.
        Specifies the SID of the Active Directory domain user to be mapped to Unix root user.

        :param unix_root_sid: The unix_root_sid of this ActiveDirectoryEntry.
        :type: str
        """

        self._unix_root_sid = unix_root_sid

    @property
    def user_id_mapping_info(self):
        """
        Gets the user_id_mapping_info of this ActiveDirectoryEntry.
        Specifies the information about how the Unix and Windows users are mapped for this domain.

        :return: The user_id_mapping_info of this ActiveDirectoryEntry.
        :rtype: UserIdMapping
        """
        return self._user_id_mapping_info

    @user_id_mapping_info.setter
    def user_id_mapping_info(self, user_id_mapping_info):
        """
        Sets the user_id_mapping_info of this ActiveDirectoryEntry.
        Specifies the information about how the Unix and Windows users are mapped for this domain.

        :param user_id_mapping_info: The user_id_mapping_info of this ActiveDirectoryEntry.
        :type: UserIdMapping
        """

        self._user_id_mapping_info = user_id_mapping_info

    @property
    def user_name(self):
        """
        Gets the user_name of this ActiveDirectoryEntry.
        Specifies a userName that has administrative privileges in the domain.

        :return: The user_name of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """
        Sets the user_name of this ActiveDirectoryEntry.
        Specifies a userName that has administrative privileges in the domain.

        :param user_name: The user_name of this ActiveDirectoryEntry.
        :type: str
        """

        self._user_name = user_name

    @property
    def workgroup(self):
        """
        Gets the workgroup of this ActiveDirectoryEntry.
        Specifies an optional Workgroup name.

        :return: The workgroup of this ActiveDirectoryEntry.
        :rtype: str
        """
        return self._workgroup

    @workgroup.setter
    def workgroup(self, workgroup):
        """
        Sets the workgroup of this ActiveDirectoryEntry.
        Specifies an optional Workgroup name.

        :param workgroup: The workgroup of this ActiveDirectoryEntry.
        :type: str
        """

        self._workgroup = workgroup

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