# cohesity.AccessTokensApi

All URIs are relative to *https://localhost/irisservices/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_access_token**](AccessTokensApi.md#generate_access_token) | **POST** /public/accessTokens | Generate an Access Token.


# **generate_access_token**
> AccessToken generate_access_token(body)

Generate an Access Token.

Before making other REST API requests, your REST client must make a 'POST /public/accessToken' request with a valid Cohesity username and password. This POST request returns an access token and type in the response that is generated by the Cohesity Cluster. Subsequent requests to other Cohesity REST API operations must specify the returned access token and type by setting 'Authorization' in the http header in the following format:  Authorization: token_type access_token  The generated token is valid for 24 hours. If a request is made with an expired token, the 'Token expired' error message is returned. Add code to your REST client to check for this error and request another access token before reissuing the request.

### Example 
```python
import time
import cohesity
from cohesity.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cohesity.AccessTokensApi()
body = cohesity.AccessTokenCredential() # AccessTokenCredential | Request to generate access token.

try: 
    # Generate an Access Token.
    api_response = api_instance.generate_access_token(body)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccessTokensApi->generate_access_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessTokenCredential**](AccessTokenCredential.md)| Request to generate access token. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
