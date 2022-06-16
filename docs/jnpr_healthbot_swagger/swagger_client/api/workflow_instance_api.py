{# Copyright (c) 2022, Juniper Networks, Inc.
# All rights reserved.
}
# coding: utf-8

"""
    Paragon Insights APIs

    API interface for PI application  # noqa: E501

    OpenAPI spec version: 4.0.0
    Contact: healthbot-feedback@juniper.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class WorkflowInstanceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_healthbot_workflow_instance_by_id(self, workflow_name, **kwargs):  # noqa: E501
        """Create workflow by ID  # noqa: E501

        Create operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_healthbot_workflow_instance_by_id(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: ID of workflow-name (required)
        :param str x_iam_token: authentication header object
        :param WorkflowInstanceSchema workflow: workflowbody object
        :return: WorkflowInstanceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
        else:
            (data) = self.create_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
            return data

    def create_healthbot_workflow_instance_by_id_with_http_info(self, workflow_name, **kwargs):  # noqa: E501
        """Create workflow by ID  # noqa: E501

        Create operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_healthbot_workflow_instance_by_id_with_http_info(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: ID of workflow-name (required)
        :param str x_iam_token: authentication header object
        :param WorkflowInstanceSchema workflow: workflowbody object
        :return: WorkflowInstanceSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_name', 'x_iam_token', 'workflow']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_healthbot_workflow_instance_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_name' is set
        if ('workflow_name' not in params or
                params['workflow_name'] is None):
            raise ValueError("Missing the required parameter `workflow_name` when calling `create_healthbot_workflow_instance_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_name' in params:
            path_params['workflow_name'] = params['workflow_name']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workflow' in params:
            body_params = params['workflow']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instance/{workflow_name}/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowInstanceSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_healthbot_workflow_instance_by_id(self, workflow_name, **kwargs):  # noqa: E501
        """Delete workflow instance by ID  # noqa: E501

        Delete operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_healthbot_workflow_instance_by_id(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: ID of workflow instance
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
            return data

    def delete_healthbot_workflow_instance_by_id_with_http_info(self, workflow_name, **kwargs):  # noqa: E501
        """Delete workflow instance by ID  # noqa: E501

        Delete operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_healthbot_workflow_instance_by_id_with_http_info(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: ID of workflow instance
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_name', 'x_iam_token', 'workflow_instance_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_healthbot_workflow_instance_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_name' is set
        if ('workflow_name' not in params or
                params['workflow_name'] is None):
            raise ValueError("Missing the required parameter `workflow_name` when calling `delete_healthbot_workflow_instance_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_name' in params:
            path_params['workflow_name'] = params['workflow_name']  # noqa: E501

        query_params = []
        if 'workflow_instance_name' in params:
            query_params.append(('workflow_instance_name', params['workflow_instance_name']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instance/{workflow_name}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_healthbot_workflow_instances(self, **kwargs):  # noqa: E501
        """Delete workflow by ID  # noqa: E501

        Delete operation of resource: workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_healthbot_workflow_instances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_healthbot_workflow_instances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.delete_healthbot_workflow_instances_with_http_info(**kwargs)  # noqa: E501
            return data

    def delete_healthbot_workflow_instances_with_http_info(self, **kwargs):  # noqa: E501
        """Delete workflow by ID  # noqa: E501

        Delete operation of resource: workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_healthbot_workflow_instances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_healthbot_workflow_instances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instances/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_healthbot_workflow_instance_by_id(self, workflow_name, **kwargs):  # noqa: E501
        """Retrieve workflow by ID  # noqa: E501

        Retrieve operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_healthbot_workflow_instance_by_id(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: Name of the workflow instance
        :param bool extensive: Get extensive information including logs
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_healthbot_workflow_instance_by_id_with_http_info(workflow_name, **kwargs)  # noqa: E501
            return data

    def retrieve_healthbot_workflow_instance_by_id_with_http_info(self, workflow_name, **kwargs):  # noqa: E501
        """Retrieve workflow by ID  # noqa: E501

        Retrieve operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_healthbot_workflow_instance_by_id_with_http_info(workflow_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: Name of the workflow instance
        :param bool extensive: Get extensive information including logs
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_name', 'x_iam_token', 'workflow_instance_name', 'extensive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_healthbot_workflow_instance_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_name' is set
        if ('workflow_name' not in params or
                params['workflow_name'] is None):
            raise ValueError("Missing the required parameter `workflow_name` when calling `retrieve_healthbot_workflow_instance_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_name' in params:
            path_params['workflow_name'] = params['workflow_name']  # noqa: E501

        query_params = []
        if 'workflow_instance_name' in params:
            query_params.append(('workflow_instance_name', params['workflow_instance_name']))  # noqa: E501
        if 'extensive' in params:
            query_params.append(('extensive', params['extensive']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instance/{workflow_name}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowInstancesSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_healthbot_workflow_instances(self, **kwargs):  # noqa: E501
        """Retrieve workflow instances  # noqa: E501

        Retrieve operation of all workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_healthbot_workflow_instances(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.retrieve_healthbot_workflow_instances_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_healthbot_workflow_instances_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_healthbot_workflow_instances_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve workflow instances  # noqa: E501

        Retrieve operation of all workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_healthbot_workflow_instances_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_iam_token: authentication header object
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_healthbot_workflow_instances" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instances/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowInstancesSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_healthbot_workflow_instance_by_id(self, workflow_name, operation, **kwargs):  # noqa: E501
        """Retrieve workflow by ID  # noqa: E501

        Update operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_healthbot_workflow_instance_by_id(workflow_name, operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str operation: Name of the update operation (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: Name of the workflow instance
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_healthbot_workflow_instance_by_id_with_http_info(workflow_name, operation, **kwargs)  # noqa: E501
        else:
            (data) = self.update_healthbot_workflow_instance_by_id_with_http_info(workflow_name, operation, **kwargs)  # noqa: E501
            return data

    def update_healthbot_workflow_instance_by_id_with_http_info(self, workflow_name, operation, **kwargs):  # noqa: E501
        """Retrieve workflow by ID  # noqa: E501

        Update operation of resource: workflow instance  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_healthbot_workflow_instance_by_id_with_http_info(workflow_name, operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow_name: Name of the workflow (required)
        :param str operation: Name of the update operation (required)
        :param str x_iam_token: authentication header object
        :param str workflow_instance_name: Name of the workflow instance
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow_name', 'operation', 'x_iam_token', 'workflow_instance_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_healthbot_workflow_instance_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workflow_name' is set
        if ('workflow_name' not in params or
                params['workflow_name'] is None):
            raise ValueError("Missing the required parameter `workflow_name` when calling `update_healthbot_workflow_instance_by_id`")  # noqa: E501
        # verify the required parameter 'operation' is set
        if ('operation' not in params or
                params['operation'] is None):
            raise ValueError("Missing the required parameter `operation` when calling `update_healthbot_workflow_instance_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workflow_name' in params:
            path_params['workflow_name'] = params['workflow_name']  # noqa: E501

        query_params = []
        if 'operation' in params:
            query_params.append(('operation', params['operation']))  # noqa: E501
        if 'workflow_instance_name' in params:
            query_params.append(('workflow_instance_name', params['workflow_instance_name']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instance/{workflow_name}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowInstancesSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_healthbot_workflow_instances(self, operation, **kwargs):  # noqa: E501
        """Update workflow instances  # noqa: E501

        Update operation of all workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_healthbot_workflow_instances(operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operation: Name of the update operation (required)
        :param str x_iam_token: authentication header object
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_healthbot_workflow_instances_with_http_info(operation, **kwargs)  # noqa: E501
        else:
            (data) = self.update_healthbot_workflow_instances_with_http_info(operation, **kwargs)  # noqa: E501
            return data

    def update_healthbot_workflow_instances_with_http_info(self, operation, **kwargs):  # noqa: E501
        """Update workflow instances  # noqa: E501

        Update operation of all workflow instances  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_healthbot_workflow_instances_with_http_info(operation, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str operation: Name of the update operation (required)
        :param str x_iam_token: authentication header object
        :return: WorkflowInstancesSchema
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['operation', 'x_iam_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_healthbot_workflow_instances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'operation' is set
        if ('operation' not in params or
                params['operation'] is None):
            raise ValueError("Missing the required parameter `operation` when calling `update_healthbot_workflow_instances`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'operation' in params:
            query_params.append(('operation', params['operation']))  # noqa: E501

        header_params = {}
        if 'x_iam_token' in params:
            header_params['x-iam-token'] = params['x_iam_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/workflow-instances/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WorkflowInstancesSchema',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
