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


class CopyRun(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, copy_snapshot_tasks=None, error=None, expiry_time_usecs=None, run_start_time_usecs=None, stats=None, status=None, target=None, task_uid=None, user_action_message=None):
        """
        CopyRun - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'copy_snapshot_tasks': 'list[CopySnapshotTaskStatus]',
            'error': 'str',
            'expiry_time_usecs': 'int',
            'run_start_time_usecs': 'int',
            'stats': 'CopyRunStats',
            'status': 'str',
            'target': 'SnapshotTarget',
            'task_uid': 'CopyRunTaskUid',
            'user_action_message': 'str'
        }

        self.attribute_map = {
            'copy_snapshot_tasks': 'copySnapshotTasks',
            'error': 'error',
            'expiry_time_usecs': 'expiryTimeUsecs',
            'run_start_time_usecs': 'runStartTimeUsecs',
            'stats': 'stats',
            'status': 'status',
            'target': 'target',
            'task_uid': 'taskUid',
            'user_action_message': 'userActionMessage'
        }

        self._copy_snapshot_tasks = copy_snapshot_tasks
        self._error = error
        self._expiry_time_usecs = expiry_time_usecs
        self._run_start_time_usecs = run_start_time_usecs
        self._stats = stats
        self._status = status
        self._target = target
        self._task_uid = task_uid
        self._user_action_message = user_action_message

    @property
    def copy_snapshot_tasks(self):
        """
        Gets the copy_snapshot_tasks of this CopyRun.
        Specifies the status information of each task that copies the snapshot taken for a Protection Source.

        :return: The copy_snapshot_tasks of this CopyRun.
        :rtype: list[CopySnapshotTaskStatus]
        """
        return self._copy_snapshot_tasks

    @copy_snapshot_tasks.setter
    def copy_snapshot_tasks(self, copy_snapshot_tasks):
        """
        Sets the copy_snapshot_tasks of this CopyRun.
        Specifies the status information of each task that copies the snapshot taken for a Protection Source.

        :param copy_snapshot_tasks: The copy_snapshot_tasks of this CopyRun.
        :type: list[CopySnapshotTaskStatus]
        """

        self._copy_snapshot_tasks = copy_snapshot_tasks

    @property
    def error(self):
        """
        Gets the error of this CopyRun.
        Specifies if an error occurred (if any) while running this task. This field is populated when the status is equal to 'kFailure'.

        :return: The error of this CopyRun.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this CopyRun.
        Specifies if an error occurred (if any) while running this task. This field is populated when the status is equal to 'kFailure'.

        :param error: The error of this CopyRun.
        :type: str
        """

        self._error = error

    @property
    def expiry_time_usecs(self):
        """
        Gets the expiry_time_usecs of this CopyRun.
        Specifies expiry time of the copies of the snapshots in this Protection Run.

        :return: The expiry_time_usecs of this CopyRun.
        :rtype: int
        """
        return self._expiry_time_usecs

    @expiry_time_usecs.setter
    def expiry_time_usecs(self, expiry_time_usecs):
        """
        Sets the expiry_time_usecs of this CopyRun.
        Specifies expiry time of the copies of the snapshots in this Protection Run.

        :param expiry_time_usecs: The expiry_time_usecs of this CopyRun.
        :type: int
        """

        self._expiry_time_usecs = expiry_time_usecs

    @property
    def run_start_time_usecs(self):
        """
        Gets the run_start_time_usecs of this CopyRun.
        Specifies start time of the copy run.

        :return: The run_start_time_usecs of this CopyRun.
        :rtype: int
        """
        return self._run_start_time_usecs

    @run_start_time_usecs.setter
    def run_start_time_usecs(self, run_start_time_usecs):
        """
        Sets the run_start_time_usecs of this CopyRun.
        Specifies start time of the copy run.

        :param run_start_time_usecs: The run_start_time_usecs of this CopyRun.
        :type: int
        """

        self._run_start_time_usecs = run_start_time_usecs

    @property
    def stats(self):
        """
        Gets the stats of this CopyRun.
        Specifies the aggregated information of all the copy tasks.

        :return: The stats of this CopyRun.
        :rtype: CopyRunStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this CopyRun.
        Specifies the aggregated information of all the copy tasks.

        :param stats: The stats of this CopyRun.
        :type: CopyRunStats
        """

        self._stats = stats

    @property
    def status(self):
        """
        Gets the status of this CopyRun.
        Specifies the aggregated status of copy tasks such as 'kRunning', 'kSuccess', 'kFailure' etc. 'kAccepted' indicates the task is queued to run but not yet running. 'kRunning' indicates the task is running. 'kCanceling' indicates a request to cancel the task has occurred but the task is not yet canceled. 'kCanceled' indicates the task has been canceled. 'kSuccess' indicates the task was successful. 'kFailure' indicates the task failed.

        :return: The status of this CopyRun.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CopyRun.
        Specifies the aggregated status of copy tasks such as 'kRunning', 'kSuccess', 'kFailure' etc. 'kAccepted' indicates the task is queued to run but not yet running. 'kRunning' indicates the task is running. 'kCanceling' indicates a request to cancel the task has occurred but the task is not yet canceled. 'kCanceled' indicates the task has been canceled. 'kSuccess' indicates the task was successful. 'kFailure' indicates the task failed.

        :param status: The status of this CopyRun.
        :type: str
        """
        allowed_values = ["kAccepted", "kRunning", "kCanceling", "kCanceled", "kSuccess", "kFailure"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def target(self):
        """
        Gets the target of this CopyRun.
        Specifies the target of the copy task such as an external target or a Remote Cohesity Cluster.

        :return: The target of this CopyRun.
        :rtype: SnapshotTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this CopyRun.
        Specifies the target of the copy task such as an external target or a Remote Cohesity Cluster.

        :param target: The target of this CopyRun.
        :type: SnapshotTarget
        """

        self._target = target

    @property
    def task_uid(self):
        """
        Gets the task_uid of this CopyRun.


        :return: The task_uid of this CopyRun.
        :rtype: CopyRunTaskUid
        """
        return self._task_uid

    @task_uid.setter
    def task_uid(self, task_uid):
        """
        Sets the task_uid of this CopyRun.


        :param task_uid: The task_uid of this CopyRun.
        :type: CopyRunTaskUid
        """

        self._task_uid = task_uid

    @property
    def user_action_message(self):
        """
        Gets the user_action_message of this CopyRun.
        Specifies a message to the user if any manual intervention is needed to make forward progress for the archival task. This message is mainly relevant for tape based archival tasks where a backup admin might be asked to load a new media when the tape library does not have any more media to use.

        :return: The user_action_message of this CopyRun.
        :rtype: str
        """
        return self._user_action_message

    @user_action_message.setter
    def user_action_message(self, user_action_message):
        """
        Sets the user_action_message of this CopyRun.
        Specifies a message to the user if any manual intervention is needed to make forward progress for the archival task. This message is mainly relevant for tape based archival tasks where a backup admin might be asked to load a new media when the tape library does not have any more media to use.

        :param user_action_message: The user_action_message of this CopyRun.
        :type: str
        """

        self._user_action_message = user_action_message

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