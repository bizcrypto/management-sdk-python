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


class ProtectionPolicyFullSchedulingPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, continuous_schedule=None, daily_schedule=None, monthly_schedule=None, periodicity=None):
        """
        ProtectionPolicyFullSchedulingPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'continuous_schedule': 'ProtectionPolicyFullSchedulingPolicyContinuousSchedule',
            'daily_schedule': 'ProtectionPolicyFullSchedulingPolicyDailySchedule',
            'monthly_schedule': 'ProtectionPolicyFullSchedulingPolicyMonthlySchedule',
            'periodicity': 'str'
        }

        self.attribute_map = {
            'continuous_schedule': 'continuousSchedule',
            'daily_schedule': 'dailySchedule',
            'monthly_schedule': 'monthlySchedule',
            'periodicity': 'periodicity'
        }

        self._continuous_schedule = continuous_schedule
        self._daily_schedule = daily_schedule
        self._monthly_schedule = monthly_schedule
        self._periodicity = periodicity

    @property
    def continuous_schedule(self):
        """
        Gets the continuous_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :return: The continuous_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :rtype: ProtectionPolicyFullSchedulingPolicyContinuousSchedule
        """
        return self._continuous_schedule

    @continuous_schedule.setter
    def continuous_schedule(self, continuous_schedule):
        """
        Sets the continuous_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :param continuous_schedule: The continuous_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :type: ProtectionPolicyFullSchedulingPolicyContinuousSchedule
        """

        self._continuous_schedule = continuous_schedule

    @property
    def daily_schedule(self):
        """
        Gets the daily_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :return: The daily_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :rtype: ProtectionPolicyFullSchedulingPolicyDailySchedule
        """
        return self._daily_schedule

    @daily_schedule.setter
    def daily_schedule(self, daily_schedule):
        """
        Sets the daily_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :param daily_schedule: The daily_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :type: ProtectionPolicyFullSchedulingPolicyDailySchedule
        """

        self._daily_schedule = daily_schedule

    @property
    def monthly_schedule(self):
        """
        Gets the monthly_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :return: The monthly_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :rtype: ProtectionPolicyFullSchedulingPolicyMonthlySchedule
        """
        return self._monthly_schedule

    @monthly_schedule.setter
    def monthly_schedule(self, monthly_schedule):
        """
        Sets the monthly_schedule of this ProtectionPolicyFullSchedulingPolicy.


        :param monthly_schedule: The monthly_schedule of this ProtectionPolicyFullSchedulingPolicy.
        :type: ProtectionPolicyFullSchedulingPolicyMonthlySchedule
        """

        self._monthly_schedule = monthly_schedule

    @property
    def periodicity(self):
        """
        Gets the periodicity of this ProtectionPolicyFullSchedulingPolicy.
        Specifies how often to start new Job Runs of a Protection Job. 'kDaily' means new Job Runs start daily. 'kMonthly' means new Job Runs start monthly. 'kContinuous' means new Job Runs repetitively start at the beginning of the specified time interval (in hours or minutes). 'kOneOff' means this is an additional schedule.

        :return: The periodicity of this ProtectionPolicyFullSchedulingPolicy.
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity):
        """
        Sets the periodicity of this ProtectionPolicyFullSchedulingPolicy.
        Specifies how often to start new Job Runs of a Protection Job. 'kDaily' means new Job Runs start daily. 'kMonthly' means new Job Runs start monthly. 'kContinuous' means new Job Runs repetitively start at the beginning of the specified time interval (in hours or minutes). 'kOneOff' means this is an additional schedule.

        :param periodicity: The periodicity of this ProtectionPolicyFullSchedulingPolicy.
        :type: str
        """
        allowed_values = ["kContinuous", "kDaily", "kMonthly", "kOneOff"]
        if periodicity not in allowed_values:
            raise ValueError(
                "Invalid value for `periodicity` ({0}), must be one of {1}"
                .format(periodicity, allowed_values)
            )

        self._periodicity = periodicity

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