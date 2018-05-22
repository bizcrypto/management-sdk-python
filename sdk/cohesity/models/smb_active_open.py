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


class SmbActiveOpen(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, access_info_list=None, open_id=None, others_can_delete=None, others_can_read=None, others_can_write=None):
        """
        SmbActiveOpen - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access_info_list': 'list[str]',
            'open_id': 'int',
            'others_can_delete': 'bool',
            'others_can_read': 'bool',
            'others_can_write': 'bool'
        }

        self.attribute_map = {
            'access_info_list': 'accessInfoList',
            'open_id': 'openId',
            'others_can_delete': 'othersCanDelete',
            'others_can_read': 'othersCanRead',
            'others_can_write': 'othersCanWrite'
        }

        self._access_info_list = access_info_list
        self._open_id = open_id
        self._others_can_delete = others_can_delete
        self._others_can_read = others_can_read
        self._others_can_write = others_can_write

    @property
    def access_info_list(self):
        """
        Gets the access_info_list of this SmbActiveOpen.
        'kFileReadData' indicates the right to read data from the file or named pipe. 'kFileWriteData' indicates the right to write data into the file or named pipe beyond the end of the file. 'kFileAppendData' indicates the right to append data into the file or named pipe. 'kFileReadEa' indicates the right to read the extended attributes of the file or named pipe. 'kFileWriteEa' indicates the right to write or change the extended attributes to the file or named pipe. 'kFileExecute' indicates the right to delete entries within a directory. 'kFileDeleteChild' indicates the right to execute the file. 'kFileReadAttributes' indicates the right to read the attributes of the file. 'kFileWriteAttributes' indicates the right to change the attributes of the file. 'kDelete' indicates the right to delete the file. 'kReadControl' indicates the right to read the security descriptor for the file or named pipe. 'kWriteDac' indicates the right to change the discretionary access control list (DACL) in the security descriptor for the file or named pipe. For the DACL data structure, see ACL in [MS-DTYP]. 'kWriteOwner' indicates the right to change the owner in the security descriptor for the file or named pipe. 'kSynchronize' is used only by SMB2 clients. 'kAccessSystemSecurity' indicates the right to read or change the system access control list (SACL) in the security descriptor for the file or named pipe. For the SACL data structure, see ACL in [MS-DTYP].<42> 'kMaximumAllowed' indicates that the client is requesting an open to the file with the highest level of access the client has on this file. If no access is granted for the client on this file, the server MUST fail the open with STATUS_ACCESS_DENIED. 'kGenericAll' indicates a request for all the access flags that are previously listed except kMaximumAllowed and kAccessSystemSecurity. 'kGenericExecute' indicates a request for the following combination of access flags listed above: kFileReadAttributes| kFileExecute| kSynchronize| kReadControl. 'kGenericWrite' indicates a request for the following combination of access flags listed above: kFileWriteData| kFileAppendData| kFileWriteAttributes| kFileWriteEa| kSynchronize| kReadControl. 'kGenericRead' indicates a request for the following combination of access flags listed above: kFileReadData| kFileReadAttributes| kFileReadEa| kSynchronize| kReadControl.

        :return: The access_info_list of this SmbActiveOpen.
        :rtype: list[str]
        """
        return self._access_info_list

    @access_info_list.setter
    def access_info_list(self, access_info_list):
        """
        Sets the access_info_list of this SmbActiveOpen.
        'kFileReadData' indicates the right to read data from the file or named pipe. 'kFileWriteData' indicates the right to write data into the file or named pipe beyond the end of the file. 'kFileAppendData' indicates the right to append data into the file or named pipe. 'kFileReadEa' indicates the right to read the extended attributes of the file or named pipe. 'kFileWriteEa' indicates the right to write or change the extended attributes to the file or named pipe. 'kFileExecute' indicates the right to delete entries within a directory. 'kFileDeleteChild' indicates the right to execute the file. 'kFileReadAttributes' indicates the right to read the attributes of the file. 'kFileWriteAttributes' indicates the right to change the attributes of the file. 'kDelete' indicates the right to delete the file. 'kReadControl' indicates the right to read the security descriptor for the file or named pipe. 'kWriteDac' indicates the right to change the discretionary access control list (DACL) in the security descriptor for the file or named pipe. For the DACL data structure, see ACL in [MS-DTYP]. 'kWriteOwner' indicates the right to change the owner in the security descriptor for the file or named pipe. 'kSynchronize' is used only by SMB2 clients. 'kAccessSystemSecurity' indicates the right to read or change the system access control list (SACL) in the security descriptor for the file or named pipe. For the SACL data structure, see ACL in [MS-DTYP].<42> 'kMaximumAllowed' indicates that the client is requesting an open to the file with the highest level of access the client has on this file. If no access is granted for the client on this file, the server MUST fail the open with STATUS_ACCESS_DENIED. 'kGenericAll' indicates a request for all the access flags that are previously listed except kMaximumAllowed and kAccessSystemSecurity. 'kGenericExecute' indicates a request for the following combination of access flags listed above: kFileReadAttributes| kFileExecute| kSynchronize| kReadControl. 'kGenericWrite' indicates a request for the following combination of access flags listed above: kFileWriteData| kFileAppendData| kFileWriteAttributes| kFileWriteEa| kSynchronize| kReadControl. 'kGenericRead' indicates a request for the following combination of access flags listed above: kFileReadData| kFileReadAttributes| kFileReadEa| kSynchronize| kReadControl.

        :param access_info_list: The access_info_list of this SmbActiveOpen.
        :type: list[str]
        """
        allowed_values = ["kFileReadData", "kFileWriteData", "kFileAppendData", "kFileReadEa", "kFileWriteEa", "kFileExecute", "kFileDeleteChild", "kFileReadAttributes", "kFileWriteAttributes", "kDelete", "kReadControl", "kWriteDac", "kWriteOwner", "kSynchronize", "kAccessSystemSecurity", "kMaximumAllowed", "kGenericAll", "kGenericExecute", "kGenericWrite", "kGenericRead"]
        if access_info_list not in allowed_values:
            raise ValueError(
                "Invalid value for `access_info_list` ({0}), must be one of {1}"
                .format(access_info_list, allowed_values)
            )

        self._access_info_list = access_info_list

    @property
    def open_id(self):
        """
        Gets the open_id of this SmbActiveOpen.
        Specifies the id of the active open.

        :return: The open_id of this SmbActiveOpen.
        :rtype: int
        """
        return self._open_id

    @open_id.setter
    def open_id(self, open_id):
        """
        Sets the open_id of this SmbActiveOpen.
        Specifies the id of the active open.

        :param open_id: The open_id of this SmbActiveOpen.
        :type: int
        """

        self._open_id = open_id

    @property
    def others_can_delete(self):
        """
        Gets the others_can_delete of this SmbActiveOpen.
        Specifies whether others are allowed to delete.

        :return: The others_can_delete of this SmbActiveOpen.
        :rtype: bool
        """
        return self._others_can_delete

    @others_can_delete.setter
    def others_can_delete(self, others_can_delete):
        """
        Sets the others_can_delete of this SmbActiveOpen.
        Specifies whether others are allowed to delete.

        :param others_can_delete: The others_can_delete of this SmbActiveOpen.
        :type: bool
        """

        self._others_can_delete = others_can_delete

    @property
    def others_can_read(self):
        """
        Gets the others_can_read of this SmbActiveOpen.
        Specifies whether others are allowed to read.

        :return: The others_can_read of this SmbActiveOpen.
        :rtype: bool
        """
        return self._others_can_read

    @others_can_read.setter
    def others_can_read(self, others_can_read):
        """
        Sets the others_can_read of this SmbActiveOpen.
        Specifies whether others are allowed to read.

        :param others_can_read: The others_can_read of this SmbActiveOpen.
        :type: bool
        """

        self._others_can_read = others_can_read

    @property
    def others_can_write(self):
        """
        Gets the others_can_write of this SmbActiveOpen.
        Specifies whether others are allowed to write.

        :return: The others_can_write of this SmbActiveOpen.
        :rtype: bool
        """
        return self._others_can_write

    @others_can_write.setter
    def others_can_write(self, others_can_write):
        """
        Sets the others_can_write of this SmbActiveOpen.
        Specifies whether others are allowed to write.

        :param others_can_write: The others_can_write of this SmbActiveOpen.
        :type: bool
        """

        self._others_can_write = others_can_write

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