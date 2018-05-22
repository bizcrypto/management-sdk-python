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


class ChassisInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, chassis_id=None, chassis_name=None, location=None, rack_id=None):
        """
        ChassisInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'chassis_id': 'int',
            'chassis_name': 'str',
            'location': 'str',
            'rack_id': 'int'
        }

        self.attribute_map = {
            'chassis_id': 'chassisId',
            'chassis_name': 'chassisName',
            'location': 'location',
            'rack_id': 'rackId'
        }

        self._chassis_id = chassis_id
        self._chassis_name = chassis_name
        self._location = location
        self._rack_id = rack_id

    @property
    def chassis_id(self):
        """
        Gets the chassis_id of this ChassisInfo.
        ChassisId is a unique id assigned to the chassis.

        :return: The chassis_id of this ChassisInfo.
        :rtype: int
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """
        Sets the chassis_id of this ChassisInfo.
        ChassisId is a unique id assigned to the chassis.

        :param chassis_id: The chassis_id of this ChassisInfo.
        :type: int
        """

        self._chassis_id = chassis_id

    @property
    def chassis_name(self):
        """
        Gets the chassis_name of this ChassisInfo.
        ChassisName is the name of the chassis. This could be the chassis serial number.

        :return: The chassis_name of this ChassisInfo.
        :rtype: str
        """
        return self._chassis_name

    @chassis_name.setter
    def chassis_name(self, chassis_name):
        """
        Sets the chassis_name of this ChassisInfo.
        ChassisName is the name of the chassis. This could be the chassis serial number.

        :param chassis_name: The chassis_name of this ChassisInfo.
        :type: str
        """

        self._chassis_name = chassis_name

    @property
    def location(self):
        """
        Gets the location of this ChassisInfo.
        Location is the location of the chassis within the rack.

        :return: The location of this ChassisInfo.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this ChassisInfo.
        Location is the location of the chassis within the rack.

        :param location: The location of this ChassisInfo.
        :type: str
        """

        self._location = location

    @property
    def rack_id(self):
        """
        Gets the rack_id of this ChassisInfo.
        Rack is the rack within which this chassis lives.

        :return: The rack_id of this ChassisInfo.
        :rtype: int
        """
        return self._rack_id

    @rack_id.setter
    def rack_id(self, rack_id):
        """
        Sets the rack_id of this ChassisInfo.
        Rack is the rack within which this chassis lives.

        :param rack_id: The rack_id of this ChassisInfo.
        :type: int
        """

        self._rack_id = rack_id

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