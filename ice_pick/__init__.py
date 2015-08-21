"""
Ice Pick
~~~~~~~~~~~~~~~~~~~~

Ice Pick is a library that allows easy access to AWS billing data collected by
the Netflix OSS Ice tool.

Basic usage:

>>> from ice_pick.api import APIRequest

>>> api_request = APIRequest('http://example.com/ice/')
>>> api_request.get_data()
{
    'data': {
        'AWS Data Pipeline': [0.25148882999999966],
        'Alexa Web Information Service': [0.11130000000000001],
        'aggregated': [48884.90918908445],
        'cloudfront': [3241.575401989994],
        .
        .
        .
        'vpc': [296.7824844800026]
    },
    'groupBy': 'Product',
    'hours': [588],
    'start': 1391212800000,
    'stats': {
        'AWS Data Pipeline': {
            'average': 0.25148882999999966,
            'max': 0.25148882999999966,
            'total': 0.25148882999999966
        },
        'Alexa Web Information Service': {
            'average': 0.11130000000000001,
            'max': 0.11130000000000001,
            'total': 0.11130000000000001
        },
        'aggregated': {
            'average': 48884.90918908445,
            'max': 48884.90918908445,
            'total': 48884.90918908445
        },
        'cloudfront': {
            'average': 3241.575401989994,
            'max': 3241.575401989994,
            'total': 3241.575401989994
        },
        .
        .
        .
        'vpc': {
            'average': 296.7824844800026,
            'max': 296.7824844800026,
            'total': 296.7824844800026
            }
        },
    'status': 200,
    'time': [1391212800000]
}

Copyright 2014 Demand Media.

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


__title__ = 'ice_pick'
__version__ = '0.4'
__author__ = 'Demand Media'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2014 Demand Media'
