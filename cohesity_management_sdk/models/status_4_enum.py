# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

class Status4Enum(object):

    """Implementation of the 'Status4' enum.

    Specifies the aggregated status of copy tasks such as 'kRunning',
    'kSuccess', 'kFailure' etc.
    'kAccepted' indicates the task is queued to run but not yet running.
    'kRunning' indicates the task is running.
    'kCanceling' indicates a request to cancel the task has occurred but
    the task is not yet canceled.
    'kCanceled' indicates the task has been canceled.
    'kSuccess' indicates the task was successful.
    'kFailure' indicates the task failed.

    Attributes:
        KACCEPTED: TODO: type description here.
        KRUNNING: TODO: type description here.
        KCANCELING: TODO: type description here.
        KCANCELED: TODO: type description here.
        KSUCCESS: TODO: type description here.
        KFAILURE: TODO: type description here.

    """

    KACCEPTED = 'kAccepted'

    KRUNNING = 'kRunning'

    KCANCELING = 'kCanceling'

    KCANCELED = 'kCanceled'

    KSUCCESS = 'kSuccess'

    KFAILURE = 'kFailure'

