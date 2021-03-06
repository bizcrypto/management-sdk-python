# Copyright 2019 Cohesity Inc. # -*- coding: utf-8 -*-

import logging
from cohesity_management_sdk.api_helper import APIHelper
from cohesity_management_sdk.configuration import Configuration
from cohesity_management_sdk.controllers.base_controller import BaseController
from cohesity_management_sdk.http.auth.auth_manager import AuthManager
from cohesity_management_sdk.models.get_kms_configuration_response_parameters import GetKMSConfigurationResponseParameters
from cohesity_management_sdk.exceptions.error_error_exception import ErrorErrorException

class KmsConfiguration(BaseController):

    """A Controller to access Endpoints in the cohesity_management_sdk API."""

    def __init__(self, client=None, call_back=None):
        super(KmsConfiguration, self).__init__(client, call_back)
        self.logger = logging.getLogger(__name__)

    def get_kms_config(self,
                       server_ip=None):
        """Does a GET request to /public/kmsConfig.

        List KMS configurations in the cluster.

        Args:
            server_ip (string, optional): Specifies IP address of the KMS for
                which KMS configuration is requested. If server IP is not
                specified, all KMS configurations will be fetched.

        Returns:
            list of GetKMSConfigurationResponseParameters: Response from the
                API. Specifies a list of KMS configurations.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('get_kms_config called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for get_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_parameters = {
                'serverIp': server_ip
            }
            _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
                _query_parameters, Configuration.array_serialization)
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for get_kms_config.')
            _headers = {
                'accept': 'application/json'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for get_kms_config.')
            _request = self.http_client.get(_query_url, headers=_headers)
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'get_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for get_kms_config.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetKMSConfigurationResponseParameters.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def update_kms_config(self,
                          body=None):
        """Does a PUT request to /public/kmsConfig.

        Update KMS configurations in the cluster.

        Args:
            body (KMSConfiguration, optional): TODO: type description here.
                Example: 

        Returns:
            GetKMSConfigurationResponseParameters: Response from the API.
                Response after KMS has been updated.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('update_kms_config called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for update_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for update_kms_config.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for update_kms_config.')
            _request = self.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'update_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for update_kms_config.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetKMSConfigurationResponseParameters.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise

    def create_kms_config(self,
                          body=None):
        """Does a POST request to /public/kmsConfig.

        Returns the created KMS config.

        Args:
            body (KMSConfiguration, optional): TODO: type description here.
                Example: 

        Returns:
            GetKMSConfigurationResponseParameters: Response from the API.
                Response after KMS has been created.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        try:
            self.logger.info('create_kms_config called.')
    
            # Prepare query URL
            self.logger.info('Preparing query URL for create_kms_config.')
            _url_path = '/public/kmsConfig'
            _query_builder = Configuration.get_base_uri()
            _query_builder += _url_path
            _query_url = APIHelper.clean_url(_query_builder)
    
            # Prepare headers
            self.logger.info('Preparing headers for create_kms_config.')
            _headers = {
                'accept': 'application/json',
                'content-type': 'application/json; charset=utf-8'
            }
    
            # Prepare and execute request
            self.logger.info('Preparing and executing request for create_kms_config.')
            _request = self.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
            AuthManager.apply(_request)
            _context = self.execute_request(_request, name = 'create_kms_config')

            # Endpoint and global error handling using HTTP status codes.
            self.logger.info('Validating response for create_kms_config.')
            if _context.response.status_code == 0:
                raise ErrorErrorException('Error', _context)
            self.validate_response(_context)
    
            # Return appropriate type
            return APIHelper.json_deserialize(_context.response.raw_body, GetKMSConfigurationResponseParameters.from_dictionary)

        except Exception as e:
            self.logger.error(e, exc_info = True)
            raise
