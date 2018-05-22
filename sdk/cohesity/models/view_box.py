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


class ViewBox(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ad_domain_name=None, cluster_partition_id=None, default_user_quota_policy=None, default_view_quota_policy=None, id=None, name=None, physical_quota=None, removal_state=None, s3_buckets_allowed=None, stats=None, storage_policy=None, treat_file_sync_as_data_sync=None):
        """
        ViewBox - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ad_domain_name': 'str',
            'cluster_partition_id': 'int',
            'cluster_partition_name': 'str',
            'default_user_quota_policy': 'CreateViewBoxParamsDefaultUserQuotaPolicy',
            'default_view_quota_policy': 'CreateViewBoxParamsDefaultViewQuotaPolicy',
            'id': 'int',
            'name': 'str',
            'physical_quota': 'CreateViewBoxParamsPhysicalQuota',
            'removal_state': 'str',
            's3_buckets_allowed': 'bool',
            'stats': 'ViewBoxStats',
            'storage_policy': 'StoragePolicy',
            'treat_file_sync_as_data_sync': 'bool'
        }

        self.attribute_map = {
            'ad_domain_name': 'adDomainName',
            'cluster_partition_id': 'clusterPartitionId',
            'cluster_partition_name': 'clusterPartitionName',
            'default_user_quota_policy': 'defaultUserQuotaPolicy',
            'default_view_quota_policy': 'defaultViewQuotaPolicy',
            'id': 'id',
            'name': 'name',
            'physical_quota': 'physicalQuota',
            'removal_state': 'removalState',
            's3_buckets_allowed': 's3BucketsAllowed',
            'stats': 'stats',
            'storage_policy': 'storagePolicy',
            'treat_file_sync_as_data_sync': 'treatFileSyncAsDataSync'
        }

        self._cluster_partition_name = None
        self._ad_domain_name = ad_domain_name
        self._cluster_partition_id = cluster_partition_id
        self._default_user_quota_policy = default_user_quota_policy
        self._default_view_quota_policy = default_view_quota_policy
        self._id = id
        self._name = name
        self._physical_quota = physical_quota
        self._removal_state = removal_state
        self._s3_buckets_allowed = s3_buckets_allowed
        self._stats = stats
        self._storage_policy = storage_policy
        self._treat_file_sync_as_data_sync = treat_file_sync_as_data_sync

    @property
    def ad_domain_name(self):
        """
        Gets the ad_domain_name of this ViewBox.
        Specifies an active directory domain that this view box is mapped to.

        :return: The ad_domain_name of this ViewBox.
        :rtype: str
        """
        return self._ad_domain_name

    @ad_domain_name.setter
    def ad_domain_name(self, ad_domain_name):
        """
        Sets the ad_domain_name of this ViewBox.
        Specifies an active directory domain that this view box is mapped to.

        :param ad_domain_name: The ad_domain_name of this ViewBox.
        :type: str
        """

        self._ad_domain_name = ad_domain_name

    @property
    def cluster_partition_id(self):
        """
        Gets the cluster_partition_id of this ViewBox.
        Specifies the Cluster Partition id where the Storage Domain (View Box) is located.

        :return: The cluster_partition_id of this ViewBox.
        :rtype: int
        """
        return self._cluster_partition_id

    @cluster_partition_id.setter
    def cluster_partition_id(self, cluster_partition_id):
        """
        Sets the cluster_partition_id of this ViewBox.
        Specifies the Cluster Partition id where the Storage Domain (View Box) is located.

        :param cluster_partition_id: The cluster_partition_id of this ViewBox.
        :type: int
        """

        self._cluster_partition_id = cluster_partition_id

    @property
    def cluster_partition_name(self):
        """
        Gets the cluster_partition_name of this ViewBox.
        Specifies the Cohesity Cluster name where the Storage Domain (View Box) is located.

        :return: The cluster_partition_name of this ViewBox.
        :rtype: str
        """
        return self._cluster_partition_name

    @property
    def default_user_quota_policy(self):
        """
        Gets the default_user_quota_policy of this ViewBox.


        :return: The default_user_quota_policy of this ViewBox.
        :rtype: CreateViewBoxParamsDefaultUserQuotaPolicy
        """
        return self._default_user_quota_policy

    @default_user_quota_policy.setter
    def default_user_quota_policy(self, default_user_quota_policy):
        """
        Sets the default_user_quota_policy of this ViewBox.


        :param default_user_quota_policy: The default_user_quota_policy of this ViewBox.
        :type: CreateViewBoxParamsDefaultUserQuotaPolicy
        """

        self._default_user_quota_policy = default_user_quota_policy

    @property
    def default_view_quota_policy(self):
        """
        Gets the default_view_quota_policy of this ViewBox.


        :return: The default_view_quota_policy of this ViewBox.
        :rtype: CreateViewBoxParamsDefaultViewQuotaPolicy
        """
        return self._default_view_quota_policy

    @default_view_quota_policy.setter
    def default_view_quota_policy(self, default_view_quota_policy):
        """
        Sets the default_view_quota_policy of this ViewBox.


        :param default_view_quota_policy: The default_view_quota_policy of this ViewBox.
        :type: CreateViewBoxParamsDefaultViewQuotaPolicy
        """

        self._default_view_quota_policy = default_view_quota_policy

    @property
    def id(self):
        """
        Gets the id of this ViewBox.
        Specifies the Id of the Storage Domain (View Box).

        :return: The id of this ViewBox.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ViewBox.
        Specifies the Id of the Storage Domain (View Box).

        :param id: The id of this ViewBox.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ViewBox.
        Specifies the name of the Storage Domain (View Box).

        :return: The name of this ViewBox.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ViewBox.
        Specifies the name of the Storage Domain (View Box).

        :param name: The name of this ViewBox.
        :type: str
        """

        self._name = name

    @property
    def physical_quota(self):
        """
        Gets the physical_quota of this ViewBox.


        :return: The physical_quota of this ViewBox.
        :rtype: CreateViewBoxParamsPhysicalQuota
        """
        return self._physical_quota

    @physical_quota.setter
    def physical_quota(self, physical_quota):
        """
        Sets the physical_quota of this ViewBox.


        :param physical_quota: The physical_quota of this ViewBox.
        :type: CreateViewBoxParamsPhysicalQuota
        """

        self._physical_quota = physical_quota

    @property
    def removal_state(self):
        """
        Gets the removal_state of this ViewBox.
        Specifies the current removal state of the Storage Domain (View Box). 'kDontRemove' means the state of object is functional and it is not being removed. 'kMarkedForRemoval' means the object is being removed. 'kOkToRemove' means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster.

        :return: The removal_state of this ViewBox.
        :rtype: str
        """
        return self._removal_state

    @removal_state.setter
    def removal_state(self, removal_state):
        """
        Sets the removal_state of this ViewBox.
        Specifies the current removal state of the Storage Domain (View Box). 'kDontRemove' means the state of object is functional and it is not being removed. 'kMarkedForRemoval' means the object is being removed. 'kOkToRemove' means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster.

        :param removal_state: The removal_state of this ViewBox.
        :type: str
        """
        allowed_values = ["kDontRemove", "kMarkedForRemoval", "kOkToRemove"]
        if removal_state not in allowed_values:
            raise ValueError(
                "Invalid value for `removal_state` ({0}), must be one of {1}"
                .format(removal_state, allowed_values)
            )

        self._removal_state = removal_state

    @property
    def s3_buckets_allowed(self):
        """
        Gets the s3_buckets_allowed of this ViewBox.
        Specifies whether creation of a S3 bucket is allowed in this Storage Domain (View Box). When a new S3 bucket creation request arrives, we'll look at all the View Boxes and the first Storage Domain (View Box) that allows creating S3 buckets in it will be the one where the bucket will be placed.

        :return: The s3_buckets_allowed of this ViewBox.
        :rtype: bool
        """
        return self._s3_buckets_allowed

    @s3_buckets_allowed.setter
    def s3_buckets_allowed(self, s3_buckets_allowed):
        """
        Sets the s3_buckets_allowed of this ViewBox.
        Specifies whether creation of a S3 bucket is allowed in this Storage Domain (View Box). When a new S3 bucket creation request arrives, we'll look at all the View Boxes and the first Storage Domain (View Box) that allows creating S3 buckets in it will be the one where the bucket will be placed.

        :param s3_buckets_allowed: The s3_buckets_allowed of this ViewBox.
        :type: bool
        """

        self._s3_buckets_allowed = s3_buckets_allowed

    @property
    def stats(self):
        """
        Gets the stats of this ViewBox.
        Specifies statistics about the Storage Domain (View Box). readOnly: true

        :return: The stats of this ViewBox.
        :rtype: ViewBoxStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this ViewBox.
        Specifies statistics about the Storage Domain (View Box). readOnly: true

        :param stats: The stats of this ViewBox.
        :type: ViewBoxStats
        """

        self._stats = stats

    @property
    def storage_policy(self):
        """
        Gets the storage_policy of this ViewBox.
        Specifies the storage options applied to the Storage Domain (View Box).

        :return: The storage_policy of this ViewBox.
        :rtype: StoragePolicy
        """
        return self._storage_policy

    @storage_policy.setter
    def storage_policy(self, storage_policy):
        """
        Sets the storage_policy of this ViewBox.
        Specifies the storage options applied to the Storage Domain (View Box).

        :param storage_policy: The storage_policy of this ViewBox.
        :type: StoragePolicy
        """

        self._storage_policy = storage_policy

    @property
    def treat_file_sync_as_data_sync(self):
        """
        Gets the treat_file_sync_as_data_sync of this ViewBox.
        If 'true', when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.) Only set to 'false' if your environment requires a very accurate modification time. The default value is 'true' which provides the best Cohesity Cluster performance.

        :return: The treat_file_sync_as_data_sync of this ViewBox.
        :rtype: bool
        """
        return self._treat_file_sync_as_data_sync

    @treat_file_sync_as_data_sync.setter
    def treat_file_sync_as_data_sync(self, treat_file_sync_as_data_sync):
        """
        Sets the treat_file_sync_as_data_sync of this ViewBox.
        If 'true', when the Cohesity Cluster is writing to a file, the file modification time is not persisted synchronously during the file write, so the modification time may not be accurate. (Typically the file modification time is off by 30 seconds but it can be longer.) Only set to 'false' if your environment requires a very accurate modification time. The default value is 'true' which provides the best Cohesity Cluster performance.

        :param treat_file_sync_as_data_sync: The treat_file_sync_as_data_sync of this ViewBox.
        :type: bool
        """

        self._treat_file_sync_as_data_sync = treat_file_sync_as_data_sync

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