# Copyright 2019 Cohesity Inc.
#
# Python example to list recent user_configurable unresolved alert unresolved Alerts.
#
# Usage: python list_unresolved_alerts.py --max_alerts 10

import argparse
import datetime

from cohesity_management_sdk.cohesity_client import CohesityClient
from cohesity_management_sdk.models.alert_state_list_enum import AlertStateListEnum

CLUSTER_USERNAME = 'cluster_username'
CLUSTER_PASSWORD = 'cluster_password'
CLUSTER_VIP = 'prod-cluster.cohesity.com'
MAX_ALERTS = 100

class Alerts(object):
    """
    Class to display Alerts.
    """
    severity_map = {'kCritical':'CRITICAL', 'kWarning':'WARNING', 'kInfo':'INFO'}
    category_map = {'kDisk':'DISK', 'kNode': 'NODE', 'kCluster': 'CLUSTER', 'kNodeHealth': 'NODE_HEALTH',
                    'kClusterHealth': 'CLUSTER_HEALTH', 'kBackupRestore': 'BACKUP_RESTORE', 'kEncryption':'ENCRYPTION',
                    'kArchivalRestore': 'ARCHIVAL_RESTORE'}

    def display_alerts(self, cohesity_client, max_alerts):
        """
        Method to display the list of Unresolved Alerts
        :param cohesity_client(object): Cohesity client object.
        :return:
        """
        alerts = cohesity_client.alerts
        alerts_list = alerts.get_alerts(max_alerts=max_alerts, alert_state_list=[AlertStateListEnum.KOPEN])
        for alert in alerts_list:
            print ('{0:<10}\t\t{1:>8}\t{2:>10}'.format(self.epoch_to_date(alert.first_timestamp_usecs),
                                                           self.category_map[alert.alert_category],
                                                           self.severity_map[alert.severity]))

    @staticmethod
    def epoch_to_date(epoch):
        """
        Method to convert epoch time in usec to date format
        :param epoch(int): Epoch time of the job run.
        :return: date(str): Date format of the job run.
        """
        date_string = datetime.datetime.fromtimestamp(epoch/10**6).strftime('%m-%d-%Y %H:%M:%S')
        return date_string

def main(args):

    # To init client with user/pass.
    cohesity_client = CohesityClient(username=CLUSTER_USERNAME, password=CLUSTER_PASSWORD)
    cohesity_client.config.cluster_vip = CLUSTER_VIP
    cohesity_client.config.enable_logging()
    cohesity_client.config.skip_ssl_verification = True

    alerts = Alerts()
    alerts.display_alerts(cohesity_client, args.max_alerts)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments needed to run this python process.")
    parser.add_argument("--max_alerts", help="Number of Alerts.", default=MAX_ALERTS)
    args = parser.parse_args()
    main(args)