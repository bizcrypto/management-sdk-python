# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

class InstallStateEnum(object):

    """Implementation of the 'InstallState' enum.

    Specifies app installation status.
    Specifies status of the app installation.
    kNotInstalled - App yet to be installed.
    kInstallInProgress - App installation is in progress.
    kInstalled - App is installed successfully and can be launched.
    kInstallFailed - App installation failed.
    kUninstallInProgress - App uninstallation is in progress.
    kUninstallFailed - App uninstallation failed.

    Attributes:
        KNOTINSTALLED: TODO: type description here.
        KINSTALLINPROGRESS: TODO: type description here.
        KINSTALLED: TODO: type description here.
        KINSTALLFAILED: TODO: type description here.
        KUNINSTALLINPROGRESS: TODO: type description here.
        KUNINSTALLFAILED: TODO: type description here.

    """

    KNOTINSTALLED = 'kNotInstalled'

    KINSTALLINPROGRESS = 'kInstallInProgress'

    KINSTALLED = 'kInstalled'

    KINSTALLFAILED = 'kInstallFailed'

    KUNINSTALLINPROGRESS = 'kUninstallInProgress'

    KUNINSTALLFAILED = 'kUninstallFailed'

