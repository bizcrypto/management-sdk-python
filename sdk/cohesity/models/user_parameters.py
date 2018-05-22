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


class UserParameters(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, domain=None, effective_time_msecs=None, email_address=None, password=None, restricted=None, roles=None, username=None):
        """
        UserParameters - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'domain': 'str',
            'effective_time_msecs': 'int',
            'email_address': 'str',
            'password': 'str',
            'restricted': 'bool',
            'roles': 'list[str]',
            'username': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'domain': 'domain',
            'effective_time_msecs': 'effectiveTimeMsecs',
            'email_address': 'emailAddress',
            'password': 'password',
            'restricted': 'restricted',
            'roles': 'roles',
            'username': 'username'
        }

        self._description = description
        self._domain = domain
        self._effective_time_msecs = effective_time_msecs
        self._email_address = email_address
        self._password = password
        self._restricted = restricted
        self._roles = roles
        self._username = username

    @property
    def description(self):
        """
        Gets the description of this UserParameters.
        Specifies a description about the user.

        :return: The description of this UserParameters.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserParameters.
        Specifies a description about the user.

        :param description: The description of this UserParameters.
        :type: str
        """

        self._description = description

    @property
    def domain(self):
        """
        Gets the domain of this UserParameters.
        Specifies the fully qualified domain name (FQDN) of an Active Directory or LOCAL for the default LOCAL domain on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain.

        :return: The domain of this UserParameters.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this UserParameters.
        Specifies the fully qualified domain name (FQDN) of an Active Directory or LOCAL for the default LOCAL domain on the Cohesity Cluster. A user is uniquely identified by combination of the username and the domain.

        :param domain: The domain of this UserParameters.
        :type: str
        """

        self._domain = domain

    @property
    def effective_time_msecs(self):
        """
        Gets the effective_time_msecs of this UserParameters.
        Specifies the epoch time in milliseconds when the user becomes effective. Until that time, the user cannot log in.

        :return: The effective_time_msecs of this UserParameters.
        :rtype: int
        """
        return self._effective_time_msecs

    @effective_time_msecs.setter
    def effective_time_msecs(self, effective_time_msecs):
        """
        Sets the effective_time_msecs of this UserParameters.
        Specifies the epoch time in milliseconds when the user becomes effective. Until that time, the user cannot log in.

        :param effective_time_msecs: The effective_time_msecs of this UserParameters.
        :type: int
        """

        self._effective_time_msecs = effective_time_msecs

    @property
    def email_address(self):
        """
        Gets the email_address of this UserParameters.
        Specifies the email address of the user.

        :return: The email_address of this UserParameters.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """
        Sets the email_address of this UserParameters.
        Specifies the email address of the user.

        :param email_address: The email_address of this UserParameters.
        :type: str
        """

        self._email_address = email_address

    @property
    def password(self):
        """
        Gets the password of this UserParameters.
        Specifies the password of this user.

        :return: The password of this UserParameters.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UserParameters.
        Specifies the password of this user.

        :param password: The password of this UserParameters.
        :type: str
        """

        self._password = password

    @property
    def restricted(self):
        """
        Gets the restricted of this UserParameters.
        Whether the user is a restricted user. A restricted user can only view the objects he has permissions to.

        :return: The restricted of this UserParameters.
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this UserParameters.
        Whether the user is a restricted user. A restricted user can only view the objects he has permissions to.

        :param restricted: The restricted of this UserParameters.
        :type: bool
        """

        self._restricted = restricted

    @property
    def roles(self):
        """
        Gets the roles of this UserParameters.
        Specifies the Cohesity roles to associate with the user such as such as 'Admin', 'Ops' or 'View'. The Cohesity roles determine privileges on the Cohesity Cluster for this user.

        :return: The roles of this UserParameters.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this UserParameters.
        Specifies the Cohesity roles to associate with the user such as such as 'Admin', 'Ops' or 'View'. The Cohesity roles determine privileges on the Cohesity Cluster for this user.

        :param roles: The roles of this UserParameters.
        :type: list[str]
        """

        self._roles = roles

    @property
    def username(self):
        """
        Gets the username of this UserParameters.
        Specifies the login name of the user.

        :return: The username of this UserParameters.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this UserParameters.
        Specifies the login name of the user.

        :param username: The username of this UserParameters.
        :type: str
        """

        self._username = username

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