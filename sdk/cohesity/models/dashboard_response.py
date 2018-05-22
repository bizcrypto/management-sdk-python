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


class DashboardResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, dashboard=None, dashboards=None):
        """
        DashboardResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'dashboard': 'Dashboard',
            'dashboards': 'list[Dashboard]'
        }

        self.attribute_map = {
            'dashboard': 'dashboard',
            'dashboards': 'dashboards'
        }

        self._dashboard = dashboard
        self._dashboards = dashboards

    @property
    def dashboard(self):
        """
        Gets the dashboard of this DashboardResponse.
        Specifies the dashboard of the local cluster or a remote cluster whose id is set in clusterId query parameter when the query parameter allClusters is not given or set to false. Otherwise this field is populated with aggregated dashboard values for all the dashboards in the dashboards field.

        :return: The dashboard of this DashboardResponse.
        :rtype: Dashboard
        """
        return self._dashboard

    @dashboard.setter
    def dashboard(self, dashboard):
        """
        Sets the dashboard of this DashboardResponse.
        Specifies the dashboard of the local cluster or a remote cluster whose id is set in clusterId query parameter when the query parameter allClusters is not given or set to false. Otherwise this field is populated with aggregated dashboard values for all the dashboards in the dashboards field.

        :param dashboard: The dashboard of this DashboardResponse.
        :type: Dashboard
        """

        self._dashboard = dashboard

    @property
    def dashboards(self):
        """
        Gets the dashboards of this DashboardResponse.
        Specifies a list of dashboards of all the clusters in the SPOG setup if the query parameter allClusters is set to true. Otherwise this field is not populated. When populated the dashboard field is also populated with aggregated dashboard values.

        :return: The dashboards of this DashboardResponse.
        :rtype: list[Dashboard]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """
        Sets the dashboards of this DashboardResponse.
        Specifies a list of dashboards of all the clusters in the SPOG setup if the query parameter allClusters is set to true. Otherwise this field is not populated. When populated the dashboard field is also populated with aggregated dashboard values.

        :param dashboards: The dashboards of this DashboardResponse.
        :type: list[Dashboard]
        """

        self._dashboards = dashboards

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