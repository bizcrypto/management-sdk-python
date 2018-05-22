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


class AgentInformation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cbmr_version=None, id=None, name=None, registration_info=None, source_side_dedup_enabled=None, status=None, status_message=None, upgradability=None, upgrade_status=None, upgrade_status_message=None, version=None):
        """
        AgentInformation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cbmr_version': 'str',
            'id': 'int',
            'name': 'str',
            'registration_info': 'RegisteredSourceInfo',
            'source_side_dedup_enabled': 'bool',
            'status': 'str',
            'status_message': 'str',
            'upgradability': 'str',
            'upgrade_status': 'str',
            'upgrade_status_message': 'str',
            'version': 'str'
        }

        self.attribute_map = {
            'cbmr_version': 'cbmrVersion',
            'id': 'id',
            'name': 'name',
            'registration_info': 'registrationInfo',
            'source_side_dedup_enabled': 'sourceSideDedupEnabled',
            'status': 'status',
            'status_message': 'statusMessage',
            'upgradability': 'upgradability',
            'upgrade_status': 'upgradeStatus',
            'upgrade_status_message': 'upgradeStatusMessage',
            'version': 'version'
        }

        self._cbmr_version = cbmr_version
        self._id = id
        self._name = name
        self._registration_info = registration_info
        self._source_side_dedup_enabled = source_side_dedup_enabled
        self._status = status
        self._status_message = status_message
        self._upgradability = upgradability
        self._upgrade_status = upgrade_status
        self._upgrade_status_message = upgrade_status_message
        self._version = version

    @property
    def cbmr_version(self):
        """
        Gets the cbmr_version of this AgentInformation.
        Specifies the version if Cristie BMR product is installed on the host.

        :return: The cbmr_version of this AgentInformation.
        :rtype: str
        """
        return self._cbmr_version

    @cbmr_version.setter
    def cbmr_version(self, cbmr_version):
        """
        Sets the cbmr_version of this AgentInformation.
        Specifies the version if Cristie BMR product is installed on the host.

        :param cbmr_version: The cbmr_version of this AgentInformation.
        :type: str
        """

        self._cbmr_version = cbmr_version

    @property
    def id(self):
        """
        Gets the id of this AgentInformation.
        Specifies the agent's id.

        :return: The id of this AgentInformation.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AgentInformation.
        Specifies the agent's id.

        :param id: The id of this AgentInformation.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AgentInformation.
        Specifies the agent's name.

        :return: The name of this AgentInformation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AgentInformation.
        Specifies the agent's name.

        :param name: The name of this AgentInformation.
        :type: str
        """

        self._name = name

    @property
    def registration_info(self):
        """
        Gets the registration_info of this AgentInformation.
        Specifies registration information for an Agent.

        :return: The registration_info of this AgentInformation.
        :rtype: RegisteredSourceInfo
        """
        return self._registration_info

    @registration_info.setter
    def registration_info(self, registration_info):
        """
        Sets the registration_info of this AgentInformation.
        Specifies registration information for an Agent.

        :param registration_info: The registration_info of this AgentInformation.
        :type: RegisteredSourceInfo
        """

        self._registration_info = registration_info

    @property
    def source_side_dedup_enabled(self):
        """
        Gets the source_side_dedup_enabled of this AgentInformation.
        Specifies whether source side dedup is enabled or not.

        :return: The source_side_dedup_enabled of this AgentInformation.
        :rtype: bool
        """
        return self._source_side_dedup_enabled

    @source_side_dedup_enabled.setter
    def source_side_dedup_enabled(self, source_side_dedup_enabled):
        """
        Sets the source_side_dedup_enabled of this AgentInformation.
        Specifies whether source side dedup is enabled or not.

        :param source_side_dedup_enabled: The source_side_dedup_enabled of this AgentInformation.
        :type: bool
        """

        self._source_side_dedup_enabled = source_side_dedup_enabled

    @property
    def status(self):
        """
        Gets the status of this AgentInformation.
        Specifies the agent status. Specifies the status of the agent running on a physical source. 'kUnknown' indicates the Agent is not known. No attempt to connect to the Agent has occurred. 'kUnreachable' indicates the Agent is not reachable. 'kHealthy' indicates the Agent is healthy. 'kDegraded' indicates the Agent is running but in a degraded state.

        :return: The status of this AgentInformation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AgentInformation.
        Specifies the agent status. Specifies the status of the agent running on a physical source. 'kUnknown' indicates the Agent is not known. No attempt to connect to the Agent has occurred. 'kUnreachable' indicates the Agent is not reachable. 'kHealthy' indicates the Agent is healthy. 'kDegraded' indicates the Agent is running but in a degraded state.

        :param status: The status of this AgentInformation.
        :type: str
        """
        allowed_values = ["kUnknown", "kUnreachable", "kHealthy", "kDegraded"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """
        Gets the status_message of this AgentInformation.
        Specifies additional details about the agent status.

        :return: The status_message of this AgentInformation.
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """
        Sets the status_message of this AgentInformation.
        Specifies additional details about the agent status.

        :param status_message: The status_message of this AgentInformation.
        :type: str
        """

        self._status_message = status_message

    @property
    def upgradability(self):
        """
        Gets the upgradability of this AgentInformation.
        Specifies the upgradability of the agent running on the physical server. Specifies the upgradability of the agent running on the physical server. 'kUpgradable' indicates the Agent can be upgraded to the agent software version on the cluster. 'kCurrent' indicates the Agent is running the latest version. 'kUnknown' indicates the Agent's version is not known. 'kNonUpgradableInvalidVersion' indicates the Agent's version is invalid. 'kNonUpgradableAgentIsNewer' indicates the Agent's version is newer than the agent software version the cluster. 'kNonUpgradableAgentIsOld' indicates the Agent's version is too old that does not support upgrades.

        :return: The upgradability of this AgentInformation.
        :rtype: str
        """
        return self._upgradability

    @upgradability.setter
    def upgradability(self, upgradability):
        """
        Sets the upgradability of this AgentInformation.
        Specifies the upgradability of the agent running on the physical server. Specifies the upgradability of the agent running on the physical server. 'kUpgradable' indicates the Agent can be upgraded to the agent software version on the cluster. 'kCurrent' indicates the Agent is running the latest version. 'kUnknown' indicates the Agent's version is not known. 'kNonUpgradableInvalidVersion' indicates the Agent's version is invalid. 'kNonUpgradableAgentIsNewer' indicates the Agent's version is newer than the agent software version the cluster. 'kNonUpgradableAgentIsOld' indicates the Agent's version is too old that does not support upgrades.

        :param upgradability: The upgradability of this AgentInformation.
        :type: str
        """
        allowed_values = ["kUpgradable", "kCurrent", "kUnknown", "kNonUpgradableInvalidVersion", "kNonUpgradableAgentIsNewer", "kNonUpgradableAgentIsOld"]
        if upgradability not in allowed_values:
            raise ValueError(
                "Invalid value for `upgradability` ({0}), must be one of {1}"
                .format(upgradability, allowed_values)
            )

        self._upgradability = upgradability

    @property
    def upgrade_status(self):
        """
        Gets the upgrade_status of this AgentInformation.
        Specifies the status of the upgrade of the agent on a physical server. Specifies the status of the upgrade of the agent on a physical server. 'kIdle' indicates there is no agent upgrade in progress. 'kAccepted' indicates the Agent upgrade is accepted. 'kStarted' indicates the Agent upgrade is in progress. 'kFinished' indicates the Agent upgrade is completed.

        :return: The upgrade_status of this AgentInformation.
        :rtype: str
        """
        return self._upgrade_status

    @upgrade_status.setter
    def upgrade_status(self, upgrade_status):
        """
        Sets the upgrade_status of this AgentInformation.
        Specifies the status of the upgrade of the agent on a physical server. Specifies the status of the upgrade of the agent on a physical server. 'kIdle' indicates there is no agent upgrade in progress. 'kAccepted' indicates the Agent upgrade is accepted. 'kStarted' indicates the Agent upgrade is in progress. 'kFinished' indicates the Agent upgrade is completed.

        :param upgrade_status: The upgrade_status of this AgentInformation.
        :type: str
        """
        allowed_values = ["kIdle", "kAccepted", "kStarted", "kFinished"]
        if upgrade_status not in allowed_values:
            raise ValueError(
                "Invalid value for `upgrade_status` ({0}), must be one of {1}"
                .format(upgrade_status, allowed_values)
            )

        self._upgrade_status = upgrade_status

    @property
    def upgrade_status_message(self):
        """
        Gets the upgrade_status_message of this AgentInformation.
        Specifies detailed message about the agent upgrade failure. This field is not set for successful upgrade.

        :return: The upgrade_status_message of this AgentInformation.
        :rtype: str
        """
        return self._upgrade_status_message

    @upgrade_status_message.setter
    def upgrade_status_message(self, upgrade_status_message):
        """
        Sets the upgrade_status_message of this AgentInformation.
        Specifies detailed message about the agent upgrade failure. This field is not set for successful upgrade.

        :param upgrade_status_message: The upgrade_status_message of this AgentInformation.
        :type: str
        """

        self._upgrade_status_message = upgrade_status_message

    @property
    def version(self):
        """
        Gets the version of this AgentInformation.
        Specifies the version of the Agent software.

        :return: The version of this AgentInformation.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this AgentInformation.
        Specifies the version of the Agent software.

        :param version: The version of this AgentInformation.
        :type: str
        """

        self._version = version

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