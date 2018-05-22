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


class UserQuotaSummaryForUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, num_views_above_alert_threshold=None, num_views_above_hard_limit=None, total_num_views=None):
        """
        UserQuotaSummaryForUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'num_views_above_alert_threshold': 'int',
            'num_views_above_hard_limit': 'int',
            'total_num_views': 'int'
        }

        self.attribute_map = {
            'num_views_above_alert_threshold': 'numViewsAboveAlertThreshold',
            'num_views_above_hard_limit': 'numViewsAboveHardLimit',
            'total_num_views': 'totalNumViews'
        }

        self._num_views_above_alert_threshold = num_views_above_alert_threshold
        self._num_views_above_hard_limit = num_views_above_hard_limit
        self._total_num_views = total_num_views

    @property
    def num_views_above_alert_threshold(self):
        """
        Gets the num_views_above_alert_threshold of this UserQuotaSummaryForUser.
        Number of views in which user has exceeded alert threshold limit.

        :return: The num_views_above_alert_threshold of this UserQuotaSummaryForUser.
        :rtype: int
        """
        return self._num_views_above_alert_threshold

    @num_views_above_alert_threshold.setter
    def num_views_above_alert_threshold(self, num_views_above_alert_threshold):
        """
        Sets the num_views_above_alert_threshold of this UserQuotaSummaryForUser.
        Number of views in which user has exceeded alert threshold limit.

        :param num_views_above_alert_threshold: The num_views_above_alert_threshold of this UserQuotaSummaryForUser.
        :type: int
        """

        self._num_views_above_alert_threshold = num_views_above_alert_threshold

    @property
    def num_views_above_hard_limit(self):
        """
        Gets the num_views_above_hard_limit of this UserQuotaSummaryForUser.
        Number of views in which the user has exceeded hard limit.

        :return: The num_views_above_hard_limit of this UserQuotaSummaryForUser.
        :rtype: int
        """
        return self._num_views_above_hard_limit

    @num_views_above_hard_limit.setter
    def num_views_above_hard_limit(self, num_views_above_hard_limit):
        """
        Sets the num_views_above_hard_limit of this UserQuotaSummaryForUser.
        Number of views in which the user has exceeded hard limit.

        :param num_views_above_hard_limit: The num_views_above_hard_limit of this UserQuotaSummaryForUser.
        :type: int
        """

        self._num_views_above_hard_limit = num_views_above_hard_limit

    @property
    def total_num_views(self):
        """
        Gets the total_num_views of this UserQuotaSummaryForUser.
        Total number of views in which the user has a quota policy specified or has non-zero usage.

        :return: The total_num_views of this UserQuotaSummaryForUser.
        :rtype: int
        """
        return self._total_num_views

    @total_num_views.setter
    def total_num_views(self, total_num_views):
        """
        Sets the total_num_views of this UserQuotaSummaryForUser.
        Total number of views in which the user has a quota policy specified or has non-zero usage.

        :param total_num_views: The total_num_views of this UserQuotaSummaryForUser.
        :type: int
        """

        self._total_num_views = total_num_views

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