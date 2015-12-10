# coding: utf-8

"""
PositionApi.py
Copyright 2015 SmartBear Software

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

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PositionApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def position_find(self, **kwargs):
        """
        Get your positions.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.position_find(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Table filter. For example, send {\"symbol\": \"XBT24H\"}.
        :param str columns: Which columns to fetch. For example, send [\"columnName\"].
        :param float count: Number of rows to fetch.
        :return: list[Position]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'columns', 'count']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method position_find" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/position'.replace('{format}', 'json')
        method = 'GET'

        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'columns' in params:
            query_params['columns'] = params['columns']
        if 'count' in params:
            query_params['count'] = params['count']

        header_params = {}

        form_params = {}
        files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='list[Position]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def position_isolate_margin(self, symbol, **kwargs):
        """
        Toggle isolated (fixed) margin per-position.
        On Speculative (DPE-Enabled) contracts, users can switch isolate margin per-position. This function allows switching margin isolation (aka fixed margin) on and off. A position must be open to isolate it.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.position_isolate_margin(symbol, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str symbol: Position symbol to isolate. (required)
        :param bool enabled: If true, will enable isolated margin.
        :return: Position
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'enabled']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method position_isolate_margin" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'symbol' is set
        if ('symbol' not in params) or (params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `position_isolate_margin`")

        resource_path = '/position/isolate'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'symbol' in params:
            form_params['symbol'] = params['symbol']
        if 'enabled' in params:
            form_params['enabled'] = params['enabled']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='Position',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def position_transfer_isolated_margin(self, symbol, amount, **kwargs):
        """
        Transfer equity in or out of a position.
        When margin is isolated on a position, use this function to add or remove margin from the position. Note that you cannot remove margin below the initial margin threshold.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.position_transfer_isolated_margin(symbol, amount, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str symbol: Position symbol to isolate. (required)
        :param float amount: Amount to transfer, in satoshis. May be negative. (required)
        :return: Position
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['symbol', 'amount']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method position_transfer_isolated_margin" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'symbol' is set
        if ('symbol' not in params) or (params['symbol'] is None):
            raise ValueError("Missing the required parameter `symbol` when calling `position_transfer_isolated_margin`")
        # verify the required parameter 'amount' is set
        if ('amount' not in params) or (params['amount'] is None):
            raise ValueError("Missing the required parameter `amount` when calling `position_transfer_isolated_margin`")

        resource_path = '/position/transferMargin'.replace('{format}', 'json')
        method = 'POST'

        path_params = {}

        query_params = {}

        header_params = {}

        form_params = {}
        files = {}
        if 'symbol' in params:
            form_params['symbol'] = params['symbol']
        if 'amount' in params:
            form_params['amount'] = params['amount']

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'application/xml', 'text/xml', 'application/javascript', 'text/javascript'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        response = self.api_client.call_api(resource_path, method,
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=files,
                                            response_type='Position',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response