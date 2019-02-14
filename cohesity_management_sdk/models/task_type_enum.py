# -*- coding: utf-8 -*-

class TaskTypeEnum(object):

    """Implementation of the 'TaskType' enum.

    Task type denotes which type of task this notification is for.
    This param is used to reflect the taskType.
    'Restore' notification type is generated upon completion of Restore
    tasks.
    'Clone' notification type is generated upon completion of Clone tasks.
    'BackupNow' notification type is generated upon completion of Backup
    tasks.
    'FieldMessage' notification type is generated when field message from
    Cohesity support is created.

    Attributes:
        RESTORE: TODO: type description here.
        CLONE: TODO: type description here.
        BACKUPNOW: TODO: type description here.
        FIELDMESSAGE: TODO: type description here.

    """

    RESTORE = 'Restore'

    CLONE = 'Clone'

    BACKUPNOW = 'BackupNow'

    FIELDMESSAGE = 'FieldMessage'

