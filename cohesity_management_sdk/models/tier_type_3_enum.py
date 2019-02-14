# -*- coding: utf-8 -*-

class TierType3Enum(object):

    """Implementation of the 'TierType3' enum.

    Specifies the storage class of Oracle vault.
    OracleTierType specifies the storage class for Oracle.
    'kOracleTierStandard' indicates a tier type of Oracle properties that
    requires fast, immediate and frequent access.
    'kOracleTierArchive' indicates a tier type of Oracle properties that is
    rarely accesed and preserved for long times.

    Attributes:
        KORACLETIERSTANDARD: TODO: type description here.
        KORACLETIERARCHIVE: TODO: type description here.

    """

    KORACLETIERSTANDARD = 'kOracleTierStandard'

    KORACLETIERARCHIVE = 'kOracleTierArchive'

