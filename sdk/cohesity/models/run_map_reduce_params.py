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


class RunMapReduceParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, app_id=None, input_params=None, mr_input=None, mr_output=None):
        """
        RunMapReduceParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'app_id': 'int',
            'input_params': 'list[MapReduceInstanceInputParam]',
            'mr_input': 'InputSpec',
            'mr_output': 'OutputSpec'
        }

        self.attribute_map = {
            'app_id': 'appId',
            'input_params': 'inputParams',
            'mr_input': 'mrInput',
            'mr_output': 'mrOutput'
        }

        self._app_id = app_id
        self._input_params = input_params
        self._mr_input = mr_input
        self._mr_output = mr_output

    @property
    def app_id(self):
        """
        Gets the app_id of this RunMapReduceParams.
        ApplicationId is the Id of the map reduce application to run.

        :return: The app_id of this RunMapReduceParams.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this RunMapReduceParams.
        ApplicationId is the Id of the map reduce application to run.

        :param app_id: The app_id of this RunMapReduceParams.
        :type: int
        """

        self._app_id = app_id

    @property
    def input_params(self):
        """
        Gets the input_params of this RunMapReduceParams.
        InputParams specifies optional list of key=value input params specified for running the map reduce instance.

        :return: The input_params of this RunMapReduceParams.
        :rtype: list[MapReduceInstanceInputParam]
        """
        return self._input_params

    @input_params.setter
    def input_params(self, input_params):
        """
        Sets the input_params of this RunMapReduceParams.
        InputParams specifies optional list of key=value input params specified for running the map reduce instance.

        :param input_params: The input_params of this RunMapReduceParams.
        :type: list[MapReduceInstanceInputParam]
        """

        self._input_params = input_params

    @property
    def mr_input(self):
        """
        Gets the mr_input of this RunMapReduceParams.
        InputSpecification specifies the input information to run the specific map reduce instance.

        :return: The mr_input of this RunMapReduceParams.
        :rtype: InputSpec
        """
        return self._mr_input

    @mr_input.setter
    def mr_input(self, mr_input):
        """
        Sets the mr_input of this RunMapReduceParams.
        InputSpecification specifies the input information to run the specific map reduce instance.

        :param mr_input: The mr_input of this RunMapReduceParams.
        :type: InputSpec
        """

        self._mr_input = mr_input

    @property
    def mr_output(self):
        """
        Gets the mr_output of this RunMapReduceParams.
        OutputSpecification specifies the output information to run the specific map reduce instance.

        :return: The mr_output of this RunMapReduceParams.
        :rtype: OutputSpec
        """
        return self._mr_output

    @mr_output.setter
    def mr_output(self, mr_output):
        """
        Sets the mr_output of this RunMapReduceParams.
        OutputSpecification specifies the output information to run the specific map reduce instance.

        :param mr_output: The mr_output of this RunMapReduceParams.
        :type: OutputSpec
        """

        self._mr_output = mr_output

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