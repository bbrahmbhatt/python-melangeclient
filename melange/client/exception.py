#!/usr/bin/env python
# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class ClientConnectionError(Exception):
    """Error resulting from a client connecting to a server"""
    pass


class MelangeClientError(Exception):

    def __init__(self, message):
        super(MelangeClientError, self).__init__(message)


class TemplateNotFoundError(Exception):

    def __init__(self, message=None):
        message = message or "template not found"
        super(TemplateNotFoundError, self).__init__(message)


class MelangeServiceResponseError(Exception):

    def __init__(self, error):
        super(MelangeServiceResponseError, self).__init__(error)
