# swagger_client.UtilityApi

All URIs are relative to *http://api-server/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**junosdecode**](UtilityApi.md#junosdecode) | **POST** /junos-decode/ | Decode string with Junos
[**junosencode**](UtilityApi.md#junosencode) | **POST** /junos-encode/ | Encode string with Junos


# **junosdecode**
> Data1 junosdecode(data, x_iam_token=x_iam_token)

Decode string with Junos

Decode string with Junos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilityApi()
data = swagger_client.Data1() # Data1 | String to Encode with Junos
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Decode string with Junos
    api_response = api_instance.junosdecode(data, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->junosdecode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data1**](Data1.md)| String to Encode with Junos | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**Data1**](Data1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **junosencode**
> Data junosencode(data, x_iam_token=x_iam_token)

Encode string with Junos

Encode string with Junos

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilityApi()
data = swagger_client.Data() # Data | String to Encode with Junos
x_iam_token = 'x_iam_token_example' # str | authentication header object (optional)

try:
    # Encode string with Junos
    api_response = api_instance.junosencode(data, x_iam_token=x_iam_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilityApi->junosencode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)| String to Encode with Junos | 
 **x_iam_token** | **str**| authentication header object | [optional] 

### Return type

[**Data**](Data.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

