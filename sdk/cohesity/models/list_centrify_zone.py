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


class ListCentrifyZone(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, centrify_schema=None, description=None, distinguished_name=None, zone_name=None):
        """
        ListCentrifyZone - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'centrify_schema': 'str',
            'description': 'str',
            'distinguished_name': 'str',
            'zone_name': 'str'
        }

        self.attribute_map = {
            'centrify_schema': 'centrifySchema',
            'description': 'description',
            'distinguished_name': 'distinguishedName',
            'zone_name': 'zoneName'
        }

        self._centrify_schema = centrify_schema
        self._description = description
        self._distinguished_name = distinguished_name
        self._zone_name = zone_name

    @property
    def centrify_schema(self):
        """
        Gets the centrify_schema of this ListCentrifyZone.
        Specifies the schema of this Centrify zone. The below list of schemas and their values are taken from the document Centrify Server Suite 2016 Windows API Programmer's Guide https://docs.centrify.com/en/css/suite2016/centrify-win-progguide.pdf 'kCentrifyDynamicSchema_1_0' specifies dynamic schema, version 1.0. 'kCentrifyDynamicSchema_2_0' specifies dynamic schema, version 2.0. 'kCentrifyDynamicSchema_3_0' specifies dynamic schema, version 3.0. 'kCentrifyDynamicSchema_5_0' specifies dynamic schema, version 5.0. 'kCentrifySfu_3_0' specifies sfu schema, version 3.0. 'kCentrifySfu_3_0_V5' specifies sfu schema, 3.0.5. 'kCentrifySfu_4_0' specifies sfu schema, version 4.0. 'kCentrifyCdcRfc2307' specifies cdcrfc2307 schema. 'kCentrifyCdcRfc2307_2' specifies cdcrfc2307, version 2. 'kCentrifyCdcRfc2307_3' specifies cdcrfc2307, version 3.

        :return: The centrify_schema of this ListCentrifyZone.
        :rtype: str
        """
        return self._centrify_schema

    @centrify_schema.setter
    def centrify_schema(self, centrify_schema):
        """
        Sets the centrify_schema of this ListCentrifyZone.
        Specifies the schema of this Centrify zone. The below list of schemas and their values are taken from the document Centrify Server Suite 2016 Windows API Programmer's Guide https://docs.centrify.com/en/css/suite2016/centrify-win-progguide.pdf 'kCentrifyDynamicSchema_1_0' specifies dynamic schema, version 1.0. 'kCentrifyDynamicSchema_2_0' specifies dynamic schema, version 2.0. 'kCentrifyDynamicSchema_3_0' specifies dynamic schema, version 3.0. 'kCentrifyDynamicSchema_5_0' specifies dynamic schema, version 5.0. 'kCentrifySfu_3_0' specifies sfu schema, version 3.0. 'kCentrifySfu_3_0_V5' specifies sfu schema, 3.0.5. 'kCentrifySfu_4_0' specifies sfu schema, version 4.0. 'kCentrifyCdcRfc2307' specifies cdcrfc2307 schema. 'kCentrifyCdcRfc2307_2' specifies cdcrfc2307, version 2. 'kCentrifyCdcRfc2307_3' specifies cdcrfc2307, version 3.

        :param centrify_schema: The centrify_schema of this ListCentrifyZone.
        :type: str
        """
        allowed_values = ["kCentrifyDynamicSchema_1_0", "kCentrifyDynamicSchema_2_0", "kCentrifySfu_3_0", "kCentrifySfu_4_0", "kCentrifyCdcRfc2307", "kCentrifyDynamicSchema_3_0", "kCentrifyCdcRfc2307_2", "kCentrifyDynamicSchema_5_0", "kCentrifyCdcRfc2307_3", "kCentrifySfu_3_0_V5"]
        if centrify_schema not in allowed_values:
            raise ValueError(
                "Invalid value for `centrify_schema` ({0}), must be one of {1}"
                .format(centrify_schema, allowed_values)
            )

        self._centrify_schema = centrify_schema

    @property
    def description(self):
        """
        Gets the description of this ListCentrifyZone.
        Specifies a description of the Centrify zone.

        :return: The description of this ListCentrifyZone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ListCentrifyZone.
        Specifies a description of the Centrify zone.

        :param description: The description of this ListCentrifyZone.
        :type: str
        """

        self._description = description

    @property
    def distinguished_name(self):
        """
        Gets the distinguished_name of this ListCentrifyZone.
        Specifies the distinguished name of the Centrify zone.

        :return: The distinguished_name of this ListCentrifyZone.
        :rtype: str
        """
        return self._distinguished_name

    @distinguished_name.setter
    def distinguished_name(self, distinguished_name):
        """
        Sets the distinguished_name of this ListCentrifyZone.
        Specifies the distinguished name of the Centrify zone.

        :param distinguished_name: The distinguished_name of this ListCentrifyZone.
        :type: str
        """

        self._distinguished_name = distinguished_name

    @property
    def zone_name(self):
        """
        Gets the zone_name of this ListCentrifyZone.
        Specifies the zone name.

        :return: The zone_name of this ListCentrifyZone.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """
        Sets the zone_name of this ListCentrifyZone.
        Specifies the zone name.

        :param zone_name: The zone_name of this ListCentrifyZone.
        :type: str
        """

        self._zone_name = zone_name

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