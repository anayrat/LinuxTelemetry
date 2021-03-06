#!/usr/bin/python

##########################################################################
# Copyright (c) 2015, Salesforce.com, Inc.
# All rights reserved.
#
# Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#
# Neither the name of Salesforce.com nor the names of its
# contributors may be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
# GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
##########################################################################

############################################################
# Mockup for collectd for testing plugins as well as for
# generating docs
############################################################

import socket

class Values:
    def __init__(self):
        self.host = socket.gethostbyaddr(socket.gethostname())[0]
        self.plugin = 'test-plugin'
        self.type = 'test-type'
        self.type_instance = 'test-type-instance'
        self.values = []

    def dispatch(self):
        print('dispatch: type_instance: %s value: %s' % (self.type_instance, self.values))

def info(params):
    print('INFO: ' + params)

def warn(params):
    print('WARN: ' + params)

def error(params):
    print('ERROR: ' + params)

def debug(params):
    print('DEBUG: ' + params)

def register_config(params):
    pass

def register_init(params):
    pass

def register_read(params):
    pass

def register_write(params):
    pass

def register_shutdown(params):
    pass
