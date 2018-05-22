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


class MapReduceInstance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, input_params=None, input_spec=None, map_reduce_info_id=None, output_spec=None, run_info=None):
        """
        MapReduceInstance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'input_params': 'list[MapReduceInstanceInputParam]',
            'input_spec': 'InputSpec',
            'map_reduce_info_id': 'int',
            'output_spec': 'OutputSpec',
            'run_info': 'MapReduceInstanceRunInfo'
        }

        self.attribute_map = {
            'id': 'id',
            'input_params': 'inputParams',
            'input_spec': 'inputSpec',
            'map_reduce_info_id': 'mapReduceInfoId',
            'output_spec': 'outputSpec',
            'run_info': 'runInfo'
        }

        self._id = id
        self._input_params = input_params
        self._input_spec = input_spec
        self._map_reduce_info_id = map_reduce_info_id
        self._output_spec = output_spec
        self._run_info = run_info

    @property
    def id(self):
        """
        Gets the id of this MapReduceInstance.
        System generated ID of map reduce instance.

        :return: The id of this MapReduceInstance.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MapReduceInstance.
        System generated ID of map reduce instance.

        :param id: The id of this MapReduceInstance.
        :type: int
        """

        self._id = id

    @property
    def input_params(self):
        """
        Gets the input_params of this MapReduceInstance.


        :return: The input_params of this MapReduceInstance.
        :rtype: list[MapReduceInstanceInputParam]
        """
        return self._input_params

    @input_params.setter
    def input_params(self, input_params):
        """
        Sets the input_params of this MapReduceInstance.


        :param input_params: The input_params of this MapReduceInstance.
        :type: list[MapReduceInstanceInputParam]
        """

        self._input_params = input_params

    @property
    def input_spec(self):
        """
        Gets the input_spec of this MapReduceInstance.
        Input spec for the MR.

        :return: The input_spec of this MapReduceInstance.
        :rtype: InputSpec
        """
        return self._input_spec

    @input_spec.setter
    def input_spec(self, input_spec):
        """
        Sets the input_spec of this MapReduceInstance.
        Input spec for the MR.

        :param input_spec: The input_spec of this MapReduceInstance.
        :type: InputSpec
        """

        self._input_spec = input_spec

    @property
    def map_reduce_info_id(self):
        """
        Gets the map_reduce_info_id of this MapReduceInstance.
        ID of Map reduce info.

        :return: The map_reduce_info_id of this MapReduceInstance.
        :rtype: int
        """
        return self._map_reduce_info_id

    @map_reduce_info_id.setter
    def map_reduce_info_id(self, map_reduce_info_id):
        """
        Sets the map_reduce_info_id of this MapReduceInstance.
        ID of Map reduce info.

        :param map_reduce_info_id: The map_reduce_info_id of this MapReduceInstance.
        :type: int
        """

        self._map_reduce_info_id = map_reduce_info_id

    @property
    def output_spec(self):
        """
        Gets the output_spec of this MapReduceInstance.
        Output spec for the MR.

        :return: The output_spec of this MapReduceInstance.
        :rtype: OutputSpec
        """
        return self._output_spec

    @output_spec.setter
    def output_spec(self, output_spec):
        """
        Sets the output_spec of this MapReduceInstance.
        Output spec for the MR.

        :param output_spec: The output_spec of this MapReduceInstance.
        :type: OutputSpec
        """

        self._output_spec = output_spec

    @property
    def run_info(self):
        """
        Gets the run_info of this MapReduceInstance.
        Information about run of this instance. All fields of RunInfo will be populated by yoda/analytics components.

        :return: The run_info of this MapReduceInstance.
        :rtype: MapReduceInstanceRunInfo
        """
        return self._run_info

    @run_info.setter
    def run_info(self, run_info):
        """
        Sets the run_info of this MapReduceInstance.
        Information about run of this instance. All fields of RunInfo will be populated by yoda/analytics components.

        :param run_info: The run_info of this MapReduceInstance.
        :type: MapReduceInstanceRunInfo
        """

        self._run_info = run_info

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